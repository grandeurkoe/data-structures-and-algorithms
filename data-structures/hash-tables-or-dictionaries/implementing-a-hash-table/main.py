class Dictionary:
    def __init__(self, size):
        """Generate a hash table of fixed memory size."""
        self.data = [None for _ in range(size)]
        self.length = size

    def is_empty(self):
        """Check if dictionary is empty. Return True if empty else False."""
        for entry in self.data:
            if entry is not None:
                return False
        return True

    def display(self):
        """Display dictionary."""
        if self.is_empty():
            print("\nDictionary: {}")
        else:
            dict_string = "\nDictionary: {"
            for entry in self.data:
                if entry is None:
                    pass
                else:
                    for pair in entry:
                        dict_string += f"'{pair[0]}': {pair[1]}, "
            dict_string = dict_string[:len(dict_string) - 2]
            print(f"{dict_string}" + "}")

    def generate_hash(self, key):
        """Generate hash value based on key. Return hash value."""
        hash_value = 0
        for char_idx in range(len(key)):
            hash_value = (hash_value + ord(key[char_idx]) * char_idx) % self.length
        return hash_value

    def entry_exist(self, hash_value, key):
        """Check if dictionary entry exists. Return True if exists else return False."""
        for entry in self.data[hash_value]:
            if key == entry[0]:
                return True
        return False

    # LOOKUP OPERATION
    # Time complexity or BIG(O) - O(n)
    def get_entry(self, key):
        if self.is_empty():
            print("No entries in dictionary.")
        else:
            hash_value = self.generate_hash(key)
            if self.entry_exist(hash_value, key):
                for entry in self.data[hash_value]:
                    if key == entry[0]:
                        print(f"Lookup ({entry[0]}, {entry[1]}).")
            else:
                print(f"Key('{key}') doesn't exist.")

    # INSERT OPERATION
    # Insert entries into a dictionary.
    # Time complexity or BIG(O) - O(1)
    def insert(self, key, value):
        """Insert dictionary entry."""
        hash_value = self.generate_hash(key)
        if self.data[hash_value] is None:
            self.data[hash_value] = []

        self.data[hash_value].append([key, value])
        print(f"Insert ({key}, {value}).")

    # DELETE OPERATION
    # Remove entries from dictionary.
    # Time complexity or BIG(O) - O(n)
    def delete(self, key):
        """Delete dictionary entry"""
        if self.is_empty():
            print("No entries in dictionary.")
        else:
            del_idx = 0
            hash_value = self.generate_hash(key)
            if self.entry_exist(hash_value, key):
                for entry_idx in range(len(self.data[hash_value])):
                    if key == self.data[hash_value][entry_idx][0]:
                        del_idx = entry_idx
                print(f"Delete ({self.data[hash_value][del_idx][0]}, {self.data[hash_value][entry_idx][1]}).")
                self.data[hash_value].pop(del_idx)

                if len(self.data[hash_value]) == 0:
                    self.data[hash_value] = None


my_dict = Dictionary(2)
my_dict.insert('grapes', 10000)
my_dict.insert('apples', 15000)
my_dict.insert('oranges', 20000)
my_dict.get_entry('grapes')
my_dict.delete('grapes')
my_dict.delete('apples')
my_dict.delete('oranges')
my_dict.get_entry('grapes')
my_dict.display()
