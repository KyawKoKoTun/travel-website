import sqlite3
import mysql.connector

# SQLite database information
sqlite_db_file = 'database.sqlite'

# MySQL database information
db_name = 'freedb_travel-website'
db_user = 'freedb_KyawKoKoTun'
db_password = '7u#YX?&b9%mzbhH'
db_host = 'sql.freedb.tech'
db_port = '3306'

try:
    # Connect to the SQLite database
    sqlite_conn = sqlite3.connect(sqlite_db_file)
    sqlite_cursor = sqlite_conn.cursor()

    # Connect to the MySQL database
    mysql_conn = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )
    mysql_cursor = mysql_conn.cursor()

    # Get a list of table names from the SQLite database
    sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = [row[0] for row in sqlite_cursor.fetchall()]

    # Loop through each table and copy data to MySQL database
    for table_name in table_names:
        # Fetch data from the SQLite table
        sqlite_cursor.execute(f"SELECT * FROM {table_name};")
        rows = sqlite_cursor.fetchall()

        # Create the corresponding table in the MySQL database (assuming table structure is the same)
        # You can create the table manually in the MySQL database with the same structure as in SQLite
        # or use Python to fetch the table schema from SQLite and create the same table in MySQL

        # Insert the data from the SQLite table into the corresponding table in the MySQL database
        # Assuming the table structure is the same, if not, modify the insert query accordingly
        
        for row in rows:
            insert_query = f"INSERT INTO {table_name} VALUES ({','.join(['%s']*len(row))})"
            mysql_cursor.execute(insert_query, row)

        # Commit the changes to the MySQL database for each table
        mysql_conn.commit()

    print("Database duplication successful!")

except Exception as e:
    print("Error:", str(e))

finally:
    # Close the database connections
    sqlite_cursor.close()
    sqlite_conn.close()
    mysql_cursor.close()
    mysql_conn.close()
