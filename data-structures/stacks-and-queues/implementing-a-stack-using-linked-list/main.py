class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def display(self):
        """Display stack."""
        if self.bottom is None:
            print("\nNo data elements available in the Stack.")
        else:
            stack_disp = []
            current_node = self.bottom
            while current_node:
                stack_disp.append(current_node.value)
                current_node = current_node.next
            print("\nStack:")
            print(f"{stack_disp[-1]} <- Stack Top")
            for index in range(len(stack_disp) - 2, -1, -1):
                print(f"{stack_disp[index]}")

    # PUSH OPERATION
    # Time complexity or BIG(O) - O(1)
    def push(self, value):
        """Add data element to the top of the stack."""
        new_node = Node(value)
        if self.bottom is None:
            self.bottom = new_node
            self.top = self.bottom
        else:
            self.top.next = new_node
            self.top = new_node
        self.length += 1
        print(f"Push '{value}'.")

    # POP OPERATION
    # Time complexity or BIG(O) - O(1)
    def pop(self):
        """Remove data element from the top of the stack"""
        if self.bottom is None:
            print("No data elements available in the Stack.")
        else:
            element_to_delete = self.top.value
            if self.length == 1:
                self.top = None
                self.bottom = None
            else:
                current_node = self.bottom
                for _ in range(self.length - 2):
                    current_node = current_node.next
                current_node.next = None
                self.top = current_node
            print(f"Pop '{element_to_delete}'.")
            self.length -= 1

    # PEEK OPERATION
    # Time complexity or BIG(O) - O(1)
    def peek(self):
        """Get data element at the top of the Stack."""
        if self.bottom is None:
            print("No data elements available in the Stack.")
        else:
            print(f"Value({self.top.value}) is at the top of the stack.")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.peek()
stack.display()
