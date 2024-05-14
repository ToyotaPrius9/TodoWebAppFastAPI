import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('todotodo.db')
cursor = conn.cursor()

# Function to display all tables in the database
def list_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])

# Function to display the contents of a specific table
def display_table(table_name):
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    
    print(f"\nContents of table '{table_name}':")
    print(" | ".join(column_names))
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    for row in rows:
        print(" | ".join(map(str, row)))

# List all tables
list_tables()

# Display contents of the 'tasks' table (you can change the table name if needed)
display_table('tasks')

# Close the connection
conn.close()
