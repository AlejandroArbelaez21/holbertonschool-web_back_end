#!/usr/bin/env python3

"""
2. Hypermedia pagination
"""
import csv
import math
from typing import List
from typing import Dict


def index_range(page: int, page_size: int) -> tuple:
    """
    function should return a tuple of size two containing a start
    index and an end index corresponding to the range of indexes
    """
    return (page - 1) * page_size, page * page_size


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
        """ Implement a method named get_page that takes two integer arguments
            page with default value 1 and page_size with default value 10.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        self.dataset()
        index = index_range(page=page, page_size=page_size)
        return self.__dataset[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Implement a get_hyper method that takes the same arguments
            (and defaults) as get_page and returns a dictionary
        """
        get = self.get_page(page, page_size)
        p = self.__dataset
        p_size = page_size
        my_dict = {
            'page_size': len(get),
            'page': page,
            'data': get,
            'next_page': page + 1 if (page + 1) < (len(p) / p_size) else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': math.ceil(len(p) / page_size)
        }
        return my_dict
