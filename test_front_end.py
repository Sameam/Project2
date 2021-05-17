import os,unittest,time

from flask import url_for
from flask_testing import LiveServerTestCase
from selenium import webdriver
from app import  app,db
from app.models import Users

from config import basedir, Config

# name for admin 1
test_admin_name = "Admin"
test_admin_password = "admin1223"
test_admin_email = "admin12@gmail.com"
test_admin_phone = 8512934804

# name for user 1 
test_user1_name = "User1"
test_user1_password = "user1123"
test_user1_email = "user1@gmail.com"
test_user1_phone = 9321842740

# name for user 2 
test_user2_name = "User2"
test_user2_password = "user2123"
test_user2_email = "user2@gmail.com"
test_user2_phone = 5432984805

# name for user 3 
test_user3_name = "User3"
test_user3_password = "user3123"
test_user3_email = "user3@gmail.com"
test_user3_phone = 8632984805

BASE_URL = "http://127.0.0.1:5000/"

class TestConfig(Config):

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'test.db')

class TestBase(unittest.TestCase):
  
  driver = None
  
  def setUp(self):
    
    # create a chorme session 
    self.driver = webdriver.Chrome()

    if not self.driver:
      self.skipTest('Web browser not available')
    else:
      db.init_app(app)
      db.session.query(Users).delete()
      db.session.commit()
      db.session.remove()
      db.create_all()
      
      self.admin = Users(name=test_admin_name,password=test_admin_password,email=test_admin_email,phone=test_admin_phone,admin=True)
      db.session.add(self.admin)
      db.session.commit()
      self.driver.maximize_window()
      self.driver.get(BASE_URL)
      time.sleep(1)
    
  
  def tearDown(self):
    self.driver.close()
    db.session.query(Users).delete()
    db.session.commit()
    db.session.remove()
  
      
class UserRegistration(TestBase):
  register_url = (BASE_URL + "register")
  login_url = (BASE_URL + "/login")
    
  
  
  def test_registration(self):
    '''
    test whether can user can used register form to register 
    '''
    
    self.driver.get(self.register_url)
    time.sleep(1)
    
    # Fill in the registration form 
    self.driver.find_element_by_id("name").send_keys(test_user1_name)
    self.driver.find_element_by_id('email').send_keys(test_user1_email)
    self.driver.find_element_by_id('password').send_keys(test_user1_password)
    self.driver.find_element_by_id('password2').send_keys(test_user1_password)
    self.driver.find_element_by_id('telephone').send_keys(test_user1_phone)
    self.driver.find_element_by_id('submit').click()
    time.sleep(2)
    
  def test_registration_password_confirmation(self):
    ''' 
    check if we have 2 different password, is it going to allow user to sign up?
    '''
    
    self.driver.get(self.register_url)
    time.sleep(1)
    self.driver.find_element_by_id("name").send_keys(test_user3_name)
    self.driver.find_element_by_id('email').send_keys(test_user3_email)
    self.driver.find_element_by_id('password').send_keys(test_user3_password)
    self.driver.find_element_by_id('password2').send_keys(test_user2_password)
    self.driver.find_element_by_id('telephone').send_keys(test_user3_phone)
    self.driver.find_element_by_id('submit').click()
    time.sleep(2)
    

    
class TestLogin(TestBase):
  register_url = (BASE_URL + "/register")
  login_url = (BASE_URL + "/login")


  def test_login(self):
    
    ''' 
    check whether user can use the login form to fill the login
    '''
    
    self.driver.get(self.register_url)
    time.sleep(1)
    
    # Fill in the registration form 
    self.driver.find_element_by_id("name").send_keys(test_user2_name)
    self.driver.find_element_by_id('email').send_keys(test_user2_email)
    self.driver.find_element_by_id('password').send_keys(test_user2_password)
    self.driver.find_element_by_id('password2').send_keys(test_user2_password)
    self.driver.find_element_by_id('telephone').send_keys(test_user2_phone)
    self.driver.find_element_by_id('submit').click()
    time.sleep(1)
    
    # get the login url
    self.driver.get(self.login_url)
    time.sleep(2)
    

    # Fill in Login form
    self.driver.find_element_by_id("name").send_keys(test_user2_name)
    self.driver.find_element_by_id("password").send_keys(test_user2_password)

    self.driver.find_element_by_id("submit").click()
    time.sleep(2)
    
class TestAdmin(TestBase):
  register_url = (BASE_URL + "/register")
  login_url = (BASE_URL + "/login")
  
  def testAdminLogin(self): 
    
    
    ''' 
    check if admin can used login form to login 
    '''
    
    self.driver.get(self.login_url)
    time.sleep(2)
    

    # Fill in Login form
    self.driver.find_element_by_id("name").send_keys(test_admin_name)
    self.driver.find_element_by_id("password").send_keys(test_admin_password)

    self.driver.find_element_by_id("submit").click()
    time.sleep(2)
    

if __name__ == '__main__':
  unittest.main(verbosity=2)
  
  

      
      
      
      
    
    
  
  
  

