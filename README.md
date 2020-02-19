# TODO_list
overkill cli-based todo list using python and a database (postgres?)

### setup (for now)
`./configure` to setup a venv
next, I need to make this pull from requirements.txt

### top issues
* connecting to the db with `conn = psycopg2.connect("dbname=todo user=postgres")` makes a *lot* of assumptions.