class Node:
    def __init__(self, val) -> None:
        self.l_child = None
        self.r_child = None
        self.data = val



def insert(root: Node, node: Node):
    if root is None:
        root = node

    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                insert(root.r_child, node)

def pre_order_print(root):
    if not root:
        return
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)
    

