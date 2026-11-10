import sqlite3

DB_NAME = "grades.db"


def connect(path=DB_NAME):
    conn = sqlite3.connect(path)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            mathematics REAL NOT NULL,
            english REAL NOT NULL,
            science REAL NOT NULL,
            average REAL NOT NULL,
            grade TEXT NOT NULL)"""
    )
    return conn


def add_student(conn, name, marks, avg, grade):
    conn.execute(
        """INSERT INTO students
           (name, mathematics, english, science, average, grade)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (name, *marks, avg, grade),
    )
    conn.commit()


def get_students(conn):
    return conn.execute(
        """SELECT name, mathematics, english, science, average, grade
           FROM students ORDER BY id"""
    ).fetchall()
