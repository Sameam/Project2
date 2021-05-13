import os,unittest,time

from flask import url_for
from flask_testing import LiveServerTestCase
from selenium import webdriver
from app import  app,db
from app.models import Users

from config import basedir 

# name for admin 1
test_admin_name = "Admin"
test_admin_password = "admin@123"
test_admin_email = "admin@gmail.com"
test_admin_phone = "0312934804"

# name for user 1 
test_user1_name = "User1"
test_user1_password = "user1@123"
test_user1_email = "user1@gmail.com"
test_user1_phone = "0321842740"

# name for user 2 
test_user2_name = "User2"
test_user2_password = "user2@123"
test_user2_email = "user2@gmail.com"
test_user2_phone = "0432984805"

BASE_URL = "http://127.0.0.1:5000/"

class TestBase(unittest.TestCase):
  
  def setUp(self):
      """
      Will be called before every test
      """
      # create a new Safari session
      self.driver = webdriver.Safari()
      if not self.driver:
        self.SkipTest("Browser is not available")
      else:
        db.init_app(app)
        db.create_all()
        user1 = Users(name=test_user1_name,password=test_user1_password,email=test_user1_password,phone=test_user1_phone,admin=False)
        admin = Users(name=test_admin_name,password=test_admin_password,email=test_admin_password,phone=test_admin_phone,admin=True)
        db.session.add(user1)
        db.session.add(admin)
        db.session.commit()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
      
  def tearDown(self):
    
    if self.driver:
      self.driver.close()
      db.session.query(Users).delete()
      db.session.commit()
      db.session.remove()
      # close the browser window
      
      
class UserRegistration(TestBase):
    register_url = (BASE_URL + "register")
    
    def test_registration(self):
      '''
      test whether can user can used register form to register 
      '''
      
      self.driver.get(self.register_url)
      time.sleep(5)
      
      # Fill in the registration form 
      self.driver.find_element_by_id("name").send_keys(test_user1_name)
      self.driver.find_element_by_id('email').send_keys(test_user1_email)
      self.driver.find_element_by_id('password').send_keys(test_user1_password)
      self.driver.find_element_by_id('password2').send_keys(test_user1_password)
      self.driver.find_element_by_id('telephone').send_keys(test_user1_phone)
      self.driver.find_element_by_id('submit').click()
      time.sleep(2)
      
      # assert that register redirect to login page
      assert url_for('login') in self.driver.current_url
      
      sucess_message = self.driver.find_element_by_class_name("alert").text
      assert "You have sucessfully registered" in sucess_message
      
      self.assertEqual(User.query.count(), 1)
      
      
class TestLogin(TestBase):
  login_url = (BASE_URL + "login")
  
  def test_login(self):
    # test whether user can used login form to login 
    self.driver.get(self.login_url)
    time.sleep(5)
    
    self.driver.find_element_by_id('name').send_keys(test_user1_name)
    self.driver.find_element_by_id('password').send_keys(test_user1_password)
    self.driver.find_element_by_id('submit').click()
    time.sleep(2)
    
    assert url_for('introduction') in self.driver.current_url
    
    name_greeting = self.driver.find_element_by_id("name_greeting").text
    assert "Hi User 1" in name_greeting

if __name__ == '__main__':
    unittest.main(verbosity=2)
  
  

      
      
      
      
    
    
  
  
  

