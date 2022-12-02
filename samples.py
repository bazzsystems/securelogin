import sqlite3
import hashlib

conn = sqlite3.connect('userdata.db')

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")
username1, password1 = "john31231", hashlib.sha256("Johnisadush31".encode()).hexdigest()
username2, password2 = "jane39", hashlib.sha256("Aotveryhuman48@".encode()).hexdigest()
username3, password3 = "yossihagever69", hashlib.sha256("WarMachine69!".encode()).hexdigest()
username4, password4 = "ashermalkno99", hashlib.sha256("BietarJ4e".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))
conn.commit()