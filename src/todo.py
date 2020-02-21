#!/usr/bin/env python

from cli.cli import parse
from dbinterface.interface import init, add_todo, get_list


def pretty_print(todo_items):
    DISPLAY_WIDTH = 78
    print("")
    print(f"TODO ITEMS: top {len(todo_items)}")
    print("-"*DISPLAY_WIDTH)
    for result in todo_items:
        tab_separated = '\t'.join([str(item) for item in result])
        print(tab_separated)
    print("-" * DISPLAY_WIDTH)


def main():
    args = parse()
    if args.subparser_name == 'list':
        if args.num:
            list_results = get_list()
        else:
            list_results = get_list(args.num)
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