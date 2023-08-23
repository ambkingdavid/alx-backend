#!/usr/bin/python3
"""
BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        defines a Basic cache system
    """
    def put(self, key: str, item: any) -> None:
        """
            inserts or update the cache
        """
        if (key and item):
            self.cache_data[key] = item

    def get(self, key: str) -> any:
        """
        gets an item from the cache
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None
