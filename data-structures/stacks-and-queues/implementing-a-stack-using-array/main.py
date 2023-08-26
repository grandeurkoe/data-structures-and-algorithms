class Node:
    def __init__(self, value):
        """Creates an empty node."""
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        """Creates an empty stack."""
        self.array = []

    def peek(self):
        """Prints the top node in the stack."""
        if len(self.array) == 0:
            print([])
        else:
            print(self.array[-1])

    def push(self, value):
        """Adds a node to the top of the stack."""
        self.array.append(value)

    def pop(self):
        """Removes a node from the top of the stack."""
        self.array.pop()

    def print(self):
        """Prints the stack as an array."""
        print(self.array)


my_stack = Stack()
my_stack.peek()
my_stack.push('Google')
my_stack.push('Udemy')
my_stack.push('Discord')
my_stack.pop()
# my_stack.pop()
# my_stack.pop()
my_stack.peek()
my_stack.print()
