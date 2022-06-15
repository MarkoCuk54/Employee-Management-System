from turtle import position
from flask import Flask, request
from flask import render_template
from db_data import conn

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def loginSuccs():
    try:
        username =  request.form['username'] 
        password = request.form['password']
        cur = conn.cursor()
        bolean = cur.execute("SELECT * FROM admin where id = " + username)
        bolean = cur.fetchall()
        print(bolean)
        if(bolean != [] and password == bolean[0][2]):
            cur.close()
            return render_template('home.html', data = bolean)
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

@app.route("/dodaj")
def dodaj():
    return render_template("dodaj.html")

@app.route("/događaji")
def događaji():
    return render_template("događaji.html")

@app.route("/obrasci")
def obrasci():
    return render_template("obrasci.html")
# auto restart server on change

@app.route("/editUser")
def editUser():
    return render_template("editUser.html")


@app.route("/unesi", methods=["POST"])
def unesi():
        firstname =  request.form['firstname'] 
        lastname = request.form['lastname']
        birthday =  request.form['birthday'] 
        adress =  request.form['adress'] 
        email = request.form['email']
        phone =  request.form['phone'] 
        department = request.form['department']
        position = request.form['position']
        print(firstname, lastname,birthday,adress,email,phone,department,position)

app.run(debug=True)
