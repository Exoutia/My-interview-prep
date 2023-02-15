# this a stack implementation using a python list.
class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass



class ArrayStack:
    """LIFO Stack implementation using python list as underlying storage."""

    def __init__(self) -> None:
        """Create an empty array."""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return if the stack is empty or not"""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of stack"""
        self._data.append(e)

    def top(self):
        """Return (do not remove) the element of the top of the stack.
        Return Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]    # the last item in the list

    def pop(self):
        """This will remove the top element and return it.
        Return Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("stack is empty")
        return self._data.pop()
    
