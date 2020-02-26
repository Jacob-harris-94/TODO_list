from contextlib import contextmanager
import psycopg2


# https://book.pythontips.com/en/latest/context_managers.html
@contextmanager
def cur_conn(connect_data):
    conn = psycopg2.connect("dbname=todo user=postgres")
    cur = conn.cursor()
    yield cur
    conn.commit()
    cur.close()
    conn.close()


# https://www.psycopg.org/docs/
def init():
    with cur_conn("dbname=todo user=postgres") as cur:
        cur.execute("DROP SCHEMA IF EXISTS todo CASCADE;")
        cur.execute("CREATE SCHEMA IF NOT EXISTS todo;")
        cur.execute("CREATE TABLE todo.item (id serial PRIMARY KEY, description text, time_created timestamp, time_due timestamp);")


def add_todo(todo_text="default text", due_date=None):
    with cur_conn("dbname=todo user=postgres") as cur:
        cur.execute(
            "INSERT INTO todo.item (description, time_created, time_due) VALUES (%s, CURRENT_TIMESTAMP, %s);",
            (todo_text, due_date)
        )


def get_list(num_items_to_get=3, sort_by_date_created=None, sort_by_date_due=None):
    print(f"trying to get {num_items_to_get} items...")
    with cur_conn("dbname=todo user=postgres") as cur:
        cur.execute("SELECT id, time_created::date, time_due::date, description FROM todo.item LIMIT %s;", (num_items_to_get,))
        results =  cur.fetchall()
    return results