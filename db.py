import sqlite3

conn = sqlite3.connect('Stuents.db')
c = conn.cursor()


class Db_manager:
    def create():
        c.execute('''CREATE TABLE Advisor (
                        advisor_id INTEGER PRIMARY KEY,
                        name TEXT
                     )''')

        c.execute('''CREATE TABLE Student (
                        student_id INTEGER PRIMARY KEY,
                        name TEXT
                     )''')

        c.execute('''CREATE TABLE Advisor_Student (
                        advisor_id INTEGER,
                        student_id INTEGER,
                        PRIMARY KEY (advisor_id, student_id),
                        FOREIGN KEY (advisor_id) REFERENCES Advisor(advisor_id),
                        FOREIGN KEY (student_id) REFERENCES Student(student_id)
                     )''')

        conn.commit()


    def insert_data():
        advisor_names = ['adv_kaxa', 'adv_luiza', 'adv_klara', 'adv_kiki', 'adv_zezva']
        student_names = ['st_mzia', 'st_mzago', 'st_lamzira', 'st_zenaida', 'st_zoraide',
                         'st_mariami', 'st_nia', 'st_tsira', 'st_koko', 'st_tornike', 'st_irakli']
        for name in advisor_names:
            c.execute("INSERT INTO Advisor (name) VALUES (?)", (name,))

        for name in student_names:
            c.execute("INSERT INTO Student (name) VALUES (?)", (name,))

        c.execute(f"INSERT INTO Advisor_Student (advisor_id, student_id) VALUES (1, 1)")
        c.execute(f"INSERT INTO Advisor_Student (advisor_id, student_id) VALUES (1, 2)")
        c.execute(f"INSERT INTO Advisor_Student (advisor_id, student_id) VALUES (1, 3)")
        c.execute(f"INSERT INTO Advisor_Student (advisor_id, student_id) VALUES (2, 1)")
        c.execute(f"INSERT INTO Advisor_Student (advisor_id, student_id) VALUES (2, 4)")
        c.execute(f"INSERT INTO Advisor_Student (advisor_id, student_id) VALUES (2, 8)")
        c.execute(f"INSERT INTO Advisor_Student (advisor_id, student_id) VALUES (3, 8)")
        c.execute(f"INSERT INTO Advisor_Student (advisor_id, student_id) VALUES (3, 5)")
        c.execute(f"INSERT INTO Advisor_Student (advisor_id, student_id) VALUES (4, 8)")
        c.execute(f"INSERT INTO Advisor_Student (advisor_id, student_id) VALUES (4, 1)")
        c.execute(f"INSERT INTO Advisor_Student (advisor_id, student_id) VALUES (4, 3)")
        c.execute(f"INSERT INTO Advisor_Student (advisor_id, student_id) VALUES (4, 11)")
        c.execute(f"INSERT INTO Advisor_Student (advisor_id, student_id) VALUES (4, 2)")

        conn.commit()


    def read_data():
        c.execute("SELECT Advisor.name, COUNT(Advisor_Student.student_id) AS student_count FROM Advisor "
                  "LEFT JOIN Advisor_Student ON Advisor.advisor_id = Advisor_Student.advisor_id "
                  "GROUP BY Advisor.advisor_id")
        # c.execute("SELECT * from Advisor")
        for item in c.fetchall():
            print(item)


create_table()
insert_data()
read_data()

conn.close()
