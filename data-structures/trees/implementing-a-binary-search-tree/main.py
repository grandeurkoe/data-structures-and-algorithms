class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def inorder_successor(current_node):
    """Get the successor node of the node to be deleted. Return successor node."""
    current_node = current_node.right
    successor_node = current_node
    while True:
        if current_node.left is None:
            return successor_node
        else:
            current_node = current_node.left
            if successor_node.value > current_node.value:
                successor_node = current_node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # INSERT OPERATION
    def insert(self, value):
        """Add node to the binary search tree."""
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            is_inserted = False
            while not is_inserted:
                if value > current_node.value:
                    if current_node.right is None:
                        current_node.right = new_node
                        is_inserted = True
                    else:
                        current_node = current_node.right
                elif value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        is_inserted = True

                    else:
                        current_node = current_node.left
        print(f"Insert node with Value({value}).")

    # REMOVE OPERATION
    def remove(self, value):
        """Remove node from binary search tree."""
        if self.root is None:
            print("No node available in the Binary Search Tree.")
        else:
            current_node = self.root
            parent_node = None
            value_exists = True
            while value_exists:
                if value == current_node.value:
                    # CASE 1: NODE TO BE DELETED IS A LEAF NODE.
                    if current_node.left is None and current_node.right is None:
                        if current_node == self.root:
                            self.root = None
                        else:
                            if current_node.value < parent_node.value:
                                parent_node.left = None
                            elif current_node.value > parent_node.value:
                                parent_node.right = None

                    # CASE 2: NODE TO BE DELETED IS AN INTERNAL NODE WITH 1 CHILD.
                    elif current_node.left is None or current_node.right is None:
                        if parent_node is None:
                            if current_node.left is not None:
                                self.root = current_node.left
                            elif current_node.right is not None:
                                self.root = current_node.right
                        else:
                            if current_node.left is not None:
                                current_node = current_node.left
                            elif current_node.right is not None:
                                current_node = current_node.right

                            if current_node.value < parent_node.value:
                                parent_node.left = current_node
                            elif current_node.value > parent_node.value:
                                parent_node.right = current_node

                    # CASE 3: NODE TO BE DELETED IS AN INTERNAL NODE WITH 2 CHILDREN.
                    elif current_node.left is not None and current_node.right is not None:
                        successor_node = inorder_successor(current_node)
                        self.remove(successor_node.value)
                        current_node.value = successor_node.value
                    print(f"Remove node with Value({value}).")
                    value_exists = False

                elif value < current_node.value:
                    if current_node.left is None:
                        value_exists = False
                    else:
                        parent_node = current_node
                        current_node = current_node.left
                elif value > current_node.value:
                    if current_node.right is None:
                        value_exists = False
                    else:
                        parent_node = current_node
                        current_node = current_node.right

    # LOOKUP OPERATION
    def lookup(self, value):
        """Check if the node exists in the Binary Search Tree."""
        if self.root is None:
            print("No node available in the Binary Search Tree.")
        else:
            current_node = self.root
            value_exists = True
            while value_exists:
                if value == current_node.value:
                    print(f"Node[{value}] available.")
                    value_exists = False
                elif value < current_node.value:
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        print(f"Node[{value}] not available.")
                        value_exists = False
                elif value > current_node.value:
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        print(f"Node[{value}] not available.")
                        value_exists = False


bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(98)
bst.insert(15)
bst.insert(1)
bst.remove(9)
bst.remove(4)
bst.lookup(20)
bst.lookup(5)
