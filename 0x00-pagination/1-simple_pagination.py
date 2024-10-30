#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple, TypedDict


class HypermediaPagination(TypedDict):
    page_size: int
    page: int
    data: List[List]
    next_page: int
    prev_page: int
    total_pages: int


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    tuple of size two containing a start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


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
        """Retrieves a page of data.
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> HypermediaPagination:
        return {
        "page_size": page_size,
        "page": page,
        "data": self.get_page(page, page_size),  # Populate with actual data
        "next_page": page + 1,
        "prev_page": page - 1 if page > 1 else None,
        "total_pages": 100,  # Example total pages value
        }
