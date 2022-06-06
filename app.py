from email import message
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
    try:
        username =  request.form['username'] 
        password = request.form['password']
        cur = conn.cursor()
        bolean = cur.execute("SELECT * FROM admin where id = " + username)
        bolean = cur.fetchall()
        if(bolean != []):
            print(bolean)
            cur.close()
            return render_template('home.html', data = bolean[0][1])
        else:
            message = "Error"
            return render_template("login.html",  data = message)
    except:
        message = "Error"
        return render_template("login.html",data =  message)


@app.route("/svi")
def sviRadnici():
    return render_template("svi.html")

# auto restart server on change
app.run(debug=True)
