class EmptyError:
    pass

class sll:
    
    class node:
        __slots__ = '_val', '_next'
        
        def __init__(self, _val, _next):
            self._val = _val
            self._next = _next
    
    def __init__(self):
        self._head = None
        self._size = 0
        self._tail = None
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    # @abstractmethod
    def insert_at_last(self, val):
        newest = self.node(val, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    
    # @abstractmethod
    def insert_at_first(self, val):
        self._head = self.node(val, self._head)
        if self.is_empty():
            self._tail = self._head
        self._size += 1
        
    # @abstractmethod
    def insert_mid(self, val, pos):
        if pos > self._size or pos < 0:
            raise IndexError('Invalid index')
        if pos == 0:
            # this is same as insert at first 
            self.insert_at_first(val)
            return 
        if pos == self._size:
            # this is same as insert at last
            self.insert_at_last(val)
            return 
        temp = self._head
        count = pos-1
        while count:
            count -= 1
            temp = temp._next
        newnode = self.node(val, None)
        newnode._next = temp._next
        temp._next = newnode
        self._size += 1
    
    def delete_at_first(self):
        if self.is_empty():
            raise EmptyError('list is empty')            
        temp = self._head
        self._head = temp._next
        del(temp)
        self._size -= 1
        return True  
    
    def delete_at_last(self):
        if self.is_empty():
            raise EmptyError('list is Empty')
        temp = self._head
        while temp._next:
            temp = temp._next
            print(temp._val)
        self._tail = temp
        self._tail._next = None
        self._size -= 1
        # del(temp._next)    
    
    def display(self):
        temp = self._head
        while temp._next:
            print(temp._val, end='->')
            temp = temp._next
        print(temp._val)

class link_stack(sll):
    def push(self, val):
        super().insert_at_first(val)
    

if __name__ == "__main__":
    
    lin = sll()
    for i in range(9, 0, -1):
        lin.insert_at_first(i)
    lin.delete_at_last()
    print(len(lin))
    lin.display()
    stack_link = link_stack()
    stack_link.push(67)
    stack_link.insert_at_first(90)
    print(len(stack_link))
    stack_link.display()