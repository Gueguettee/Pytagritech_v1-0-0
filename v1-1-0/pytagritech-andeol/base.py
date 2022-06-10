from flask import *
from flask_sqlalchemy import *

from flask_cors import CORS, cross_origin


app = Flask (__name__)


app.datas = [0]
app.ids   = [0]
app.dates = [0]
app.battery = 0
app.nbr = 0

app.lastSend = 0


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'f3cfe9ed8fae309f02079dbf'    
db = SQLAlchemy(app)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
