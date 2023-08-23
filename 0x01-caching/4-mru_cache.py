#!/usr/bin/python3
"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    def __init__(self):
        """
        initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        add key
        """
        if key is not None and item is not None:
            # Check if the cache is full
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Get the most recently used key (MRU)
                mru_key = next(reversed(self.cache_data))
                # Remove the MRU item from the cache
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")
            # Add the new item to the cache
            self.cache_data[key] = item

    def get(self, key):
        """
        get key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
