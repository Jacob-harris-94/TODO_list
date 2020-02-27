# TODO_list
overkill cli-based todo list using python and a database (postgres?)

### setup (for now)

* install postgres
* clone the project
* run `./configure` to setup a venv
* run `./temp_init_script` to create a new database (only need to do once)

### run

* run `./todo --help` for help

### top issues
* connecting to the db with `conn = psycopg2.connect("dbname=todo user=postgres")` makes a *lot* of assumptions.
* prevent SQL injection