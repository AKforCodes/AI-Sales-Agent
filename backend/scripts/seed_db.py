import os
import psycopg2
from dotenv import load_dotenv

# This script needs to be run from the root of the `backend` directory
# to correctly locate the .env and sql files.
load_dotenv()

def execute_sql_file(filepath):
    """Executes the SQL commands from a given file."""
    conn = None
    try:
        conn = psycopg2.connect(os.environ['DATABASE_URL'])
        cur = conn.cursor()
        with open(filepath, 'r') as f:
            sql_script = f.read()
            cur.execute(sql_script)
        conn.commit()
        cur.close()
        print(f"Successfully executed {filepath}")
    except Exception as e:
        print(f"Error executing {filepath}: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Define paths relative to the script's expected location
    # Assumes running from 'backend/' directory
    schema_path = os.path.join('sql', 'schema.sql')
    data_path = os.path.join('sql', 'data.sql')

    print("Seeding database...")
    execute_sql_file(schema_path)
    execute_sql_file(data_path)
    print("Database seeding complete.")
