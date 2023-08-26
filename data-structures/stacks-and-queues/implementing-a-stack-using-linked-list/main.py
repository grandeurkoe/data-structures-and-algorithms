class Node:
    def __init__(self, value):
        """Creates an empty node."""
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        """Creates an empty stack."""
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        """Prints the top node in the stack."""
        if self.length == 0:
            print(None)
        else:
            print(self.top.value)

    def push(self, value):
        """Adds a node to the top of the stack."""
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            current_node = self.bottom
            for _ in range(self.length - 1):
                current_node = current_node.next
            self.top = new_node
            current_node.next = new_node
        self.length += 1

    def pop(self):
        """Removes a node from the top of the stack."""
        if self.length == 0:
            print("Stack is Empty! No element deleted.")
        elif self.top == self.bottom:
            self.bottom = None
            self.top = None
            self.length = 0
        else:
            current_node = self.bottom
            for _ in range(self.length - 2):
                current_node = current_node.next
            current_node.next = None
            self.top = current_node
            self.length -= 1

    def print(self):
        """Prints the stack as an array."""
        stack_array = []
        current_node = self.bottom
        traverse_var = 0
        while traverse_var != self.length:
            stack_array.append(current_node.value)
            current_node = current_node.next
            traverse_var += 1
        print(stack_array)


my_stack = Stack()
my_stack.peek()
my_stack.push('Google')
my_stack.push('Udemy')
my_stack.push('Discord')
my_stack.pop()
my_stack.pop()
my_stack.print()
