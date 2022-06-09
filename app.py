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
        if(bolean != [] and password == bolean[0][2]):
            cur.close()
            return render_template('home.html', data = bolean[0][1])
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

@app.route('/editUser', methods=["GET", "POST"])
def editUser():
        editUser.id = request.form["idEdit"]
        if(id != ""):
            try:
                cursor.execute("SELECT * FROM svi where  id = " + str(editUser.id))
                result = cursor.fetchall()
                return render_template('editUser.html', data=result[0])
            except:
                cursor.execute("ROLLBACK")
                con.commit()
                message = "ID ne postoji u Bazi"
                return render_template('error.html', message=message)
        else:
            cursor.execute("ROLLBACK")
            con.commit()
            message = "Id polje ne smije biti prazno"
            return render_template('error.html', message=message)

# auto restart server on change
app.run(debug=True)
