from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
db = SQLAlchemy(app)
app.config['SimQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'