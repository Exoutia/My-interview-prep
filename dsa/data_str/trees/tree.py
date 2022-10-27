# As we did with positional lists in Section 7.4, we deﬁne a tree ADT using the
# concept of a position as an abstraction for a node of a tree. An element is stored
# at each position, and positions satisfy parent-child relationships that deﬁne the tree
# structure. A position object for a tree supports the method:
# p.element( ): Return the element stored at position p.
# The tree ADT then supports the following accessor methods, allowing a user to
# navigate the various positions of a tree:
# T.root( ): Return the position of the root of tree T,
# or None if T is empty.
# T.is root(p): Return True if position p is the root of Tree T.
# T.parent(p): Return the position of the parent of position p,
# or None if p is the root of T.
# T.num children(p): Return the number of children of position p.
# T.children(p): Generate an iteration of the children of position p.
# T.is leaf(p): Return True if position p does not have any children.
# len(T): Return the number of positions (and hence elements) that
# are contained in tree T.
# T.is empty( ): Return True if tree T does not contain any positions.
# T.positions( ): Generate an iteration of all positions of tree T.
# iter(T): Generate an iteration of all elements stored within tree T.

class AbstrarctTree:
    """Abstract base class representing a tree struvture."""

    class Position:
        """An abstraction representing the location of single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, __o: object) -> bool:
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, __o: object) -> bool:
            """Return True if other Position represents the different location."""
            return not(self==__o)
            
    def root(self):
        """Return Position representing the tree's (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Retrun Position representing the p's parent (or none if is parent)"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Genereate an iteration of poition represnting p's children"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self)==0