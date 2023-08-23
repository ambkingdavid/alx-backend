#!/usr/bin/python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Defines a chache that work with the FIFO principle
    """
    def put(self, key: str, item: any) -> None:
        """
            inserts or update the cache
        """
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS - 1):
            if (key and item):
                last_key = list(self.cache_data)[-1]
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
        if (key and item):
            self.cache_data[key] = item

    def get(self, key: str) -> any:
        """
        gets an item from the cache
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None
