from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from setting import app

db = SQLAlchemy(app)

class Book(db.Model):