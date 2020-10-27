#!/usr/bin/python3
""" BasicCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines two functions:
      - put
      - get
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ assign to the dictionary the item value for the key key """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                for k in self.cache_data:
                    del self.cache_data[k]
                    print("DISCARD: {}".format(k))
                    break

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        return self.cache_data.get(key)
