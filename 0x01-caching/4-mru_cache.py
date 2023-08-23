#!/usr/bin/python3
"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    define class
    """
    def __init__(self):
        """
        initialize
        """
        super().__init__()
        self.recent = []

    def put(self, key, item):
        """
        add key
        """
        if key is not None and item is not None:
            # Check if the cache is full
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key = list(self.cache_data)[-1]
                if self.recent:
                    last_key = self.recent.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        get key
        """
        if key is not None and key in self.cache_data:
            self.recent = []
            self.recent.append(key)
            return self.cache_data[key]
        return None
