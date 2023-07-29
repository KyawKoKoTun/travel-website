import sqlite3

def copy_data(source_db, destination_db):
    # Connect to the source database
    source_conn = sqlite3.connect(source_db)
    source_cursor = source_conn.cursor()

    # Connect to the destination database
    destination_conn = sqlite3.connect(destination_db)
    destination_cursor = destination_conn.cursor()

    try:
        # Fetch all tables from the source database
        source_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = source_cursor.fetchall()

        for table in tables:
            table_name = table[0]

            # Fetch all data from each table in the source database
            source_cursor.execute(f"SELECT * FROM {table_name};")
            rows = source_cursor.fetchall()

            # Get the column names for the CREATE TABLE statement
            source_cursor.execute(f"PRAGMA table_info({table_name});")
            columns = source_cursor.fetchall()
            column_names = ', '.join(column[1] for column in columns)

            # Create the same table in the destination database
            destination_cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({column_names});")

            # Insert data into the destination table
            for row in rows:
                placeholders = ', '.join(['?' for _ in row])
                destination_cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders});", row)

        # Commit changes and close the connections
        destination_conn.commit()
        destination_conn.close()
        source_conn.close()

        print("Data copied successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    source_db = "database.db"
    destination_db = "database.sqlite"

    copy_data(source_db, destination_db)
