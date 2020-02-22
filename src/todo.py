#!/usr/bin/env python

from cli.cli import parse
from dbinterface.interface import init, add_todo, get_list
from tabulate import tabulate

def pretty_print(todo_items):
    DISPLAY_WIDTH = 78
    print("")
    print(f"TODO ITEMS: top {len(todo_items)}")

    # print("-"*DISPLAY_WIDTH)
    # for result in todo_items:
    #     tab_separated = '\t'.join([str(item) for item in result])
    #     print(tab_separated)
    # print("-" * DISPLAY_WIDTH)

    table = []
    TODO_COL_WIDTH = 40
    for item in todo_items:
        id, created, due, list_item = item
        list_item = list_item[:TODO_COL_WIDTH]+" [...]" if len(list_item) > TODO_COL_WIDTH else list_item
        table.append([id, created, due, list_item])
    print(tabulate(table, headers=["id", "created", "due", "list item"], tablefmt='psql'))

def main():
    args = parse()
    if args.subparser_name == 'list':
        list_results = get_list(num_items_to_get=args.num)
        pretty_print(list_results)
    elif args.subparser_name == 'add':
        if args.due:
            add_todo(args.description, args.due)
        else:
            add_todo(args.description)
    elif args.subparser_name == 'init':
        print("init! this is SUPER DESTRUCTIVE right now, update later...")
        wipe_test = input("are you 1000000% sure you want to wipe everything? \nif so, type 'yes, wipe it'\n")
        if wipe_test == "yes, wipe it":
            init()
            print("wiped!")
        else:
            print("not today!")
    else:
        print(args)

if __name__ == "__main__":
    main()