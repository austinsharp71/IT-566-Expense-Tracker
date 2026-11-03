"""Implements the Expense Tracker Application."""
import sys


class Expenses:
    """A console-based Expense Tracker Application."""

    # Menu Choice Constants
    _ADD = '1'
    _SHOW = '2'
    _FILTER = '3'
    _SAVE = '4'
    _OPEN = '5'
    _EXPORT = '6'
    _EXIT = '7'

    def __init__(self):
        """Initialize Expenses object."""
        print('I am the Expense Tracker! I am alive!')

    def display_menu(self):
        """Print menu items to the console."""
        print('\n\t\tExpense Tracker Menu\n')
        print('\t1. Add Expense')
        print('\t2. Show All Expenses')
        print('\t3. Filter Expenses')
        print('\t4. Save Expenses To JSON File')
        print('\t5. Open JSON Expense File')
        print('\t6. Export Expenses To CSV File')
        print('\t7. Exit')

    def process_menu_choice(self):
        """Process menu commands."""
        menu_choice = input('\n\tEnter Command Number: ')
        print(f'\tYou entered: {menu_choice}')
        match menu_choice:
            case self._ADD: self.add_expense()
            case self._SHOW: self.print_expenses()
            case self._FILTER: self.filter_expenses()
            case self._SAVE: self.save_expenses()
            case self._OPEN: self.open_expenses()
            case self._EXPORT: self.export_expenses()
            case self._EXIT: sys.exit()
            case _: print(f'\tWARNING: {menu_choice} is an invalid command!')

    def start_application(self):
        """Display the menu and process commands until the user exits."""
        while True:
            self.display_menu()
            self.process_menu_choice()

    def add_expense(self):
        """Prompt the user for an expense and add it to the list."""
        print('\tadd_expense() method called...')

    def print_expenses(self):
        """Print a list of expenses to the console."""
        print('\tprint_expenses() method called...')

    def filter_expenses(self):
        """Filter expenses by date range and/or category and print them."""
        print('\tfilter_expenses() method called...')

    def save_expenses(self):
        """Save the expense list to a JSON file."""
        print('\tsave_expenses() method called...')

    def open_expenses(self):
        """Open a JSON file and replace the expense list with its contents."""
        print('\topen_expenses() method called...')

    def export_expenses(self):
        """Export the expense list to a CSV file."""
        print('\texport_expenses() method called...')
