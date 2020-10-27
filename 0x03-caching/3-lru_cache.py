#!/usr/bin/python3
""" BasicCache module
"""
import collections
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ FIFOCache defines two functions:
      - put
      - get
    """
    def __init__(self):
        """ Constructor """
        super().__init__()

    def put(self, key, item):
        """ assign to the dictionary the item value for the key key """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                sorted_dict_keys = sorted(self.cache_data)
                last = sorted_dict_keys.popitem(last=False)
                print('DISCARD: {}'.format(last[0]))

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        return self.cache_data.get(key)
