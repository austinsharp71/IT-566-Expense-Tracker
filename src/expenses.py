"""Implements the Expense Tracker Application."""


class Expenses:
    """A console-based Expense Tracker Application."""

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
        # Prompt user for input
        # Assign input string to variable
        menu_choice = input('\n\tEnter Command Number: ')
        print(f'\tYou entered: {menu_choice}')
        # Is menu_choice a valid command?
        # YES - Execute command
        # NO - Display error message and try again
