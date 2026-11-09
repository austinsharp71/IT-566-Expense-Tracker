# Expense Tracker

A console program that lets you enter, filter, and print expenses. You can save expenses to a JSON file, open them again later, and export them to a CSV file that opens in Microsoft Excel.

## Files

- `src/main.py` - starts the program
- `src/expenses.py` - the `Expenses` class: the menu and the expense actions
- `src/file_handler.py` - saves and opens JSON files and exports CSV files

## Requirements

Python 3.10 or newer. 

## How to Run

From the project folder (the one that contains `src`), run:

```
python src/main.py
```

On Mac or Linux, use `python3` instead of `python`.

## How to Use

Type a number from the menu and press Enter.

| Choice | What it does |
|---|---|
| 1 | Add an expense: date, category, description, and amount |
| 2 | Show all expenses |
| 3 | Filter expenses by start date, end date, and/or category. Press Enter to skip a filter. |
| 4 | Save expenses to a JSON file |
| 5 | Open a JSON file of expenses |
| 6 | Export expenses to a CSV file for Excel |
| 7 | Exit |

- Type dates as YYYY-MM-DD, for example `2026-01-09`.
- Type amounts as plain numbers, for example `12.50`.
- Type the whole file name, including `.json` or `.csv`.
- Files go in a `data` folder inside the folder you run the program from. The program creates it the first time you save, open, or export.
