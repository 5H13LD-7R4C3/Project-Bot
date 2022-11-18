# Intial setup of databases

import sqlite3

# Connect to database
def createDatabase():
  conn=sqlite3.connect(r'C:\Users\clark\Desktop\Github\Project-Bot\Project-Bot\database.db') # delete for system location

# Create a cursor
  c= conn.cursor()

# Create a table for bots
  c.execute("""CREATE TABLE bots(
    id int AUTO INCREMENT,
    bot_ip text

  )""")

# Commit Command
  conn.commit()

# Create a table for entry relay
  c.execute("""CREATE TABLE relay(
    id int AUTO INCREMENT,
  
    relay_ip text

  )""")

# Commit Command
  conn.commit()

# Create a table
  c.execute("""CREATE TABLE targets(
    id int AUTO INCREMENT,
    target_name text,
    target_ip text
    vuln_rating int

  )""")

# Commit Command
  conn.commit()

# Close connection
  conn.close()

#createDatabase()