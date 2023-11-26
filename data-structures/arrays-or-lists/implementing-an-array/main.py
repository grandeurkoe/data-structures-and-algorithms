class Array:
    def __init__(self):
        self.data = {}
        self.length = 0

    def display(self):
        """Display list."""
        if self.length == 0:
            print("\nArray: []")
        else:
            print(f"\nArray: {list(self.data.values())}")

    # PUSH OPERATION  # -> Big O - O(1)
    def push(self, value):
        """Append data element at the end of the list."""
        self.data[self.length] = value
        self.length += 1
        print(f"Append Value({value}).")

    # INSERT OPERATION  # -> Big O - O(n)
    def insert(self, index, value):
        """Insert data element at a given index."""
        if index < 0:
            print(f"Index[{index}] out of range[0, {self.length}).")
        elif 0 <= index <= self.length - 1:
            for copy_idx in range(self.length, index, -1):
                self.data[copy_idx] = self.data[copy_idx - 1]
            self.data[index] = value
            self.length += 1
            print(f"Insert Value({value}) at Index[{index}].")
        elif index >= self.length:
            self.push(value)

    # POP OPERATION  # -> Big O - O(1)
    def pop(self):
        """Pop data element from the end of the list."""
        if self.length == 0:
            print("No element available in Array.")
        else:
            element_to_delete = self.data[self.length - 1]
            del self.data[self.length - 1]
            self.length -= 1
            print(f"Pop Value({element_to_delete}).")

    # DELETE OPERATION -> Big O - O(n)
    def remove(self, value):
        """Remove data element by value."""
        if self.length == 0:
            print("No element available in Array.")
        else:
            if value == self.data[self.length - 1]:
                self.pop()
            elif value in self.data.values():
                element_del_idx = 0
                for idx in range(self.length):
                    if value == self.data[idx]:
                        element_del_idx = idx
                        break
                for del_idx in range(element_del_idx, self.length - 1):
                    self.data[del_idx] = self.data[del_idx + 1]
                del self.data[self.length - 1]
                self.length -= 1
                print(f"Delete Value({value}).")
            else:
                print(f"Value({value}) not available in Array.")

    # LOOKUP OPERATION
    # BY VALUE -> Big O - O(n)
    def get_index(self, value):
        """Gets the index of a given data element."""
        if self.length == 0:
            print("No element available in Array.")
        else:
            if value in self.data.values():
                value_idx = 0
                for idx in range(self.length):
                    if value == self.data[idx]:
                        value_idx = idx
                        break
                print(f"Value({value}) at Index[{value_idx}].")
            else:
                print(f"Value({value}) not available in Array.")

    # BY INDEX -> Big O - O(1)
    def get_value(self, index):
        """Get the data element at a given index."""
        if self.length == 0:
            print("No element available in Array.")
        else:
            if index in self.data.keys():
                print(f"Value({self.data[index]}) at Index[{index}].")
            else:
                print(f"Index[{index}] not available in Array.")


arr = Array()
print("\nOPERATION LOG")
arr.push(0)
arr.push(2)
arr.insert(1, 1)
arr.push(3)
arr.push(4)
arr.get_value(2)
arr.pop()
arr.remove(1)
arr.remove(2)
arr.get_index(3)
arr.pop()
arr.pop()
arr.display()
