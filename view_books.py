from database import conn, cursor

query = "SELECT * FROM books"

cursor.execute(query)

books = cursor.fetchall()

print("\n===== BOOK LIST =====\n")

for book in books:
    print(f"ID       : {book[0]}")
    print(f"Title    : {book[1]}")
    print(f"Author   : {book[2]}")
    print(f"Quantity : {book[4]}")
    print("-------------------------")

cursor.close()
conn.close()