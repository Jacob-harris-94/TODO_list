import argparse

# https://docs.python.org/3/library/argparse.html#sub-commands
# https://stackoverflow.com/questions/17073688/how-to-use-argparse-subparsers-correctly

def parse():
    # create the top-level parser
    parser = argparse.ArgumentParser(prog='todo')
    parser.add_argument('--foo', action='store_true', help='foo help')
    subparsers = parser.add_subparsers(dest='subparser_name', help='sub-command help')
    # create the parser for the "list" command
    parser_list = subparsers.add_parser('list', help='list "top" todo items')
    parser_list.add_argument('--num', type=int, help='num help', default=3)
    # create the parser for the "add" command
    parser_add = subparsers.add_parser('add', help='add new todo items')
    parser_add.add_argument('description', type=str, help='description help')
    parser_add.add_argument('--due', type=str, help='date-time in any reasonable format?')
    # create the parser for the "init" command
    parser_add = subparsers.add_parser('init', help='initialize the todo list')
    args = parser.parse_args()
    return args