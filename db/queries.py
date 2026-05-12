tasks_table = """
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
"""

insert_student = """
    INSERT INTO student (name, age) VALUES (?, ?)
"""

select_students = """
    SELECT * from student
"""

update_student = """
    UPDATE student SET name = ?, age = ? WHERE id = ?
"""

delete_student = """
    DELETE FROM student WHERE id = ?
""" 