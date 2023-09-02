class Node:
    def __init__(self, value):
        """Creates an empty node."""
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        """Creates an empty binary search tree."""
        self.root = None

    def inorder_successor(self, node_to_delete):
        """Returns the successor node of the node to be deleted."""
        traverse_node = node_to_delete.right
        successor_node = traverse_node
        while True:
            if traverse_node.left is None:
                return successor_node
            else:
                traverse_node = traverse_node.left
                if traverse_node.value < successor_node.value:
                    successor_node = traverse_node

    def insert(self, value):
        """Adds a node to the binary search tree."""
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            is_insert_failure = True
            while is_insert_failure:
                if new_node.value > current_node.value:
                    if current_node.right is None:
                        current_node.right = new_node
                        is_insert_failure = False
                    else:
                        current_node = current_node.right
                if new_node.value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        is_insert_failure = False
                    else:
                        current_node = current_node.left

    def lookup(self, value):
        """Checks if the node exists in the binary search tree. Prints the value if the node exists."""
        if self.root is None:
            print("No Nodes available in BST.")
        else:
            current_node = self.root
            is_not_match = True
            while is_not_match:
                if value == current_node.value:
                    print(value)
                    is_not_match = False
                elif value > current_node.value:
                    if current_node.right is None:
                        print("Not Found!")
                        is_not_match = False
                    else:
                        current_node = current_node.right
                elif value < current_node.value:
                    if current_node.left is None:
                        print("Not Found!")
                        is_not_match = False
                    else:
                        current_node = current_node.left

    def remove(self, value):
        """Removes a node from the binary search tree."""
        if self.root is None:
            print("No nodes available in BST.")
        else:
            current_node = self.root
            parent_node = None
            is_not_match = True
            while is_not_match:
                if value == current_node.value:
                    # Case 1: Node to be deleted is a leaf node.
                    if current_node.left is None and current_node.right is None:
                        if parent_node is None:
                            self.root = None
                        else:
                            if current_node.value > parent_node.value:
                                parent_node.right = None
                            elif current_node.value < parent_node.value:
                                parent_node.left = None
                    # Case 2: Node to be deleted is an internal node with 1 child.
                    elif current_node.left is None or current_node.right is None:
                        if parent_node is None:
                            if current_node.left is not None:
                                self.root = current_node.left
                            elif current_node.right is not None:
                                self.root = current_node.right
                        else:
                            if current_node.left is not None:
                                current_node = current_node.left
                                current_node.left = None
                            elif current_node.right is not None:
                                current_node = current_node.right
                                current_node.right = None

                            if current_node.value > parent_node.value:
                                parent_node.right = current_node
                            elif current_node.value < parent_node.value:
                                parent_node.left = current_node
                    # Case 3: Node to be deleted is an internal node with 2 children.
                    elif current_node.left is not None and current_node.right is not None:
                        successor_node = self.inorder_successor(current_node)
                        self.remove(successor_node.value)
                        current_node.value = successor_node.value

                    is_not_match = False
                elif value > current_node.value:
                    if current_node.right is None:
                        print("Not Found!")
                        is_not_match = False
                    else:
                        parent_node = current_node
                        current_node = current_node.right
                elif value < current_node.value:
                    if current_node.left is None:
                        print("Not Found!")
                        is_not_match = False
                    else:
                        parent_node = current_node
                        current_node = current_node.left

    def breadth_first_search(self):
        bfs_list = []
        back_link_queue = []
        current_node_counter = 0
        current_node = self.root
        bfs_list.append(current_node.value)
        back_link_queue.append(current_node)
        is_not_end = True

        while is_not_end:

            next_node = current_node.left
            back_link_queue.append(next_node)
            bfs_list.append(next_node.value)

            next_node = current_node.right
            back_link_queue.append(next_node)
            bfs_list.append(next_node.value)

            current_node_counter += 1

            current_node = back_link_queue[current_node_counter]

            if current_node.left is None or current_node.right is None:
                is_not_end = False

        print(bfs_list)
