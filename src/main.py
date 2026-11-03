"""Serves as the point of entry to the Expense Tracker Application."""

from expenses import Expenses


def main():
    """Create the Expense Tracker Application and process one command."""
    tracker = Expenses()
    tracker.display_menu()
    tracker.process_menu_choice()


if __name__ == '__main__':
    main()
