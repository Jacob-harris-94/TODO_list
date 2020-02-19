import psycopg2


# https://www.psycopg.org/docs/
def init():
    # Connect to an existing database
    # Open a cursor to perform database operations
    # Execute a command: this creates a new table
    # cur.execute("CREATE TABLE todo.tag (id serial PRIMARY KEY, num integer, data varchar);")
    # cur.execute("CREATE TABLE todo.tag_ref (id serial PRIMARY KEY, num integer, data varchar);")
    # Make the changes to the database persistent
    # Close communication with the database
    conn = psycopg2.connect("dbname=todo user=postgres")
    cur = conn.cursor()
    cur.execute("DROP SCHEMA IF EXISTS todo CASCADE;")
    cur.execute("CREATE SCHEMA IF NOT EXISTS todo;")
    cur.execute("CREATE TABLE todo.item (id serial PRIMARY KEY, description text, time_created timestamp, time_due timestamp);")
    conn.commit()
    cur.close()
    conn.close()

def add_todo(todo_text="default text", due_date=None):
    conn = psycopg2.connect("dbname=todo user=postgres")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO todo.item (description, time_created, time_due) VALUES (%s, CURRENT_TIMESTAMP, %s);",
        (todo_text, due_date)
    )
    conn.commit()
    cur.close()
    conn.close()


def get_list():
    pass