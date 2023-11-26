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
            print("\nDictionary = {}")
        else:
            dict_display = ""
            for mem_loc in self.data:
                if mem_loc is not None:
                    for entry_idx in range(len(mem_loc)):
                        dict_display += f"'{mem_loc[entry_idx][0]}': {mem_loc[entry_idx][1]}, "
                else:
                    pass
                dict_display = dict_display[0: -2]
                # dict_display += "}"
            print("\nDictionary = " + "{" + dict_display + "}")

    def generate_hash(self, key):
        """Generate hash value based on key. Return hash value."""
        hash_value = 0
        for char_idx in range(len(key)):
            hash_value = (hash_value + (ord(key[char_idx]) * char_idx)) % self.length
        return hash_value

    # INSERT OPERATION  # -> Big O - O(1)
    def insert(self, key, value):
        """Insert dictionary entry."""
        hash_value = self.generate_hash(key)
        if self.data[hash_value] is None:
            self.data[hash_value] = [[key, value]]
            print(f"Insert entry('{key}', {value}).")
        else:
            self.data[hash_value].append([key, value])
            print(f"Insert entry('{key}', {value}).")

    # DELETE OPERATION  # -> Big O - O(n)
    def remove(self, key):
        """Delete dictionary entry"""
        hash_value = self.generate_hash(key)
        if self.is_empty():
            print("No entries available in Dictionary.")
        else:
            for each_entry in self.data[hash_value]:
                if each_entry[0] == key:
                    print(f"Delete entry('{each_entry[0]}', {each_entry[1]})")
                    self.data[hash_value].remove(each_entry)
            if len(self.data[hash_value]) == 0:
                self.data[hash_value] = None

    def lookup(self, key):
        """Check if node exists."""
        hash_value = self.generate_hash(key)
        if self.is_empty():
            print("No entries available in Dictionary.")
        else:
            if self.data[hash_value] is not None:
                for each_entry in self.data[hash_value]:
                    if each_entry[0] == key:
                        print(f"Entry('{each_entry[0]}', {each_entry[1]}) exists.")
                        return True
                print(f"Key('{key}') doesn't exist.")
            else:
                print(f"Key('{key}') doesn't exist.")


dictionary = Dictionary(2)
print("\nOPERATION LOG")
dictionary.insert('Grapes', 10000)
dictionary.insert('Apples', 15000)
dictionary.insert('Oranges', 20000)
dictionary.lookup('k')
dictionary.lookup('Apples')
dictionary.remove('Apples')
dictionary.remove('Grapes')
dictionary.remove('Oranges')
dictionary.display()
