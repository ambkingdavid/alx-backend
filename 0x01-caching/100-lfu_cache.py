#!/usr/bin/python3
"""
LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Define class
    """
    def __init__(self):
        """
        initialize
        """
        super().__init__()
        self.order = []
        self.frequency = {}

    def put(self, key, item):
        """
        insert into cache
        """
        del_key: str
        data = self.cache_data
        if (key is not None and item is not None and key not in data):

            if len(self.cache_data) > self.MAX_ITEMS - 1:
                max_freq = min(self.frequency.values())
                lfu_key = [k for k, v in self.frequency.items()
                           if v == max_freq]

                if len(lfu_key) > 1:
                    for i in range(len(self.order)):
                        if self.order[i] in lfu_key:
                            del_key = self.order.pop(i)
                            break
                else:
                    del_key = lfu_key[0]
                # Remove the LRU item from the cache
                del self.cache_data[del_key]
                del self.frequency[del_key]
                print(f"DISCARD: {del_key}")
            # Add the new item to the cache
            self.cache_data[key] = item
            # Add the key to the LRU order
            self.order.append(key)
            # Add the key to lfu frequency
            self.frequency[key] = 0
        elif (key is not None and item is not None and key in data):
            # Add the new item to the cache
            self.cache_data[key] = item
            # Add the key to the LRU order
            self.order.remove(key)
            self.order.append(key)
            # Add the key to lfu frequency
            self.frequency[key] = self.frequency[key] + 1

    def get(self, key):
        """
        get from the cache
        """
        if key is not None and key in self.cache_data:
            # Move the accessed key to the end of the LRU order
            self.order.remove(key)
            self.order.append(key)
            # update the frequency
            self.frequency[key] = self.frequency[key] + 1
            return self.cache_data[key]
        return None
