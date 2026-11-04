"""Saves, opens, and exports expense files."""
import json
import os


def get_file_path(filename):
    """Return the path to filename inside the data directory."""
    working_dir = os.getcwd()
    data_dir = 'data'
    data_dir_path = os.path.join(working_dir, data_dir)

    # Create data directory if it does not exist
    if not os.path.exists(data_dir_path):
        os.makedirs(data_dir_path)

    return os.path.join(data_dir_path, filename)


def save_json(filename, expense_list):
    """Convert the expense list to JSON and write it to a file."""
    try:
        json_string = json.dumps(expense_list)
        with open(get_file_path(filename), 'w') as f:
            f.write(json_string)
        print(f'\tSaved {filename}')
    except (OSError, Exception) as e:
        print(f'\tProblem saving file: {e}')
