#!/usr/bin/python3
""" BasicCache module
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache defines two functions:
      - put
      - get
    """
    def put(self, key, item):
        """ assign to the dictionary self.cache_data the item value for the key key """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        return self.cache_data.get(key)
