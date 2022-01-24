from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

# Using import secrets --> secrets.token_hex(64) to generate us a 64 byte key
app.config['SECRET_KEY'] = '50c72b086099e7dae1970ccc255a78411113c75173fad7aa6e9678091c4bb7cf04e1d6f220a396fada70f53a655cbd9fa5d0e68f5590256da0c750436ecc7e4e'
# Creating SqlLite database and an instance of it
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flaskblog import routes