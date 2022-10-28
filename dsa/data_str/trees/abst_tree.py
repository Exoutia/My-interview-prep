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
# T.depth(p): let p be the positon of a node of tree T. then the depth of p would be number of ancestors of p, exluding p itself,
# • If p is the root, then the depth of p is 0.
# • Otherwise, the depth of p is one plus the depth of the parent of p.

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

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self):
        """Return the height of the tree
        O(n^2) time complexity"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _heihgt2(self, p):
        """Return the height of the subtree rooted at Position p.
        linear time complexity"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._heihgt2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at position p

        Args:
            p (Node, optional): subtree node. Defaults to None.
        if p is none return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._heihgt2(p)

    