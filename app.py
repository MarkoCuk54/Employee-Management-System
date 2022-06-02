from flask import Flask
from flask import render_template
from db_data import conn

app = Flask(__name__)

@app.route("/")
def login():
    cur = conn.cursor()
    cur.execute('SELECT * FROM admin;')
    admin = cur.fetchall()
    print(admin)
    cur.close()
    return render_template('login.html')




# auto restart server on change
app.run(debug=True)
