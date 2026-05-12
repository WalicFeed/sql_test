import sqlite3
from config import path_db
from db import queries


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.student_table)
    conn.commit()
    conn.close()


def insert_student(name, age):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_student, (name, age))
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    return student_id


def select_students():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.select_students)
    students = cursor.fetchall()
    conn.close()
    return students


def update_student(name, age, student_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.update_student, (name, age, student_id))
    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.delete_student, (student_id,))
    conn.commit()
    conn.close()