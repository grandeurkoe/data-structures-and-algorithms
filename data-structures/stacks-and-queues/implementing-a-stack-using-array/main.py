class Stack:
    def __init__(self):
        self.data = []

    def display(self):
        """Display stack."""
        if len(self.data) == 0:
            print("\nNo data elements available in the Stack.")
        else:
            print("\nStack:")
            print(f"{self.data[-1]} <- Stack Top")
            for index in range(len(self.data) - 2, -1, -1):
                print(f"{self.data[index]}")

    # PUSH OPERATION
    # Time complexity or BIG(O) - O(1)
    def push(self, value):
        """Add data element to the top of the stack."""
        self.data.append(value)
        print(f"Push '{value}'.")

    # POP OPERATION
    # Time complexity or BIG(O) - O(1)
    def pop(self):
        """Remove data element from the top of the stack"""
        if len(self.data) == 0:
            print("No data elements available in the Stack.")
        else:
            element_to_delete = self.data[-1]
            self.data.pop()
            print(f"Pop '{element_to_delete}'.")

    # PEEK OPERATION
    # Time complexity or BIG(O) - O(1)
    def peek(self):
        """Get data element at the top of the Stack."""
        if len(self.data) == 0:
            print("No data elements available in the Stack.")
        else:
            print(f"Value({self.data[-1]}) is at the top of the stack.")


stack = Stack()
stack.push(1)
stack.push(2)
stack.pop()
stack.peek()
stack.display()
