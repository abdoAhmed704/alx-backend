#!/usr/bin/env python3
"""
return a tuple of size two containing a start index and an end index.
"""

import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """
    tuple of size two containing a start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
