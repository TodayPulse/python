import sqlite3

titles = [
    (1, "The Hunger Games"),
    (2, "The Great Gatsby"),
    (3, "The Maze Runner"),
    (4, "The Lord of the Rings")
]

with sqlite3.connect("books.db") as connection:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE if NOT EXISTS books (
        id  INTEGER,
        title TEXT)
    """)

    for id, title in titles:
        cursor.execute("INSERT INTO books VALUES (?,?)", (id, title))