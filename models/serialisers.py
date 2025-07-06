"""
serialisers.py
--------------
Provides JSON encoding and decoding logic for Student and Undergraduate objects.

This module defines custom JSONEncoder and JSONDecoder subclasses to handle
serialization (saving to JSON) and deserialization (loading from JSON) of 
Student and Undergraduate objects, preserving object structure and class hierarchy.

Used to integrate object-oriented structures with persistent file storage.

Additionally added for Part of Task 5: Implement File Storage for Student Records.
"""

from models.book import Book
import json

class BookEncoder(json.JSONEncoder):
    # Override the default() method to define how custom Student and Undergraduate objects are serialised
    # 'o', being  the object in reference
    def default(self, o):
        # If the instance of the object is a student
        if isinstance(o, Book):
            # If the instance of the object is an undergrad encode into JSON in this format
                return {
                    "isbn": o.isbn, 
                    "title": o.title, 
                    "author": o.author, 
                    "publisher": o.publisher, 
                    "pub_year": o.pub_year,
                    "genre": o.genre,
                    "available": o.available,
                    "total": o.total,
                }
        
        # Fall back to the default behavior for other object types
        return super().default(o)

class BookDecoder(json.JSONDecoder):
    def __init__(self):
        # Override the default initaliser to use a custom object_hook
        super().__init__(object_hook=self.object_hook)

    def object_hook(self, dct):
        # This method is automatically called during JSON decoding.
        # It converts JSON dictionaries into Book objects,
        if "isbn" in dct and "title" in dct and "author" in dct and "publisher" in dct and "pub_year" in dct and "genre" in dct and "available" in dct and "total" in dct:
            return Book(dct["isbn"], dct["title"], dct["author"], dct["publisher"], dct["pub_year"], dct["genre"], dct["available"], dct["total"])
        return dct