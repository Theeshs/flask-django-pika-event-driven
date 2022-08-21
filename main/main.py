from dataclasses import dataclass
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate

from dotenv import load_dotenv
load_dotenv()

DB_URL = os.getenv("SQLALCHEMY_DATABASE_URI", "postgresql+psycopg2://postgres:mysecretpassword@dbmain/main")

if not DB_URL:
    raise Exception("No DB URL found")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db = SQLAlchemy(app)

migrate = Migrate(app, db)
CORS(app)

@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str
    
    id = db.Column(
        db.Integer, 
        primary_key=True,
        autoincrement=False
    )
    title = db.Column(
        db.String(200)
    )
    image = db.Column(
        db.String(200)
    )

@dataclass
class ProductUser(db.Model):
    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    user_id = db.Column(
        db.Integer, 
    )
    prodict_id = db.Column(
        db.Integer, 
    )
    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route('/api/products')
def index():
    return jsonify(Product.query.all())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')