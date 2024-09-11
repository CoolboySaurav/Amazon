from collections import defaultdict

class Node(object):
    def __init__(self, key=None, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.nodeMap = {}  # Better to use a regular dictionary
        self.cap = capacity
        self.left = Node(0)  # Dummy head node
        self.right = Node(0)  # Dummy tail node
        self.left.next, self.right.prev = self.right, self.left  # Initialize doubly linked list

    def insert(self, node):
        """Insert node before the right dummy node (most recent)"""
        prev, next = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def remove(self, node):
        """Remove node from its current position"""
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.nodeMap:
            # Update the value and move to the most recent position
            self.remove(self.nodeMap[key])
            self.nodeMap[key].val = value
            self.insert(self.nodeMap[key])
        else:
            if len(self.nodeMap) == self.cap:
                # Remove the least recently used node
                lru = self.left.next  # LRU node is at the front
                del self.nodeMap[lru.key]
                self.remove(lru)
            
            # Insert the new node
            node = Node(key, value)
            self.nodeMap[key] = node
            self.insert(node)
# Unit testing module for above code
# import unittest

# class TestLRUCache(unittest.TestCase):
#     def setUp(self):
#         """Set up the test environment before each test."""
#         self.cache = LRUCache(2)  # Create an LRUCache with capacity 2

#     def test_put_and_get(self):
#         """Test basic put and get functionality."""
#         self.cache.put(1, 1)
#         self.cache.put(2, 2)
#         self.assertEqual(self.cache.get(1), 1)  # Should return 1
#         self.cache.put(3, 3)  # Evicts key 2
#         self.assertEqual(self.cache.get(2), -1)  # Should return -1 (not found)
#         self.cache.put(4, 4)  # Evicts key 1
#         self.assertEqual(self.cache.get(1), -1)  # Should return -1 (not found)
#         self.assertEqual(self.cache.get(3), 3)  # Should return 3
#         self.assertEqual(self.cache.get(4), 4)  # Should return 4

#     def test_update_existing_key(self):
#         """Test that updating an existing key changes the value and order."""
#         self.cache.put(1, 1)
#         self.cache.put(2, 2)
#         self.cache.put(1, 10)  # Update key 1 to 10
#         self.assertEqual(self.cache.get(1), 10)  # Should return updated value 10
#         self.cache.put(3, 3)  # Evicts key 2, not key 1
#         self.assertEqual(self.cache.get(2), -1)  # Should return -1 (not found)
#         self.assertEqual(self.cache.get(1), 10)  # Should still return 10
#         self.assertEqual(self.cache.get(3), 3)  # Should return 3

#     def test_cache_eviction_order(self):
#         """Test that cache evicts in the correct order."""
#         self.cache.put(1, 1)
#         self.cache.put(2, 2)
#         self.cache.get(1)  # Access key 1
#         self.cache.put(3, 3)  # Should evict key 2 (least recently used)
#         self.assertEqual(self.cache.get(2), -1)  # Should return -1 (not found)
#         self.assertEqual(self.cache.get(1), 1)  # Should return 1
#         self.assertEqual(self.cache.get(3), 3)  # Should return 3

#     def test_capacity_one(self):
#         """Test behavior with a cache capacity of one."""
#         self.cache = LRUCache(1)  # Create an LRUCache with capacity 1
#         self.cache.put(1, 1)
#         self.assertEqual(self.cache.get(1), 1)  # Should return 1
#         self.cache.put(2, 2)  # Evicts key 1
#         self.assertEqual(self.cache.get(1), -1)  # Should return -1 (not found)
#         self.assertEqual(self.cache.get(2), 2)  # Should return 2

#     def test_invalid_key(self):
#         """Test get with an invalid key."""
#         self.assertEqual(self.cache.get(999), -1)  # Should return -1 (not found)

# if __name__ == '__main__':
#     unittest.main()
