from flask import Flask, render_template
import sqlite3


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    