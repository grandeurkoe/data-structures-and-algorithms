class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    # DISPLAY OPERATION
    def display(self):
        """Display linked list."""
        disp_list = ""
        if self.length == 0:
            print("\nNo Nodes available in Doubly Linked List.")
        else:
            current_node = self.head
            while current_node:
                disp_list += f"{current_node.value} <-> "
                current_node = current_node.next
            print(f"\nDoubly Linked List:\n{disp_list[:-4]}")

    # APPEND OPERATION -> Big O - O(1).
    def append(self, value):
        """Add a node with given value at the end of the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1
        print(f"Append Node({value}).")

    # PREPEND OPERATION -> Big O - O(1).
    def prepend(self, value):
        """Add a node with a given value at the beginning of the list."""
        new_node = Node(value)
        if self.length == 0:
            self.append(value)
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            self.length += 1
            print(f"Prepend Node({value}).")

    # INSERT OPERATION -> Big O - O(n).
    def insert(self, index, value):
        """Insert node with a given value at a given index."""
        new_node = Node(value)
        if index <= 0:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.previous = current_node
            current_node.next.previous = new_node
            current_node.next = new_node
            self.length += 1

    # DELETE OPERATION -> Big O - O(n).
    def remove(self, index):
        """Remove node at given index."""
        if self.length == 0:
            print("No Nodes available in Doubly Linked List.")
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            if index == 0:
                print(f"Delete Node({self.head.value}).")
                next_node = self.head.next
                self.head.value = next_node.value
                self.head.next = next_node.next
                self.head = next_node
                self.head.previous = None
                self.length -= 1
            elif index >= self.length - 1:
                current_node = self.tail.previous
                print(f"Delete Node({current_node.next.value}).")
                current_node.next = None
                self.tail = current_node
                self.length -= 1
            else:
                current_node = self.head
                for _ in range(index - 1):
                    current_node = current_node.next
                print(f"Delete Node({current_node.next.value}).")
                current_node.next = current_node.next.next
                current_node.next.previous = current_node
                self.length -= 1

    # LOOKUP OPERATION -> Big O - O(n).
    def lookup(self, index):
        """Get node by index."""
        if self.length == 0:
            print("No Nodes available in Doubly Linked List.")
        else:
            current_node = self.head
            if index in range(self.length):
                for _ in range(index):
                    current_node = current_node.next
                print(f"Node({current_node.value}) at Index[{index}].")
            else:
                print("Index out of range!")


linked_list = DoublyLinkedList()
print("\nOPERATION LOG")
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.prepend(4)
linked_list.insert(1, 10)
linked_list.remove(2)
linked_list.lookup(2)
linked_list.remove(0)
linked_list.remove(0)
linked_list.remove(0)
linked_list.remove(0)
linked_list.display()
