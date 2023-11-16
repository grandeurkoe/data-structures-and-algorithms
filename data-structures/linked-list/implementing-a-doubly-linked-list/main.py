class DoublyLinkedList:
    def __init__(self, value):
        """Creates an empty doubly linked list."""
        self.head = {
            'value': value,
            'next': None,
            'previous': None,
        }
        self.tail = self.head
        self.length = 1

    def append(self, add_value_end):
        """Adds a node at the end of the doubly linked list."""
        node = {'value': add_value_end, 'next': None, 'previous': self.tail}
        self.tail['next'] = node
        self.tail = node
        self.length += 1

    def prepend(self, add_value_start):
        """Adds a node at the beginning of the doubly linked list."""
        node = {'value': add_value_start, 'next': self.head, 'previous': None}
        self.head['previous'] = node
        self.head = node
        self.length += 1

    def printlist(self):
        """Prints the doubly linked list as an array."""
        linked_list_array = []
        current_node = self.head
        while current_node is not None:
            linked_list_array.append(current_node['value'])
            current_node = current_node['next']
        print(linked_list_array)

    def insert(self, index, value_insert):
        """Adds a node at the given index in the doubly linked list."""
        if index == 0:
            self.prepend(value_insert)
        elif index >= self.length:
            self.append(value_insert)
        else:
            node = {
                'value': value_insert,
                'next': None,
                'previous': None
            }
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node['next']
            node['next'] = current_node['next']
            node['previous'] = current_node
            current_node['next'] = node
            node['next']['previous'] = node
            self.length += 1

    def remove(self, index):
        """Removes a node at the given index in the doubly linked list."""
        if index == 0:
            self.head['value'] = self.head['next']['value']
            self.head['next'] = self.head['next']['next']
            if self.head['next'] is not None:
                self.head['next']['previous'] = self.head
            else:
                self.tail = self.head
            self.length -= 1
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node['next']
            if index == self.length - 1:
                current_node['next'] = None
                self.tail = current_node
            else:
                current_node['next'] = current_node['next']['next']
                current_node['next']['previous'] = current_node
            self.length -= 1


my_linked_list = DoublyLinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(1)
my_linked_list.insert(2, 99)
my_linked_list.remove(2)
my_linked_list.printlist()
print(my_linked_list.head)
print(my_linked_list.tail)
