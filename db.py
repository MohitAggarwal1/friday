import csv
import sqlite3

con =  sqlite3.connect('friday.db')
cur = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id  INTEGER PRIMARY KEY, name VARCHAR(100), path VARCHAR(1000))"
# cur.execute(query)

# desired_columns_indices = [0, 18]

# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cur.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()

# query = "INSERT INTO contacts VALUES (null,'Mohit', '8376825101', 'null')"
# cur.execute(query)
# con.commit()
