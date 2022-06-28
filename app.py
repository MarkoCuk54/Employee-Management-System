from turtle import position
from xmlrpc.client import boolean
from flask import Flask, request
from flask import render_template, request
from db_data import conn, db, Feedback, conn, cursor, app
from datetime import datetime, date
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/home")
def home():
    cur = conn.cursor()
    cur.execute("SELECT * FROM radnici")
    data = cur.fetchall()
    return render_template("home.html", data = data)

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

@app.route('/deleteUser', methods=["GET, POST"])
def deleteUser():
        id = request.form["id"]
        cur = conn.cursor()
        cur.execute("DELETE * FROM radnici where id = " + id)
        data = cur.fetchall()
        db.session.query(Feedback).filter(Feedback.id==id).delete()
        db.session.commit()
        return render_template("svi.html",  data = data)

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
            return render_template('editUser.html')
        except:
            return render_template('editUser.html')

@app.route('/changePosition', methods=["POST"])
def changePosition():
        novaPozicija = request.form["position"]
        try:
            user = db.session.query(Feedback).filter(Feedback.id == editUser.id).one()
            user.Position = novaPozicija
            izmjena = db.session.query(changePosition).filter(changePosition.id == editUser.id).one()
            izmjena.izmjena = novaPozicija
            db.session.commit()
            return render_template('editUser.html')
        except:
            return render_template('editUser.html')

@app.route("/dodaj")
def dodaj():
    cur = conn.cursor()
    cur.execute("SELECT * FROM radnici")
    data = cur.fetchall()
    return render_template("dodaj.html", data = data)

@app.route('/submit_noviRadnik', methods=['POST'])
def submitNoviRadnik():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        birthday = request.form['birthday']
        adress = request.form["adress"]
        email = request.form["email"]
        phone = request.form["phone"]
        department = request.form["department"]
        position = request.form["position"]
        if firstname == '' or lastname == "":
            return render_template('dodaj.html')
        try:
            data = Feedback(firstname, lastname, birthday, adress, email, phone, department, position)
            db.session.add(data)
            db.session.commit()
            return render_template('dodaj.html')
        except:
            cursor.execute("ROLLBACK")
            conn.commit()
            return render_template('dodaj.html')

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
