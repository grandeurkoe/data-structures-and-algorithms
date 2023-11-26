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
            print("\nQueue:\nEmpty")
        else:
            disp_queue = []
            current_node = self.first
            while current_node:
                disp_queue.append(f"{current_node.value}")
                current_node = current_node.next
            print(f"\nQueue:\n{' '.join(disp_queue)}")

    # ENQUEUE OPERATION -> Big O - O(1).
    def enqueue(self, value):
        """Add node to the end of the queue."""
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = self.first
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        print(f"Enqueue Node({value}).")

    # DEQUEUE OPERATION -> Big O - O(1).
    def dequeue(self):
        """Remove node from the beginning of the queue."""
        if self.length == 0:
            print("No nodes available in Queue.")
        elif self.length == 1:
            print(f"Dequeue Node({self.first.value}).")
            self.first = None
            self.last = None
            self.length -= 1
        else:
            print(f"Dequeue Node({self.first.value}).")
            current_node = self.first.next
            self.first = current_node
            self.length -= 1

    # PEEK OPERATION -> Big O - O(1).
    def peek(self):
        """Get node from the beginning of the queue."""
        if self.length == 0:
            print("No nodes available in Queue.")
        else:
            print(f"Node({self.first.value}) is the first element in the Queue.")

    # LOOKUP OPERATION -> Big O - O(n).
    def lookup(self, value):
        """Check if node exists."""
        if self.length == 0:
            print("No nodes available in Queue.")
        else:
            current_node = self.first
            while current_node:
                if current_node.value == value:
                    print(f"Node({current_node.value}) exists.")
                    return None
                current_node = current_node.next
            print(f"Node({value}) doesn't exist.")


queue = Queue()
print("\nOPERATION LOG")
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.dequeue()
queue.peek()
queue.lookup(8)
queue.display()
