
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:emerus2705@localhost/ems'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

con = psycopg2.connect(database="ems", user="postgres", password="emerus2705", host="127.0.0.1", port="5000")
cursor = con.cursor()
db = SQLAlchemy(app)

conn = psycopg2.connect(
        host="localhost",
        database="ems",
        user='postgres',
        password='emerus2705')

class Feedback(db.Model):
    __tablename__ = 'radnici'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    birthday = db.Column(db.String(30))
    adress = db.Column(db.String(30))
    email = db.Column(db.Text())
    phone   = db.Column(db.String(30))
    department = db.Column(db.Text())
    position   = db.Column(db.String(30))

    def __init__(self, id, firstname, lastname,  Satnica, Odjel, Opis, JMBG):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.JMBG = JMBG
        self.Satnica = Satnica
        self.Odjel = Odjel
        self.Opis = Opis
