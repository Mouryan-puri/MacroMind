import pandas as pd
import sqlite3

# 1. Establish the database connection
conn = sqlite3.connect("meals.db")

# 2. Write your SQL query and load it directly into a DataFrame
# Replace 'your_table_name' with the actual table inside your .db file
df = pd.read_sql_query("SELECT * FROM meals", conn)

# 3. View the first few rows of the data
print(df['meal'])

# 4. Close the connection
conn.close()