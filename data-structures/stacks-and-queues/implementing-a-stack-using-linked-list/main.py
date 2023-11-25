class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = self.top
        self.length = 0

    def display(self):
        """Display stack."""
        if self.length == 0:
            print("\nStack:\nEmpty")
        else:
            disp_stack = []
            current_node = self.bottom
            while current_node:
                disp_stack.append(current_node.value)
                current_node = current_node.next
            print("\nStack:")
            print(f"{disp_stack[-1]} <- Top")
            for idx in range(len(disp_stack) - 2, -1, -1):
                print(disp_stack[idx])

    # PUSH OPERATION -> Big O - O(1).
    def push(self, value):
        """Add data element to the top of the stack."""
        new_node = Node(value)
        if self.length == 0:
            self.bottom = new_node
            self.top = self.bottom
        else:
            self.top.next = new_node
            self.top = new_node
        self.length += 1
        print(f"Push Node({value}).")

    # POP OPERATION -> Big O - O(n).
    def pop(self):
        """Remove data element from the top of the stack"""
        if self.length == 0:
            print("No nodes available in Stack.")
        elif self.length == 1:
            print(f"Pop Node({self.top.value}).")
            self.top = None
            self.bottom = None
            self.length -= 1
        else:
            print(f"Pop Node({self.top.value}).")
            current_node = self.bottom
            for _ in range(self.length - 2):
                current_node = current_node.next
            current_node.next = None
            self.top = current_node
            self.length -= 1

    # PEEK OPERATION -> Big O - O(1).
    def peek(self):
        """Get data element at the top of the Stack."""
        if self.length == 0:
            print("No nodes available in Stack.")
        else:
            print(f"Node({self.top.value}) at the top of the Stack.")

    # LOOKUP OPERATION -> Big O - O(n).
    def lookup(self, value):
        """Check if data element exists."""
        if self.length == 0:
            print("No nodes available in Stack.")
        else:
            current_node = self.bottom
            while current_node:
                if current_node.value == value:
                    print(f"Node({value}) exists.")
                    return None
                current_node = current_node.next
            print(f"Node({value}) doesn't exist.")


stack = Stack()
print("\nOPERATION LOG")
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.pop()
stack.peek()
stack.lookup(10)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.display()
