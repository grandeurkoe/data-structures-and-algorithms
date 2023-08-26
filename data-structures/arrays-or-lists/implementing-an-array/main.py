class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        """Returns the element at the passed index."""
        return self.data[index]

    def push(self, item):
        """Appends the item at the end of the Array. Returns the length of the Array."""
        self.data[len(self.data)] = item
        self.length += 1
        return self.length

    def delete(self):
        """Pops and returns the last element in the Array."""
        last_item = self.data[len(self.data) - 1]
        del self.data[len(self.data) - 1]
        self.length -= 1
        return last_item

    def delete_at_index(self, index):
        """Deletes and returns the elements at the passed index."""
        deleted_item = self.data[index]
        self.shift_items(index)
        self.length -= 1
        return deleted_item

    def shift_items(self, index):
        """Shifts elements after an elements has been deleted."""
        for shifts in range(index, len(self.data) - 1):
            self.data[shifts] = self.data[shifts + 1]
        del self.data[len(self.data) - 1]


my_array = Array()
my_array.push('Hi')
my_array.push('You')
my_array.push('!')
# my_array.delete()
# my_array.delete()
my_array.delete_at_index(1)
print(my_array.data)