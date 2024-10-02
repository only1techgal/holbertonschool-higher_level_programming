#!/usr/bin/python3

"""Script to add command-line arguments to a list and save to a JSON file."""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def main():
    """
    Main function to handle command-line arguments and save them
    to a JSON file.
    """

    filename = "add_item.json"

    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
