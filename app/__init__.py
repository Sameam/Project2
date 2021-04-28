from flask import Flask

app = Flask(__name__)

from app import main 

if __name__=='__main__':
    app.run(debug=True)

