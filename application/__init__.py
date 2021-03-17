from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#this is where the website is created, it's a MUST
template_folder="../templates"

app=Flask(__name__, template_folder=template_folder)

#remote db, this is connecting to the SQL Database(DB) from my Virtual Machine (VM)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:bikeshop@35.189.125.22/bikeshop'
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True

db = SQLAlchemy(app)

from application import routes