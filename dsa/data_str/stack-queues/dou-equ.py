class MyDeque():
    """A more general datastructure in which FIFO and LIFO both can occur"""
    DEFAULT_CPAPCITY = 10

    def __init__(self, maxLen:int = None) -> None:
        self._capacity = MyDeque.DEFAULT_CPAPCITY if not maxLen else maxLen
        self._size = 0
        self._data = [None] * self._capacity
        self._front = 0

    def __len__(self):
        """return the length of the deque

        Returns:
            int: number of elements in our datastructure.
        """
        return self._size

    def add_first(self, e):
        """Insert element e in the deque in front

        Args:
            e (element): the data that need to be inserted
        """
        if len(self) != self._capacity:
            self._data[self._front] = e
            self._front += 1
            self._size += 1
        else:
            self._front = (self._front - 1) % self._capacity
            self._data[self._front] = e


    def add_last(self, e):
        """Insert element at the back of the datastructure

        Args:
            e (element): the data that need to be inserted.
        """
        # todo: This need to be implemented.
        # if self._size != self._capacity:
        #     back = (self._front + self._size - 1) % self._capacity
        #     self._data[back] = e
        #     self._front += 1
        #     self._size += 1
        # else:
        pass
