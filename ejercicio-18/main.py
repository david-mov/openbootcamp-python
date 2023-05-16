import sqlite3

class Students:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.__create_table()

    def __create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50)
        );'''
        self.cursor.execute(query)

    def insert_one(self, first_name, last_name):
        query = '''INSERT INTO students(first_name, last_name) VALUES (?, ?)'''
        self.cursor.execute(query, (first_name, last_name))
        self.conn.commit()

    def insert_many(self, students):
        query = '''INSERT INTO students(first_name, last_name) VALUES (?, ?)'''
        self.cursor.executemany(query, students)
        self.conn.commit()

    def find_by_name(self, name):
        rows = self.cursor.execute(f"SELECT * FROM students WHERE first_name='{name}'")
        return rows.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()

def main():
    db = Students('./students.db')

    db.insert_one('david', 'mov')
    print('find_by_name("david"): \n', db.find_by_name('david'))

    db.insert_many([
        ('elon', 'musk'),
        ('bill', 'gates'),
        ('jeff', 'bezos'),
        ('warren', 'buffett'),
        ('mark', 'zuckerberg'),
        ('larry', 'page'),
        ('larry', 'ellison')
    ])

    print('db.find_by_name("larry"): \n', db.find_by_name('larry'))

    db.close()

if __name__ == '__main__':
    main()