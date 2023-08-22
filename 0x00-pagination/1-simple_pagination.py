#!/usr/bin/env python3

"""
Simple pagination with class
"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get page
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        data = self.dataset()
        start, end = index_range(page, page_size)
        if start > len(data):
            return []
        return data[start:end]
