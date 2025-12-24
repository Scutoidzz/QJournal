"""
Search functionality for QJournal application.
TODO: Link the button to the search window.

# TODO: Implement comprehensive search system with proper indexing
# TODO: Add proper search result ranking and relevance scoring
# TODO: Add proper search performance optimization for large datasets

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
import sys

# TODO: Implement proper search module with database integration
# TODO: Add proper search indexing and caching
# TODO: Add proper search result management

json_path = "settingslist.json"

# TODO: Move configuration to proper settings management
# TODO: Add proper search configuration options
# TODO: Add proper search index management


# TODO: Consider moving this to a configuration file
# TODO: Add proper platform-specific search optimizations
osname = os.name

def search_window(search_text):
    """
    Open the search window.
    
    TODO:
    - Create a proper search window UI with modern design
    - Add search filters (date range, tags, mood, etc.)
    - Implement search result display with highlighting
    - Add support for modal/non-modal operation
    - Add keyboard shortcuts for quick access
    - Add proper search history and recent searches
    - Add proper search result export functionality
    """
    print("Initializing search...")
    # TODO: Implement search window functionality


def search_function(search_text):
    """
    TODO:
    - Implement actual search logic with database queries
    - Add support for fuzzy matching and similarity scoring
    - Add error handling for invalid search queries
    - Implement result pagination for large result sets
    - Add proper search result caching and performance optimization
    - Add search analytics and usage tracking
    """
    print(f"searching: {search_text}")
    # TODO: Fix this logic - currently searching in file path, not database content
    # TODO: Implement proper database search with SQL queries
    # TODO: Add proper search result formatting and metadata
    if search_text in json_path:
        print("Search path found")
        result = "found in path"
    else:
        result = "not found" 
        
    # TODO: Implement actual search functionality with database integration
    # TODO: Add proper search result ranking and relevance scoring
    # TODO: Find out how to get the results to return to the UI


    return [{"match": search_text, "file": json_path}]
