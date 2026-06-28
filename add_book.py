from database import conn, cursor

title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
quantity = int(input("Enter Quantity: "))

query = "INSERT INTO books(title, author, quantity) VALUES(%s, %s, %s)"

values = (title, author, quantity)

cursor.execute(query, values)

conn.commit()

print("✅ Book Added Successfully!")

cursor.close()
conn.close()