"""
Search functionality for QJournal application.
TODO: Link the button to the search window.


TODO:
- Implement search window UI with filters and search results display
- Add support for searching within entry titles and content
- Implement case-insensitive search -- or just save each entry with multiple entries
- Add support for regular expressions in search
- Add keyboard shortcuts for common search operations
- Add support for searching within specific date ranges
- Implement search result navigation
- Add support for saving/loading search queries
"""

from PyQt6.QtWidgets import QLineEdit, QPushButton
import sys
import os
import regex


# TODO: Consider moving this to a configuration file
osname = os.name

def search_window(search_text):

    
    """Open the search window.
    
    TODO:
    - Create a proper search window UI
    - Add search filters (date range, tags, etc.)
    - Implement search result display
    - Add support for modal/non-modal operation
    - Add keyboard shortcuts for quick access
    """
    print("Initializing search...")
    # TODO: Implement search window functionality


def search_function(search_text):
    """
    TODO:
    - Implement actual search logic
    - Add support for fuzzy matching
    - Add support for boolean operators (AND, OR, NOT)
    - Implement search result ranking
    - Add support for searching within specific fields (title, content, tags)
    - Add error handling for invalid search queries
    - Implement result pagination for large result sets
    """
    print(f"searching: {search_text}")
    # TODO: Implement actual search functionality
    return []
