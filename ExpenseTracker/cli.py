import argparse
from models import Entry
from cli_commands import add_item, show_list

def main():
    parse = argparse.ArgumentParser(prog="ExpenseTracker")
    subparsers = parse.add_subparsers(dest="command")

    add_parser: argparse.ArgumentParser = subparsers.add_parser("add")
    add_parser.add_argument('-a', '--amount', type=float, required=True, help="price of the item")
    add_parser.add_argument('-c', '--category', required=True, nargs='+', help="item placed in that category")
    add_parser.add_argument('-n', '--note', nargs='+', help="Leave note for item. Not required.")

    list_parser: argparse.ArgumentParser = subparsers.add_parser("list",)
    list_parser.add_argument('-c', '--category', nargs='+', help="list items in a specific category")


    args: argparse.Namespace = parse.parse_args()

    if args.command == 'add':
        args.category = ' '.join(args.category)

        if args.note:
            args.note = ' '.join(args.note)
        else:
            args.note = ''

        entry = Entry(args.amount, args.category, args.note)
        add_item(entry)
        

    elif args.command == 'list':
        if args.category:
            args.category = ' '.join(args.category)
        else:
            args.category = ''

        show_list(args.category)

        

if __name__ == '__main__':
    main()