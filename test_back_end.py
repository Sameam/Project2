import os
import unittest
# from unittest.mock import patch

# from flask import abort, url_for
# from flask_testing import TestCase

from app import db, app
from app.models import Users
from config import basedir, Config

class TestConfig(Config):

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'test.db')

class UserModelCase(unittest.TestCase):
  
  def setup(self):
    self.app = create_app(TestConfig)
    self.app_context.push()
    db.create_all()
  
  def tearDown(self):
    db.session.remove()
    db.drop_all()
  
  def test_password_hashing(self):
    u = Users(name = "Sam")
    u.set_password("sam12345")
    
    self.assertFalse(u.check_password("sam23456"))
    self.assertTrue(u.check_password("sam12345"))
    
if __name__=='__main__':
  unittest.main(verbosity=2)