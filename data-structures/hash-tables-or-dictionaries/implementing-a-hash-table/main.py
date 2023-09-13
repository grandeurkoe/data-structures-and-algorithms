class Dictionary:
    def __init__(self, size):
        """Generates a hash table of fixed size."""
        self.data = [None for _ in range(size)]
        self.length = size

    def show_dictionary(self):
        """Shows all entries in the hash table."""
        print(self.data)

    def is_empty(self):
        """Checks if hash table is empty."""
        for each_entry in self.data:
            if each_entry is not None:
                return False
        return True

    def generate_hash_for(self, key):
        """Generates a hash value for a given key. Returns hash value."""
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % self.length
        return hash_value

    # LOOKUP OPERATION
    # To get the value of a dictionary entry based on the key provided.
    def get_entry(self, key):
        """Gets a (key, value) entry from the hash table."""
        hash_value = self.generate_hash_for(key)
        if self.data[hash_value] is None:
            print(f"{key} key doesn't exist.")
        else:
            for each_entry in self.data[hash_value]:
                if each_entry[0] == key:
                    print(each_entry)
                    return True
            print(f"{key} key doesn't exist.")

            # INSERTION OPERATION

    # To insert entries into a dictionary.
    def insert(self, key, value):
        """Inserts a (key, value) entry into a hash table."""
        hash_value = self.generate_hash_for(key)
        if self.data[hash_value] is None:
            self.data[hash_value] = []
        self.data[hash_value].append([key, value])
        print(f"Pushed ['{key}', {value}].")

    # DELETION OPERATION
    # To delete entries from dictionary.
    def remove(self, key):
        """Removes a (key, value) entry into a hash table."""
        hash_value = self.generate_hash_for(key)
        if not self.is_empty():
            if self.data[hash_value] is None:
                print(f"'{key}' key doesn't exist.")
            else:
                for each_entry in range(len(self.data[hash_value])):
                    if self.data[hash_value][each_entry][0] == key:
                        print(f"Popped {self.data[hash_value][each_entry]}")
                        del self.data[hash_value][each_entry]
                        if len(self.data[hash_value]) == 0:
                            self.data[hash_value] = None
                        return True
                print(f"'{key}' key doesn't exist.")


sample = Dictionary(2)
sample.insert('grapes', 10000)
sample.insert('apples', 15000)
sample.insert('oranges', 20000)
sample.remove('apples')
sample.show_dictionary()
