#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching is doing the thing."""
    def __init__(self):
        """Intialize values"""
        super().__init__()

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
        the item value for the key key."""
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-2]
            self.cache_data.pop(last_key)
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """Must return the value in self.cache_data linked to key"""
        if self.cache_data.get(key) is None or key is None:
            return None
        return self.cache_data.get(key)
