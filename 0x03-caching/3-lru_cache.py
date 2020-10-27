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
        self.cache_data = collections.OrderedDict()

    def put(self, key, item):
        """ assign to the dictionary the item value for the key key """
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(key))

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        return self.cache_data.get(key)
