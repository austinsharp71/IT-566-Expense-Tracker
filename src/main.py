"""Serves as the point of entry to the Expense Tracker Application."""

from expenses import Expenses


def main():
    """Create the Expense Tracker Application and display its menu."""
    tracker = Expenses()
    tracker.display_menu()


if __name__ == '__main__':
    main()
