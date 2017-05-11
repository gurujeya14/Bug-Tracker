import sqlite3

#Open database
conn = sqlite3.connect('bugTracker_sample.db')
print "Opened database successfully";

#Create Required Tables
conn.execute('CREATE TABLE users (id TEXT NOT NULL UNIQUE PRIMARY KEY, uname TEXT, paswd TEXT)')
conn.execute('CREATE TABLE bugs (pdtNm TEXT, pdtVer TEXT, bug TEXT NOT NULL UNIQUE PRIMARY KEY, des TEXT, severe TEXT, status TEXT, date TEXT, chgUser TEXT)')
print "Tables created successfully";
conn.close()
