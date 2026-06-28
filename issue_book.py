from database import conn, cursor

book_id = int(input("Enter Book ID to Issue: "))

query = "UPDATE books SET quantity = quantity - 1 WHERE book_id = %s"

cursor.execute(query, (book_id,))
conn.commit()

print("✅ Book Issued Successfully!")

cursor.close()
conn.close()