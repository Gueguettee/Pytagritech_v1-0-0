from flask import *
from flask_sqlalchemy import *


app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'f3cfe9ed8fae309f02079dbf'    
db = SQLAlchemy(app)
