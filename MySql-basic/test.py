from datetime import datetime

import mysql.connector

# Create a connection to a database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase"
)
mycursor = db.cursor()

# Use the below command at first to create the database.
# After that, used reference the database as a connection parameter
# mycursor.execute("CREATE DATABASE testdatabase")

# Create first table, called Person
# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# Visualize the table Person
mycursor.execute("DESCRIBE Person")

for x in mycursor:
    print(x)

# Insert first record - commit it one and after that comment it out
# mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Tim", 19))
# db.commit()

# Check what is in the table
mycursor.execute("SELECT * FROM Person")
for x in mycursor:
    print(x)

# Create table Test
# mycursor.execute("CREATE TABLE Test (name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM('M','F','O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")

# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ("Rado", datetime.now(), 'M'))
# db.commit()

# mycursor.execute("DROP TABLE Test")
# db.commit()

# mycursor.execute("SELECT * FROM Test WHERE gender = 'M' ORDER BY id DESC")
# mycursor.execute("SELECT id FROM Test WHERE gender = 'M' ORDER BY id DESC")
# mycursor.execute("SELECT id, name FROM Test WHERE gender = 'M' ORDER BY id DESC")

for x in mycursor:
    print(x)

# mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")

# mycursor.execute("ALTER TABLE Test DROP food")
# mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")

mycursor.execute("DESCRIBE Test")
for x in mycursor:
    print(x)

users = [("tim", "timoto"),
         ("peter", "peteroto"),
         ("john", "johnoto")]

user_scores = [(44, 100),
               (45, 101),
               (46, 102)]

mycursor = db.cursor()

Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"

Q2 = "CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"

Q3 = "DROP TABLE Users"
mycursor.execute(Q1)
mycursor.execute(Q2)

mycursor.execute("SHOW TABLES")

Q3 = "INSERT INTO Users (name, passwd) VALUES (%s, %s)"
Q4 = "INSERT INTO Scores (userId, game1, game2) VALUES (%s, %s, %s)"

for x, user in enumerate(users):
    mycursor.execute(Q3, user)
    last_id = mycursor.lastrowid
    mycursor.execute(Q4, (last_id,) + user_scores[x])
db.commit()

mycursor.execute("SELECT * FROM Users")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM Scores")
for x in mycursor:
    print(x)



