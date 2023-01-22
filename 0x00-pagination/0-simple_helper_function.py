#!/usr/bin/env python3
"""Simple helper function"""
def index_range(page: int, page_size: int) -> tuple:
    """ return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters. """
    last_index = page_size * page
    first_index = last_index - page_size
    return (first_index, last_index)
