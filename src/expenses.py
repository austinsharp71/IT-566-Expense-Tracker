"""Implements the Expense Tracker Application."""
import sys

import file_handler


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
        """Initialize Expenses object with an empty expense list."""
        self._expense_list = []

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
            case self._SHOW: self.print_expenses(self._expense_list)
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
        expense = {}
        expense['date'] = input('\tDate (YYYY-MM-DD): ')
        expense['category'] = input('\tCategory: ')
        expense['description'] = input('\tDescription: ')
        expense['amount'] = float(input('\tAmount: '))
        self._expense_list.append(expense)
        print('\tExpense added.')

    def print_expenses(self, expense_list):
        """Print a list of expenses to the console."""
        for expense in expense_list:
            print(f'\t{expense}')

    def filter_expenses(self):
        """Filter expenses by date range and/or category and print them."""
        print('\tPress Enter to skip a filter.')
        start_date = input('\tStart Date (YYYY-MM-DD): ')
        end_date = input('\tEnd Date (YYYY-MM-DD): ')
        category = input('\tCategory: ')

        # Dates in YYYY-MM-DD format can be compared as strings
        filtered_list = []
        for expense in self._expense_list:
            keep = True
            if start_date != '' and expense['date'] < start_date:
                keep = False
            if end_date != '' and expense['date'] > end_date:
                keep = False
            if category != '' and expense['category'] != category:
                keep = False
            if keep:
                filtered_list.append(expense)

        self.print_expenses(filtered_list)

    def save_expenses(self):
        """Save the expense list to a JSON file."""
        filename = input('\tJSON File Name: ')
        file_handler.save_json(filename, self._expense_list)

    def open_expenses(self):
        """Open a JSON file and replace the expense list with its contents."""
        print('\topen_expenses() method called...')

    def export_expenses(self):
        """Export the expense list to a CSV file."""
        print('\texport_expenses() method called...')
