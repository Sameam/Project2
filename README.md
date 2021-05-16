# project 2
Requirements:
1. Python 3.0+ 
2. PIP 


How to Start the Project:
1. Open the CMD/Terminal in the project2 folder
2. In window write in dir, in linux/mac write ls in terminal and press enter 
    * Verify that you are inside the project 2 and can see app folder
3. Install the venv or virtual environment in the system by entering the command
    * python -m venv venv (In window)
    * python3 -m venv venv (In mac/linux)
4. After installing the venv, activate the venv using the following command
    * source venv/bin/activate (In mac/linux)
    * venv\Scripts\activate (In window)
5. Install all the project requirment by entering the command
    * pip install -r requirements.txt (In windows)
    * pip3 install -r requirements.txt (In mac)
    * sudo pip3 install -r requirments.txt (In Linux)
6. There will need to be create a database first. 
    * To create a database, flask db init 
    * flask db migrate -m "name for the table"
    * flask db upgrade
7. To run the server type the command
    * set FlASK_APP=app(for window)
    * export FLASK_APP=app (for Mac/Linux)
    * flask run 

Your Project will get start
* It will give you the host address 
* Copy the address and paste it into your any favorite Browser


There are two panels inside the projects:
1. Admin 
2. User

How To Create An Admin User
1. Run The Command 
* ---->python createsuperuser.py(In windows)
* ---->sudo python3 createsuperuser.py (In Linux)
* ---->python3 createSuperUser.py (In Mac)
Enter the details asked by the Command Prompt
It will create a new super user.


How to run test cases.
For testing, we first need to open __init__.py and change app.config.from_object(Config) to app.config.from_object('config.TestingConfig'). This will create a test.db which is a testing database. 
1. Front_end test case
* **Make sure that your server is up and running. You can do flask run first in one of your terminal or cmd. Then**
* ---->python test_front_end.py(for window)
* ---->python3 test_front_end.py(for Mac/Linux)
2. Back_end test case
* ---->python test_back_end.py(for window)
* ---->python3 test_back_end.py(for Mac/Linux)
