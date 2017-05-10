import sqlite3

#Open database
conn = sqlite3.connect('bugTracker_sample.db')
print "Opened database successfully";

#Create Required Tables
conn.execute('CREATE TABLE users (id TEXT NOT NULL UNIQUE PRIMARY KEY, uname TEXT, paswd TEXT)')
print "Table created successfully";
conn.close()
