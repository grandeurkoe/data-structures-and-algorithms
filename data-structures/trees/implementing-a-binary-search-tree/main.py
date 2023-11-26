class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def inorder_successor(self, node_to_be_deleted):
        """Get the successor node of the node to be deleted. Return successor node."""
        traverse_node = node_to_be_deleted.right
        successor_node = node_to_be_deleted.right
        found_successor = False
        while not found_successor:
            if traverse_node.left is not None:
                traverse_node = traverse_node.left
                if traverse_node.value < successor_node.value:
                    successor_node = traverse_node
            else:
                return successor_node

    def insert(self, value):
        """Add node to the binary search tree."""
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            insert_success = False
            current_node = self.root
            while not insert_success:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        insert_success = True
                    else:
                        current_node = current_node.left
                elif value > current_node.value:
                    if current_node.right is None:
                        current_node.right = new_node
                        insert_success = True
                    else:
                        current_node = current_node.right
        self.length += 1
        print(f"Insert Node({value}).")

    def remove(self, value):
        """Remove node from binary search tree."""
        if self.length == 0:
            print("No Nodes available in Binary Search Tree.")
        else:
            current_node = self.root
            parent_node = None
            remove_failure = False
            while not remove_failure:
                if value == current_node.value:
                    # CASE 1: Delete leaf nodes.
                    if current_node.left is None and current_node.right is None:
                        if parent_node is None:
                            self.root = None
                        else:
                            if current_node.value < parent_node.value:
                                parent_node.left = None
                            elif current_node.value > parent_node.value:
                                parent_node.right = None
                        self.length -= 1
                        print(f"Remove Node({value}).")
                        break

                    # CASE 2: Delete node with a single child.
                    elif current_node.left is None or current_node.right is None:
                        if parent_node is None:
                            if current_node.left is not None:
                                self.root = current_node.left
                            elif current_node.right is not None:
                                self.root = current_node.right
                        else:
                            if current_node.left is not None:
                                current_node = current_node.left
                                parent_node.left = current_node
                            elif current_node.right is not None:
                                current_node = current_node.right
                                parent_node.right = current_node
                        self.length -= 1
                        print(f"Remove Node({value}).")
                        break

                    # CASE 3: Delete node with two children.
                    elif current_node.left is not None and current_node.right is not None:
                        print(f"Remove Node({value}).")
                        successor_node = self.inorder_successor(current_node)
                        self.remove(successor_node.value)
                        print(f"Move Node({successor_node.value}) to Node({value}).")
                        current_node.value = successor_node.value
                        break

                elif value < current_node.value:
                    if current_node.left is None:
                        print(f"Node({value}) doesn't exist.")
                        remove_failure = True
                    else:
                        parent_node = current_node
                        current_node = current_node.left
                elif value > current_node.value:
                    if current_node.right is None:
                        print(f"Node({value}) doesn't exist.")
                        remove_failure = True
                    else:
                        parent_node = current_node
                        current_node = current_node.right

    def lookup(self, value):
        """Check if the node exists in the Binary Search Tree."""
        if self.length == 0:
            print("No Nodes available in Binary Search Tree.")
        else:
            current_node = self.root
            found_success = False
            while not found_success:
                if value == current_node.value:
                    print(f"Node({value}) exists.")
                    found_success = True
                elif value < current_node.value:
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        print(f"Node({value}) doesn't exist.")
                        found_success = True
                elif value > current_node.value:
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        print(f"Node({value}) doesn't exist.")
                        found_success = True


bst = BinarySearchTree()
print("\nOPERATION LOG")
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
