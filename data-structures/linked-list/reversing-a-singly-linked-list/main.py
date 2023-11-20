class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def display(self):
        """Display linked list."""
        if self.length == 0:
            print("\nNo nodes available in Singly Linked List.")
        else:
            disp_list = ""
            current_node = self.head
            while current_node:
                disp_list += f"[{current_node.value}]"
                current_node = current_node.next
                if current_node is not None:
                    disp_list += " -> "
            print(f"\nSingly Linked List: {disp_list}")

    # LOOKUP OPERATION
    # Time complexity or BIG(O) - O(n)
    def lookup(self, index):
        """Get node by index."""
        if self.length == 0:
            print("No nodes available in Singly Linked List.")
        else:
            if index in range(self.length):
                current_node = self.head
                for _ in range(index):
                    current_node = current_node.next
                print(f"Node[{current_node.value}] at Index[{index}].")
            else:
                print("Index out of range.")

    # APPEND OPERATION
    # Time complexity or BIG(O) - O(1)
    def append(self, value):
        """Add a node with given value at the end of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        print(f"Append node with Value({value}).")

    # PREPEND OPERATION
    # Time complexity or BIG(O) - O(1)
    def prepend(self, value):
        """Add a node with a given value at the beginning of the list."""
        new_node = Node(value)
        if self.head is None:
            self.append(value)
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            print(f"Prepend node with Value({value}).")

    # INSERT OPERATION
    # Time complexity or BIG(O) - O(n)
    def insert(self, index, value):
        """Insert node with a given value at a given index."""
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
        elif index == self.length - 1:
            self.append(value)
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
            print(f"Insert node with Value({value}) at Index[{index}].")

    # DELETE OPERATION
    # Time complexity or BIG(O) - O(n)
    def delete(self, index):
        """Remove node at given index."""
        if index in range(self.length):
            if self.length == 0:
                print("No nodes available in Singly Linked List.")
            elif self.length == 1:
                self.head = None
                self.tail = None
                self.length -= 1
                print(f"Remove node at Index[0].")
            else:
                if index == 0:
                    next_node = self.head.next
                    self.head.value = next_node.value
                    self.head.next = next_node.next
                    self.head = next_node
                    self.length -= 1
                    print(f"Remove node at Index[{index}].")
                elif index == self.length - 1:
                    current_node = self.head
                    for _ in range(index - 1):
                        current_node = current_node.next
                    current_node.next = None
                    self.tail = current_node
                    self.length -= 1
                    print(f"Remove node at Index[{index}].")
                elif 0 < index < self.length - 1:
                    current_node = self.head
                    for _ in range(index - 1):
                        current_node = current_node.next
                    current_node.next = current_node.next.next
                    self.length -= 1
                    print(f"Remove node at Index[{index}].")
        else:
            print("Index out of range.")

    def reverse(self):
        """Reverse linked list."""
        if self.length == 0:
            print("No nodes available in Singly Linked List.")
        elif self.length == 1:
            pass
        else:
            first = self.head
            second = first.next
            self.tail = self.head
            while second:
                temp = second.next
                second.next = first
                first = second
                second = temp
            self.head.next = None
            self.head = first
            print(f"Reverse Singly Linked List.")


linked_list = SinglyLinkedList()
linked_list.prepend(10)
linked_list.append(5)
linked_list.prepend(1)
linked_list.insert(1, 16)
linked_list.delete(0)
# linked_list.delete(2)
linked_list.lookup(1)
linked_list.reverse()
linked_list.display()
