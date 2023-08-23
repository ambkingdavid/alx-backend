#!/usr/bin/python3
"""
FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines a chache that work with the FIFO principle
    """
    def put(self, key: str, item: any) -> None:
        """
            inserts or update the cache
        """
        if (key and item):
            self.cache_data[key] = item
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key: str) -> any:
        """
        gets an item from the cache
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None
