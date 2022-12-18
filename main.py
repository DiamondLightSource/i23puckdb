import sqlite3
import datetime

conn = sqlite3.connect("pucks.db")
cur = conn.cursor()
try:
    cur.execute("CREATE TABLE pucks(puckid type UNIQUE, person, date, location)")
except:
    pass

def getInfo():
    puckid = input("Scan puck QR or type ID (XYZ-123): ").upper
    person = input("Who are you? ").upper
    today = datetime.date.today()
    date = str(today.strftime("%d_%m_%Y"))
    location = input("Scan in to I23 using QR or input send location: ").upper
    data = (puckid, person, date, location)
    if (len(puckid) < 3) or (len(person) < 1) or (len(date) < 1) or (len(location) < 1):
        return None
    else:
        return data

def sqInsert(data):
    if data == None:
        print("Data not valid. Check input again...")
    else:
        cur.execute("INSERT OR REPLACE INTO pucks VALUES(?, ?, ?, ?)", data)
        conn.commit()

def sqQuery():
    for res in cur.execute("SELECT puckid, person, date, location FROM pucks"):
        print(res)

if __name__ == "__main__":
    while True:
        puckData = getInfo()
        sqInsert(data=puckData)
    sqQuery()
