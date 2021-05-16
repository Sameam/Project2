from app.models import Users
from app import db

print("Warning: This code is use for create HSS admin")
print('')
print("If you are normal Users,please turn off this python code. Thank you")
print('')
print("Please Enter The Following Details To Create Admin")

name_not_created = True
while name_not_created:
    name = input("Enter The Name Of The Admin:  ")
    if Users.query.filter(Users.name==name).count()>0:
        print("This name already exists. Please use a different name.")
    else:
        name_not_created=False

email_not_created = True
while email_not_created:
    email = input("Enter The Email of You:  ")
    if Users.query.filter(Users.email==email).count()>0:
        print("This email already exists. Please use a different email.")
    else:
        email_not_created=False

phone_not_created = True
while phone_not_created:
    phone = input("Enter The phone of You:  ")
    if Users.query.filter(Users.phone==phone).count()>0:
        print("This phone already exists. Please use a different phone.")
    else:
        phone_not_created=False

Users = Users(name=name, email=email, phone=phone, admin=True)

password_not_created = True
while password_not_created:
    password = input("Enter The Password of You:  ")
    if len(password)>=6:
        password_not_created=False
    else:
        print("Password Should Be Atleast 6 Characters.")
Users.set_password(password)
db.session.add(Users)
db.session.commit()
print("Admin Created Successfully.")