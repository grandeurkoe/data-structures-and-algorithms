class Stack:
    def __init__(self):
        self.data = []

    def display(self):
        """Display stack."""
        if len(self.data) == 0:
            print("\nStack:\nEmpty")
        else:
            print("\nStack:")
            print(f"{self.data[-1]} <- Top")
            for idx in range(len(self.data) - 2, -1, -1):
                print(self.data[idx])

    # PUSH OPERATION -> Big O - O(1).
    def push(self, value):
        """Add data element to the top of the stack."""
        self.data.append(value)
        print(f"Push Value({value}).")

    # POP OPERATION -> Big O - O(1).
    def pop(self):
        """Remove data element from the top of the stack"""
        if len(self.data) == 0:
            print("No elements available in Stack.")
        else:
            print(f"Pop Value({self.data[-1]}).")
            self.data.pop()

    # PEEK OPERATION -> Big O - O(1).
    def peek(self):
        """Get data element at the top of the Stack."""
        if len(self.data) == 0:
            print("No elements available in Stack.")
        else:
            print(f"Value({self.data[-1]}) is at the top of the Stack.")

    # LOOKUP OPERATION -> Big O - O(n).
    def lookup(self, value):
        """Check if data element exists."""
        if len(self.data) == 0:
            print("No elements available in Stack.")
        else:
            if value in self.data:
                print(f"Value({value}) at Index[{self.data.index(value)}].")
            else:
                print(f"Value({value}) doesn't exist.")


stack = Stack()
print("\nOPERATION LOG")
stack.push(5)
stack.push(6)
stack.push(7)
stack.pop()
stack.peek()
stack.lookup(5)
stack.pop()
stack.pop()
stack.display()
