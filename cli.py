import argparse
from services.tracker import Tracker

def main_cli():
    parser = argparse.ArgumentParser(description="Personal Finance Tracker")
    parser.add_argument("command", choices=["add", "remove", "list", "report"], help="Command to execute")
    parser.add_argument("--amount", type=float, help="Transaction amount")
    parser.add_argument("--category", type=str, help="Transaction category")
    parser.add_argument("--type", type=str, choices=["income", "expense"], help="Transaction type")
    parser.add_argument("--id", type=int, help="Transaction ID to remove")
    args = parser.parse_args()

    tracker = Tracker()

    if args.command == "add":
        tracker.add_transaction(args.amount, args.category, args.type)
    elif args.command == "remove":
        tracker.remove_transaction(args.id)
    elif args.command == "list":
        tracker.list_transactions()
    elif args.command == "report":
        tracker.generate_report()