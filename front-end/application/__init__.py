from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

password = os.getenv('password')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{password}@eventsdb:3306/eventsdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes