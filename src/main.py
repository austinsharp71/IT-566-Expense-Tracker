"""Serves as the point of entry to the Expense Tracker Application."""

from expenses import Expenses


def main():
    """Create and start the Expense Tracker Application."""
    tracker = Expenses()
    tracker.start_application()


if __name__ == '__main__':
    main()
