# To provide for a general abstraction of  sequence of elements with the ability to identify 
# the location of element, we define a positional list ADT as well as a simpler position abstract data
# type to describe a location within a list. A position acts as a marker or token within the broader positional list.
# A position p is unaffected by the changes elsewhere in the list; The only way in which a position 
# become invalid if an explicit command is given to delete it.
# A position instance is a simple object which supports only:
# p.element(): Return the stored at position p.

# In the context of the positional list adt, position serve as parameters to some methods and as return values from other methods. 

from dll import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access.

    Args:
        _DoublyLinkedBase (double linked list): This the class we from which we are importing 
        doublylinked list used for the underlying of our positional list.
    """
    # --------------------------------nested Positon class------------------------------- #
    class Position:
        """An abstraction representing the location of a single element.
        """
        
        def __init__(self, container, node):
            """This constructor should not be invoked by the user.

            Args:
                conatainer (doublylinked list): This is the double linked list 
                where we are pointing positons with this position. This determines position which it points
                relation to some container.
                node (node): linked list single node
            """
            self._container = container
            self._node = node
        
        def element(self):
            """Return the element stored at this position.
            """
            return self._node._element
        
        def __eq__(self, other):
            """Return true if other is a position representing the same location.

            Args:
                other (position): some location of node.
            """
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            """Return true if other is not the same position or not the same node

            Args:
                other (position): Some other position.
            """
            return not (self == other)
    # --------------------------------Utility method------------------------------- #
    
    def _validate(self, p):
        """Return positon's node, or raise appropriate error if invalid.

        Args:
            p (position): The positon we get when in linked list
        """
        if not isinstance(p, self.Position):
            raise TypeError(f'{p} must be proper Position type')
        
        if p._container is not self:
            raise ValueError(f'{p} does not belong to this container.')
        
        if p._node._next is None:
            raise ValueError(f'{p} is no longer valid.')
        return p._node

    def _make_position(self, node):
        """Return Positions instance for given node (or None if sentinel).

        Args:
            node (node): the node of linked list
        """
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
    
    # -------------------------------- accessors ------------------------------- #
    def first(self):
        """Return the first position in the list (or None if list is empty).        
        """
        return self._make_position(self._header._next)
    
    def last(self):
        """Return the last poition of the list or none if the list is empty.
        """
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        """Return the previous element before the position provided

        Args:
            p (Position): The position provided.
        """
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        """Return the position just before the position p.

        Args:
            p (Position): Position provided.
        """
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        """Generate a forward iteration of the elements of the list.
        """
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    
    # -------------------------------- Mutators ------------------------------- #
    # Override inherited version to return Position, rather than Node
    
    def _insert_between(self, e, predecssor, successor):
        """Add element between existing nodes and return new Position.

        Args:
            e (element): Element we want to insert.
            predecssor (node): previous node
            successor (node): after node or next node
        """
        node = super()._insert_between(e, predecssor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        """Add element at front of the list and return new position.

        Args:
            e (element): element we want to insert
        """
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        """Add element at the last of list and return new position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        """Add element before the position provided

        Args:
            p (Position): Position of p
            e (Element): element we want to insert.
        """
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self, p, e):
        """Insert element e into list after the position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete_position(self, p):
        """Remove and return the element at Position p.
        """
        original = self._validate(p)
        return self._delete_node(original)
    
    def replace(self, p, e):
        """Replace the element at Position p with e

        Args:
            p (Position)
            e (element) 
        """
        original = self._validate(p)
        old_val = original._element
        original._element = e
        return old_val
    
 
def insertion_sort(pos_list: PositionalList()):
    if len(pos_list) > 1:
        marker = pos_list.first()
        while marker != pos_list.last():
            pivot = pos_list.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
                # print('1')
            else:
                walk = marker
                while walk != pos_list.first() and pos_list.before(walk).element() > value:
                    walk = pos_list.before(walk)
                pos_list.delete_position(pivot)
                pos_list.add_before(walk, value)
                


class FavouritesList:
    """List of elements ordered from most frequently accessed to least.
    """
    
    class _item:
        __slots__ = '_value', '_count'
        def __init__(self, e):
            self._value = e
            self._count = 0
    
    def _find_positions(self, e):
        """Search for element e and return its Position (or none if not find).

        Args:
            e (val): value for element
        """
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk 
    
    def _move_up(self, p):
        """Move item at position p earlier in the list based on access count.

        Args:
            p (Position): the position of element we want to add 
        """
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while 


if __name__ == "__main__":
    text = PositionalList()
    for i in range(9):
        x = text.add_first(i)

    while x:
        print(x.element(), end="-")
        x = text.after(x)
    print()
    insertion_sort(text)
    x = text.first()
    while x:
        print(x.element(), end="<->")
        x = text.after(x)
    
    
    
    
    
    
    