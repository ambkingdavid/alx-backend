#!/usr/bin/env python3

"""
Simple pagination with class
"""

import csv
import math
from typing import List, Tuple, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Args:
            page: requested page
            page_size: items requested per page
        Return:
            A dict with the following key-value pairs
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        total = math.ceil(len(self.dataset()) / page_size)
        next_page = None if page + 1 > total else page + 1
        prev_page = None if page - 1 < 1 else page - 1
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total
        }
