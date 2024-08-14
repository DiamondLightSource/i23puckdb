from flask import Flask, render_template
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)


app = Flask(__name__)

def getData():
    conn = sqlite3.connect('pucks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT puckid, person, date, location, remark FROM pucks")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    data = getData()
    return render_template('index.html', data=data)

@app.route('/healthz')
def healthCheck():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    