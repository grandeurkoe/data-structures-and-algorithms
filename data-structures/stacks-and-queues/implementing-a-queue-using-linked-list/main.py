class Node:
    def __init__(self, value):
        """Creates an empty node."""
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        """Creates an empty queue."""
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        """Prints the first node in the queue."""
        if self.length == 0:
            print(None)
        else:
            print(self.first.value)

    def enqueue(self, value):
        """Adds a node at the end of the queue."""
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            current_node = self.first
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        """Removes the front node from the queue."""
        if self.length == 0:
            print("No data available in the Queue.")
        elif self.first == self.last:
            self.first = None
            self.last = None
            self.length -= 1
        else:
            current_node = self.first
            self.first = current_node.next
            self.length -= 1

    def print(self):
        """Prints the queue as an array."""
        queue_array = []
        if self.length == 0:
            pass
        else:
            current_node = self.first
            while current_node.next is not None:
                queue_array.append(current_node.value)
                current_node = current_node.next
            queue_array.append(current_node.value)
        print(queue_array)


my_queue = Queue()
my_queue.peek()
my_queue.enqueue('Joy')
my_queue.enqueue('Matt')
my_queue.enqueue('Pavel')
my_queue.enqueue('Samir')
my_queue.dequeue()
# my_queue.dequeue()
# my_queue.dequeue()
# my_queue.dequeue()
my_queue.print()
print(my_queue.first.value)
print(my_queue.last.value)
print(my_queue.length)
