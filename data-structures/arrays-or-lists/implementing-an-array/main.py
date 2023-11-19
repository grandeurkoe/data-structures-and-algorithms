class Array:
    def __init__(self):
        self.data = {}
        self.length = 0

    def display(self):
        """Display list."""
        print(f"\nList: {list(self.data.values())}\n")

    # LOOKUP OPERATION
    # Time complexity or BIG(O) - O(n)
    def get_index(self, value):
        """Gets the index of a given data element. Returns the index."""
        if value in self.data.values():
            for index in range(self.length):
                if self.data[index] == value:
                    print(f"Value('{value}') at Index[{index}].")
                    return index
        else:
            print(f"Value('{value}') doesn't exist.")

    # Time complexity or BIG(O) - O(1)
    def get_value_by_index(self, index):
        """Get the data element at a given index."""
        if index < self.length:
            print(f"Value('{self.data[index]}') at Index[{index}].")
        else:
            print(f"Index('{index}') doesn't exist.")

    # PUSH OPERATION
    # Time complexity or BIG(O) - O(1)
    def push(self, value):
        """Append data element at the end of the list."""
        self.data[self.length] = value
        self.length += 1
        print(f"Push '{value}'.")

    # POP OPERATION
    # Time complexity or BIG(O) - O(1)
    def pop(self):
        """Pop data element from the end of the list."""
        if self.length == 0:
            print(f"No data elements available in the list.")
        else:
            element_to_delete = self.data[self.length - 1]
            del self.data[self.length - 1]
            self.length -= 1
            print(f"Pop '{element_to_delete}'.")

    # INSERT OPERATION
    # Time complexity or BIG(O) - O(n)
    def insert(self, index, value):
        """Insert data element at a given index."""
        if index >= self.length:
            self.push(value)
        else:
            if index in self.data:
                for key in range(self.length, index, -1):
                    self.data[key] = self.data[key - 1]
                self.data[index] = value
        self.length += 1
        print(f"Insert '{value}' at Index[{index}].")

    # DELETE OPERATION
    # Time complexity or BIG(O) - O(n)
    def remove_by_index(self, index):
        """Remove data element at a given index."""
        if index == self.length - 1:
            self.pop()
        elif 0 <= index < self.length - 1:
            for key in range(index, self.length - 1):
                self.data[key] = self.data[key + 1]
            del self.data[self.length - 1]
            self.length -= 1
            print(f"Delete element at Index[{index}].")
        else:
            print(f"No element at Index[{index}].")

    def remove_by_value(self, value):
        """Remove data element by value."""
        if self.length == 0:
            print(f"No data elements available in the list.")
        else:
            if value in self.data.values():
                element_idx = self.get_index(value)
                self.remove_by_index(element_idx)
            else:
                print(f"Value('{value}') doesn't exist.")


arr = Array()
arr.push('a')
arr.push('b')
arr.push('c')
arr.push('d')
arr.pop()
arr.insert(0, 'a')
arr.remove_by_index(0)
arr.remove_by_value('a')
arr.get_index('c')
arr.get_value_by_index(0)
arr.display()
print(arr.data)
