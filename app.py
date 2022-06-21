from turtle import position
from xmlrpc.client import boolean
from flask import Flask, request
from flask import render_template
from db_data import conn
import pandas as db

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def loginSuccess():
    try:
        username =  request.form['username'] 
        password = request.form['password']
        cur = conn.cursor()
        bolean = cur.execute("SELECT * FROM admin where id = " + username)
        bolean = cur.fetchall()
        print(bolean)
        if(bolean != [] and password == bolean[0][1]):
            cur.close()
            return render_template('home.html', data = boolean)
        else:
            cur.execute("ROLLBACK")
            conn.commit()
            message = "Nemate pristup ovoj aplikaciji"
            return render_template("login.html",  data = message)
    except:
        cur.execute("ROLLBACK")
        conn.commit()
        message = "Nemate pristup ovoj aplikaciji"
        return render_template("login.html",data =  message)

@app.route("/logout")
def logout():
    return render_template("login.html")

@app.route("/svi")
def svi():
    cur = conn.cursor()
    cur.execute("SELECT * FROM radnici")
    data = cur.fetchall()
    return render_template("svi.html", data = data)

@app.route('/editUser', methods=["GET", "POST"])
def editUser ():
    try: 
        cur = conn.cursor()
        cur.execute("SELECT * FROM radnici")
        data = cur.fetchall()
        return render_template("editUser.html", data = data)
    except:
        cur.execute("ROLLBACK")
        conn.commit()
        message = "ID ne postoji u Bazi"
        return render_template('error.html', message=message)

@app.route('/deleteUser', methods=["POST"])
def deleteUser ():
    try:
        id =  request.form['id'] 
        cur = conn.cursor()
        cur.execute("SELECT * FROM radnici")
        data = cur.fetchall()
        return render_template("svi.html", data = data)
    except:
        cur.execute("ROLLBACK")
        conn.commit()
        message = "ID ne postoji u Bazi"
        return render_template('error.html', message=message)

@app.route("/dodaj")
def dodaj():
    cur = conn.cursor()
    cur.execute("SELECT * FROM radnici")
    data = cur.fetchall()
    return render_template("dodaj.html", data = data)

@app.route("/unesi", methods=["POST"])
def unesi():
    if request.method == 'POST':
        firstname =  request.form['firstname'] 
        lastname = request.form['lastname']
        birthday =  request.form['birthday'] 
        adress =  request.form['adress'] 
        email = request.form['email']
        phone =  request.form['phone'] 
        department = request.form['department']
        position = request.form['position']
        print(firstname, lastname,birthday,adress,email,phone,department,position)

@app.route("/događaji")
def događaji():
    cur = conn.cursor()
    cur.execute("SELECT * FROM radnici")
    data = cur.fetchall()
    return render_template("događaji.html", data = data)

@app.route("/obrasci")
def obrasci():
    cur = conn.cursor()
    cur.execute("SELECT * FROM radnici")
    data = cur.fetchall()
    return render_template("obrasci.html", data = data)
# auto restart server on change

app.run(debug=True)
