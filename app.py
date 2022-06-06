from re import S
from flask import Flask, request
from flask import render_template
from db_data import conn

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def loginSuccs():
    username =  request.form['username'] 
    password = request.form['password']
    cur = conn.cursor()
    cur.execute('SELECT * FROM admin;')
    admin = cur.fetchall()
    print(admin, username, password)
    cur.close()
    return render_template('home.html', data = username)


@app.route("/svi")
def sviRadnici():
    return render_template("svi.html")

@app.route("/dodaj")
def dodajZaposlenika():
    return render_template("dodaj.html")

# auto restart server on change
app.run(debug=True)
