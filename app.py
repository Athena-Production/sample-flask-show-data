from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Function to connect to the database
def connect_db():
    db_connection = mysql.connector.connect(
        host="athena-do-user-16198044-0.c.db.ondigitalocean.com",
        user="doadmin",
        password="AVNS_G_K59rLh3HLpfthyzqU",
        database="defaultdb",
        port=25060
    )
    return db_connection


# Route to display data from the database
@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM scheduled_calls')
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)
'''
@app.route("/")
def hello_world():
    return render_template("index.html")
'''
