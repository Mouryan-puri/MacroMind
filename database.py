# why Sqlite?
# SQLite is just a database that lives in a single file on your computer — meals.db in your case. No server to set up, no configuration, nothing to install. Python has it built in. It's what CS50 used, you've already seen it.


import sqlite3
from datetime import datetime, date

def init_db():
    # first of all, make a connection to a database file if present, otherwise sqlite creates one  
    connection=sqlite3.connect("meals.db")

    # A cursor is an object that allows interaction with the database by executing SQL commands and fetching query results. It acts as a bridge between Python and SQLite, helping manage query execution, data retrieval, and transaction control.
    curr=connection.cursor()

    # creating a table with 4 columns
    # .execute() method is used to run sql commands 
    curr.execute(
        """
        CREATE TABLE IF NOT EXISTS meals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        meal_type TEXT NOT NULL,
        meal_name TEXT NOT NULL,
        meal_description TEXT NOT NULL,
        calories INTEGER NOT NULL,
        protein INTEGER NOT NULL,
        carbs INTEGER NOT NULL,
        fat INTEGER NOT NULL,
        date DATE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
        """
    )
    # sqlite commit the changes
    connection.commit()

    # once done, we have to close the connection to avoid any errors or data mismanagement
    connection.close()

def save_meal(meal, meal_type, response, today):
    connection=sqlite3.connect("meals.db")
    curr=connection.cursor()

    # basically, insert a row into table named meals, where columns where data will go are meal, response.
    # (?,?) are placeholders. They act as temporary slots for your actual data, telling the database to expect two inputs.
    # last (meal, response) are actual python tuple containing data that will go in table
    curr.execute("INSERT INTO meals (meal_type, meal_name, meal_description, calories, protein, carbs, fat, date) VALUES (?,?,?,?,?,?,?,?)", (meal_type, meal, response['meal_name'], response['calories'], response['protein'], response['carbs'], response['fat'],today))
    connection.commit() # to commit the actual changes 
    connection.close() # to close the connection bw sqlite and python