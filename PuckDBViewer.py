from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_httpauth import HTTPBasicAuth
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
auth = HTTPBasicAuth()

DATABASE = '/dls/science/groups/i23/PuckDB/pyqr_i23/pucks.db'
users = {"i23user": "!23u5er#"}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    return None


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
@auth.login_required
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pucks')
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)


@app.route('/delete/<string:puckid>', methods=['POST'])
@auth.login_required
def delete_record(puckid):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM pucks WHERE puckid = ?', (puckid,))
    conn.commit()
    conn.close()
    
    return jsonify({"success": True})

@app.route('/record/<string:puckid>', methods=['GET'])
def get_record(puckid):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pucks WHERE puckid = ?', (puckid,))
    record = cursor.fetchone()
    conn.close()
    return jsonify(dict(record)) if record else jsonify({})

# @app.route('/create', methods=['POST'])
# def create_entry():
#     puckid = request.form['puckid']
#     person = request.form['person']
#     date = request.form['date']
#     location = request.form['location']
#     remark = request.form.get('remark', '')  # remark is optional
    
#     conn = sqlite3.connect('pucks.db')
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO pucks (puckid, person, date, location, remark) VALUES (?, ?, ?, ?, ?)", 
#                    (puckid, person, date, location, remark))
#     conn.commit()
#     conn.close()

#     return redirect('/')

@app.route('/create', methods=['POST'])
def create_record():
    puckid = request.form.get('puckid')
    person = request.form.get('person')
    date = request.form.get('date')
    location = request.form.get('location')
    remark = request.form.get('remark')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO pucks (puckid, person, date, location, remark) VALUES (?, ?, ?, ?, ?)',
                   (puckid, person, date, location, remark))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/healthz')
def healthz():
    return jsonify(status="ok"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    