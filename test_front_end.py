import os,unittest,time

from flask import url_for
from flask_testing import LiveServerTestCase
from selenium import webdriver
from app import  db
from app.models import Users 

from config import base_dir 

# name for user 1 
test_user1_name = "User1"
test_user1_email = "user1@gmail.com"
test_user1_password = "user1@123"

# name for user 2 
test_user1_name = "User1"
test_user1_email = "user1@gmail.com"
test_user1_password = "user1@123"

BASE_URL = "http://127.0.0.1:5000"

class TestBase(unittest.TestCase):
  
  def setup(self):
    # create a chrome session 
    self.driver = webdriver.Chrome(os.path.join(BASE_DIR,"chromedriver.exe"))
  
  def teardown(self):
    pass
  
  
class UserRegistration(TestBase):
    register_url = (BASE_URL + "/register")
    
    
  
  
  

