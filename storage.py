"""
storage.py
----------
Handles persistent data storage and retrieval for student records.

Provides functions to save to and load from a JSON file. Converts between
student objects and dictionary representations.

Part of Task 5: Implement File Storage for Student Records.
"""

import json
from models.serialisers import BookEncoder
from models.serialisers import BookDecoder

# File Path for where to import/export student data from
FILE_PATH = "database.json"

# Function for loading books
def load_books():
    # Open the file and load the books data, if not found return an empty list
    try:
        with open(FILE_PATH, "r") as f:
            # Use of booksEncoder to convert from JSON into books object
            return json.load(f, cls=BookDecoder)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 
    
def save_books(books_data):
    # Open the file and save the books data, if not found raise an exception
    try:
        with open(FILE_PATH, "w") as f:
            # Use of indentation and booksEncoder to convert into JSON in desired format
            json.dump(books_data, f, indent=4, cls=BookEncoder)
    except Exception as e:
        print(f"Error writing to file: {e}")
    