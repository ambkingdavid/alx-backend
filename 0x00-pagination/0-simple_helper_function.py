#!/usr/bin/env python3

"""
Contains a simpler helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """
    Args:
        page: Requested page
        page_size: Items requested per page
    Return:
        A tuple of size two contaiing a start index and end index
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    paged = start_index, end_index
    return tuple(paged)
