#!/usr/bin/python3
"""
LRUCaching module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Defines LRUCache class
    """
    def __init__(self):
        """
        initialize the LRUCache instance
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        insert into cache
        """
        if key is not None and item is not None:
            # Check if the cache is full
            if len(self.cache_data) > self.MAX_ITEMS - 1:
                # Get the least recently used key (LRU)
                lru_key = self.order.pop(0)
                # Remove the LRU item from the cache
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            # Add the new item to the cache
            self.cache_data[key] = item
            # Add the key to the LRU order
            self.order.append(key)

    def get(self, key):
        """
        get from the cache
        """
        if key is not None and key in self.cache_data:
            # Move the accessed key to the end of the LRU order
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
