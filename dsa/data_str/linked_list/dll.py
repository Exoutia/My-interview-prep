class _DoublyLinkedBase:
    
    class node:
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self):
        self._header = self.node(None, None, None)
        self._trailer = self.node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, predecssor, successor):
        newest = self.node(e, predecssor, successor)
        predecssor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        predecssor = node._prev
        successor = node._next
        predecssor._next = successor
        successor._prev = predecssor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

class linked_deque(_DoublyLinkedBase):
        
    def first(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._header._next._element
    
    def last(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._trailer._prev._element
    
    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)
    
    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)
    
    def delete_first(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._delete_node(self._trailer._prev)
    
        