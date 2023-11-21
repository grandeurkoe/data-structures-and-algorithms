class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def display(self):
        """Display queue."""
        if self.length == 0:
            print("\nNo data elements available in the Stack.")
        else:
            queue_disp = []
            current_node = self.first
            print("\nQueue:")
            while current_node:
                queue_disp.append(str(current_node.value))
                current_node = current_node.next
            print("-" * (self.length * 3))
            print(f'{"  ".join(queue_disp)}')
            print("-" * (self.length * 3))

    # ENQUEUE OPERATION
    # Time complexity or BIG(O) - O(1)
    def enqueue(self, value):
        """Add data element to the end of the queue."""
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = self.first
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        print(f"Push '{value}'.")

    # DEQUEUE OPERATION
    # Time complexity or BIG(O) - O(1)
    def dequeue(self):
        """Remove data element from the beginning of the queue."""
        if self.length == 0:
            print("No data elements available in the Stack.")
        else:
            element_to_delete = self.first.value
            if self.length == 1:
                self.first = None
                self.last = None
                self.length -= 1
            else:
                next_node = self.first.next
                self.first = next_node
                self.length -= 1
            print(f"Pop '{element_to_delete}'.")

    # PEEK OPERATION
    # Time complexity or BIG(O) - O(1)
    def peek(self):
        """Get data element from the beginning of the queue."""
        if self.length == 0:
            print("No data elements available in the Stack.")
        else:
            print(f"Value({self.first.value}) is at the beginning of the queue.")


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
queue.peek()
queue.display()
