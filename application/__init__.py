#imports flask module
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#this is where the website is created, it's a MUST
app = Flask(__name__)
#remote db, this is connecting to the SQL DB from my VM
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:devops@34.105.250.189/bikeshop'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True

db = SQLAlchemy(app)

from application import routes