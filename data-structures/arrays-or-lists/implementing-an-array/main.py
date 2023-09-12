class Array:
    def __init__(self):
        self.data = {}
        self.length = 0

    def is_empty(self):
        """Checks if list is Empty. Returns True if Empty. """
        if self.length == 0:
            return self.length == 0
        else:
            return False

    # DISPLAY OPERATION
    # Displays the array as a string.
    # Time complexity - O(n)
    def display(self):
        """Displays list as a string."""
        if not self.is_empty():
            array = "["
            for each_key in self.data:
                array += f"{self.data[each_key]},"
            array = array[:len(array) - 1]
            print(f"{array}]")
        else:
            print("[]")

    # LOOKUP OPERATION
    # To get the data element at a certain index.
    # Since python dictionaries use hash tables, lookups are faster.
    # Time complexity - O(1)
    def get_data_at_index(self, index):
        """Gets the data element at a given index. Returns the data element"""
        if not self.is_empty():
            return self.data[index]
        else:
            return "No data elements in SAMPLE."

    # To get the index of a data element.
    # Time complexity - O(n)
    def get_index(self, element):
        """Gets the index of a given data element. Returns the index."""
        if not self.is_empty():
            for each_key in self.data:
                if self.data[each_key] == element:
                    return each_key
        else:
            return "No data elements in SAMPLE."

    # INSERTION OPERATION
    # To append data element at the end of the list.
    # Time complexity - O(1)
    def push(self, element):
        """Appends data element at the end of the list."""
        self.data[f'{self.length}'] = element
        self.length += 1
        print(f'Pushed {element}.')

    # DELETION OPERATION
    # Assuming that there is no collision introduced by the hash function.
    # However, if there is collision than the time complexity can go upto O(n).
    # To delete data element from the end of the list.
    # Time complexity - O(1)
    def pop(self):
        """Pops data element at the end of the list"""
        if not self.is_empty():
            del self.data[f'{self.length - 1}']
            self.length -= 1
        else:
            return "No data elements in SAMPLE."

    # To delete data element at a given index.
    # Time complexity - O(1)
    def remove(self, index):
        """Deletes data element at a given index."""
        if not self.is_empty():
            del self.data[f'{index}']
            self.length -= 1
        else:
            return "No data elements in SAMPLE."


sample = Array()
sample.push('a')
sample.push('b')
sample.push('c')
sample.push('d')
sample.pop()
sample.remove(1)
sample.display()
