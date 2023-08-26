class HashTable:
    def __init__(self, size):
        """Creates a hash table of given size."""
        self.data = [None for _ in range(size)]
        self.length = size

    def hash_key(self, key):
        """Generates a hash key. Returns a hash key."""
        hashes = 0
        for i in range(len(key)):
            hashes = (hashes + ord(key[i]) * i) % self.length
        return hashes

    def set(self, key, value):
        """Generates a hash key entry based on the (key,value) provided."""
        address = self.hash_key(key)
        if self.data[address] is None:
            self.data[address] = []

        self.data[address] += [[key, value]]

    def get(self, key):
        """Prints the (key,value) pair based on the key provided."""
        address = self.hash_key(key)
        if self.data[address] is None:
            print(f"Value for '{key}' does not exist.")
        else:
            for item in self.data[address]:
                if key == item[0]:
                    print(item)

    def keys(self):
        """Prints all the keys available in the hash table."""
        my_keys = []
        for element in self.data:
            if element is not None:
                for item in element:
                    my_keys.append(item[0])

        print(my_keys)


my_hash_table = HashTable(2)
my_hash_table.set('grapes', 10000)
my_hash_table.set('apples', 15000)
my_hash_table.set('oranges', 20000)
my_hash_table.get('oranges')
my_hash_table.keys()
