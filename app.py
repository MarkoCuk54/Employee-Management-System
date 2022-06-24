from turtle import position
from xmlrpc.client import boolean
from flask import Flask, request
from flask import render_template, request
from db_data import conn, db, Feedback
from datetime import datetime, date



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

@app.route('/deleteUser', methods=["POST"])
def deleteUser():
    try:
        id = request.form["id"]
        db.session.query(Feedback).filter(Feedback.id==id).delete()
        db.session.commit()
        message='Uspješno ste izbrisali zaposlenika'
        return render_template('error.html', message=message)
    except:
        message = "ID ne postoji u Bazi"
        return render_template('error.html', message=message)

@app.route("/deleteRow", methods=["DELETE"])
def deleteRow():
    id =  request.form['delete']
    cur = conn.cursor()
    cur.execute("DELETE * FROM radnici where id = " + id)
    conn.commit()
    data = cur.fetchall()
    print(data)
    return render_template("svi.html", data = data)

@app.route('/editUser', methods=["GET", "POST"])
def editUser ():
        id =  request.form['edit']
        cur = conn.cursor()
        cur.execute("SELECT * FROM radnici where id = " + id)
        data = cur.fetchall()
        print(data)
        return render_template("editUser.html", data = data[0])

@app.route("/dodaj")
def dodaj():
    cur = conn.cursor()
    cur.execute("SELECT * FROM radnici")
    data = cur.fetchall()
    return render_template("dodaj.html", data = data)

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
