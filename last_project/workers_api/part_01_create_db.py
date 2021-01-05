import mysql.connector

# creating workers
conn = mysql.connector.connect(host="localhost", user="root", password="not-real-pass")
c = conn.cursor()
c.execute("create database if not exists final_project")
c.execute("use final_project")
c.execute("create table if not exists workers (employee_id integer auto_increment primary key, "
          "first_name varchar(100), last_name varchar(100), email varchar(100), phone_number varchar(20),"
          "hire_date date, job_id varchar(20), salary float, commission_pct float, manager_id integer,"
          "department_id integer)")
query_insert = "insert into workers (first_name, last_name, email, phone_number, hire_date, job_id, salary," \
               " commission_pct, manager_id, department_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
workers = [("Harry", "Potter", "Harry@Potter", "123456789", "1987-06-17", "CEO", 90000.50, 0.00, 0, None),
           ("James", "Potter", "James@Potter", "234235234", "1957-06-11", "HR", 20000.50, 0.00, 0, 90),
           ("Adrian ", "Pucey", "Adrian @Pucey", "123356789", "1777-06-22", "RD", 30000.50, 0.00, 0, 80),
           ("Severus", "Snape", "Severus@Snape", "123456789", "1999-08-11", "HR", 40000.50, 0.00, 0, 90),
           ("Lord", "Voldemort", "Harry@Voldemort", "644556789", "1987-08-18", "IT", 50000.50, 0.00, 0, 70),
           ("Fred", "Weasley", "Fred@Weasley", "323456788", "1987-09-14", "Sales", 60000.50, 0.00, 0, 60),
           ("George", "Weasley", "George@Weasley", "423456789", "1987-11-14", "HR", 10000.50, 0.00, 0, 90),
           ("Ginny", "Weasley", "Ginny@Weasley", "523456789", "1987-10-15", "RD", 10000.50, 0.00, 0, 80),
           ("Molly", "Weasley", "Molly@Weasley", "623456789", "1999-01-16", "Sales", 10000.50, 0.00, 0, 60),
           ("Percy", "Weasley", "Percy@Weasley", "723456789", "1988-02-17", "IT", 30000.50, 0.00, 0, 70),
           ("Oliver", "Wood", "Oliver@Wood", "823456789", "1989-03-17", "IT", 30000.50, 0.00, 0, 70),
           ("Hannah", "Abbott", "Harry@Abbott", "823858789", "2003-04-17", "HR", 30000.50, 0.00, 0, 90),
           ("Armando", "Dippet", "Armando@Dippet", "128888789", "2002-04-17", "RD", 40000.50, 0.00, 0, 80),
           ("Lucius", "Malfoy", "Harry@Malfoy", "129996789", "2020-05-17", "IT", 70000.50, 0.00, 0, 70)
           ]
c.executemany(query_insert, workers)
conn.commit()
conn.close()

# creating
