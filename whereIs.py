import sqlite3

conn = sqlite3.connect("pucks.db")
cur = conn.cursor()

findMe = input("Where is the puck ID? ")
found = cur.execute("SELECT location FROM pucks WHERE puckid=?", (findMe,))
found = found.fetchone()
print(f"Puck {findMe} is at/in {found[0]}")