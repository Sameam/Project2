import os,unittest,time

from flask import url_for
from selenium import webdriver
from app import  db
from app.models import Users 

from config import basedir 

# name for user 1 
test_user1_name = "User1"
test_user1_email = "user1@gmail.com"
test_user1_password = "user1@123"

# name for user 2 
test_user2_name = "User2"
test_user2_email = "user2@gmail.com"
test_user2_password = "user2@123"

BASE_URL = "http://127.0.0.1:5000"

class TestBase(unittest.TestCase):
  
  driver = None
  
  def setup(self):
    # create a chrome session 
    self.driver = webdriver.Chrome(os.path.join(basedir,"chromedriver.exe"))
    if not self.driver:
      self.SkipTest("Browser not Available")
    else:
      db.init_app(app)
      db.create_all()
      u1 = Users("User1","user12345","user133@gmail.com","0234890804")  
      u2 = Users("User2","user12345","user233@gmail.com","0234890845")
      db.session.add(u1)
      db.session.add(u2)
      db.commit()
      self.driver.maximize_window()
      self.driver.get(BASE_URL)
  
  def teardown(self):
    if self.driver():
      # close the browser window
      self.driver.close()
      db.session.remove()
      db.drop_all()
      db.create_all()
  
  
class UserRegistration(TestBase):
    register_url = (BASE_URL + "/register")
    
    def test_registration(self):
      '''
      test whether can user can used register form to register 
      '''
      
      u = Users.query.get("User1")
      self.assertEqual(u.email,"user133@gmail.com","User exist in the database")
      # testing when user click the link
      self.driver.get(register_url)
      self.driver.implicitly_wait(5)
      name = self.driver.find_element_by_id("name")
      name.send_keys('User1')
      
      
      
    
    
  
  
  

