#!/usr/bin/env python

from cli.cli import parse
from dbinterface.interface import init, add_todo

def main():
    args = parse()
    if args.subparser_name == 'list':
        print("list some stuff")
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