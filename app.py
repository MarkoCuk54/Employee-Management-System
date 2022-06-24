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

@app.route('/editUser', methods=["GET", "POST"])
def editUser ():
        id =  request.form['edit']
        cur = conn.cursor()
        cur.execute("SELECT * FROM radnici where id = " + id)
        data = cur.fetchall()
        print(data)
        return render_template("editUser.html", data = data[0])

@app.route('/changeDepartment', methods=["POST"])
def changeDepartment():
        noviOdjel = request.form["department"]
        try:
            user = db.session.query(Feedback).filter(Feedback.id == editUser.id).one()
            user.Department = noviOdjel
            izmjena = db.session.query(changeDepartment).filter(changeDepartment.id == editUser.id).one()
            izmjena.izmjena = noviOdjel
            db.session.commit()
            message = "Uspješno ste promijenili odjel."
            return render_template('editUser.html', message=message)
        except:
            message = "Odjel je u pogrešnom formatu"
            return render_template('editUser.html', message=message)

@app.route("/dodaj")
def dodaj():
    if request.method == 'POST':
        id = request.form["id"]
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        birthday = request.form['birthday']
        adress = request.form["adress"]
        email = request.form["email"]
        phone = request.form["phone"]
        department = request.form["department"]
        position = request.form["position"]
        if id == '' or firstname == '' or lastname == "" or birthday == "" or adress == "" or email == "" or phone == "" or department == "" or position == "":
            return render_template('dodaj.html', message='Molim vas popunite obavezna polja')
        try:
            data = Feedback(id, firstname, lastname, birthday, adress, email, phone, department, position)
            db.session.add(data)
            db.session.commit()
            return render_template('dodaj.html')
        except:
            cursor.execute("ROLLBACK")
            con.commit()
            return render_template('dodaj', message='Ovaj Radnik vec postoji u bazi')

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
