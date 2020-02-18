import argparse

# see https://docs.python.org/3.8/howto/argparse.html#id1
# parser = argparse.ArgumentParser(description="manage a TODO list: add, view, sort, and more...")
# parser.add_argument("command", choices=["add", "list", "remove"], help="options for todo list items")
# parser.add_argument("description", type=str, help="text of the todo item to add")
# args = parser.parse_args()
#
# if args.command == "add":
#     print(f"adding todo item: \"{args.description}\"")
# else:
#     print(args.command)


# https://docs.python.org/3/library/argparse.html#sub-commands
# https://stackoverflow.com/questions/17073688/how-to-use-argparse-subparsers-correctly

# create the top-level parser
parser = argparse.ArgumentParser(prog='todo')
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(dest='subparser_name', help='sub-command help')
# create the parser for the "a" command
parser_a = subparsers.add_parser('list', help='list "top" todo items')
parser_a.add_argument('--num', type=int, help='num help', default=3)
# create the parser for the "b" command
parser_b = subparsers.add_parser('add', help='add new todo items')
parser_b.add_argument('description', type=str, help='description help')
args = parser.parse_args()

if args.subparser_name == 'list':
    print("list some stuff")
elif args.subparser_name == 'add':
    print(f"add some stuff: \"{args.description}\"")
else:
    print(args)