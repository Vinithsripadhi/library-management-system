import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="library_db"
)

cursor = conn.cursor()

if conn.is_connected():
    print("✅ Connected to MySQL Successfully!")