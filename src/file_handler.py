"""Saves, opens, and exports expense files."""
import json
import os


def get_file_path(filename):
    """Return the path to filename inside the data directory."""
    working_dir = os.getcwd()
    data_dir = 'data'
    data_dir_path = os.path.join(working_dir, data_dir)
