from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#app.config['SECRET_KEY'] = 'your secret key'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#engine = sqlalchemy.create_engine('sqlite:///data.db', echo=True)
#db = declarative_base()
#session = sessionmaker(bind=engine)
#session = Session()
