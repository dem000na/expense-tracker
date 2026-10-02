import argparse
import datetime
import logging
from pathlib import Path
from ExpenseTracker.models import Entry
from ExpenseTracker.commands import add_item, show_list, show_month_report

LOG_DIR: Path = Path(__file__).resolve().parent.parent / 'logging' / 'logs.log'

def main():
    LOG_DIR.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.DEBUG, filename=LOG_DIR, filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('cli')


    parse = argparse.ArgumentParser(prog="ExpenseTracker")
    subparsers = parse.add_subparsers(dest="command")

    add_parser: argparse.ArgumentParser = subparsers.add_parser("add")
    add_parser.add_argument('-a', '--amount', type=float, required=True, help="price of the item")
    add_parser.add_argument('-c', '--category', required=True, nargs='+', help="item placed in that category")
    add_parser.add_argument('-n', '--note', nargs='+', help="Leave note for item. Not required.")

    list_parser: argparse.ArgumentParser = subparsers.add_parser("list",)
    list_parser.add_argument('-c', '--category', nargs='+', help="list items in a specific category")
    list_parser.add_argument('-d', '--date', type=datetime.date.fromisoformat, help='only show entries in this format YYYY-MM-DD')

    report_parser: argparse.ArgumentParser = subparsers.add_parser("report")
    report_parser.add_argument('-m', '--month', type=lambda m: datetime.datetime.strptime(m, '%Y-%m').date(), help='only show entries in this format YYYY-MM')

    args: argparse.Namespace = parse.parse_args()
    logger.info('Running command %s with args %s', args.command, args)

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

        show_list(args.category, args.date)


    elif args.command == 'report':
        if not args.month:
            args.month = None
            
        show_month_report(args.month)

if __name__ == '__main__':
    main()