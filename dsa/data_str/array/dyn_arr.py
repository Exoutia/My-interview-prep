import ctypes

class DynamicArray:
    """A dynamic array class akin to simplified Python list."""

    def __init__(self) -> None:
        """Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Retun number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k"""
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')
        return self._A[k]

    def append(self, obj):
        """Add object to end of teh array."""
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity."""
        b = self._make_array(c)
        for k in range(self._n):
            b[k] = self._A[k]
        self._A = b
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c*ctypes.py_object)()

