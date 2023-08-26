LINKED_LIST_ARRAY = []


class LinkedList:
    def __init__(self, value):
        """Creates an empty singly linked list."""
        self.head = {
            'value': value,
            'next': None,
        }
        self.tail = self.head
        self.length = 1

    def append(self, add_value_end):
        """Adds a node at the end of the singly linked list."""
        node = {
            'value': add_value_end,
            'next': None,
        }
        self.tail['next'] = node
        self.tail = node
        self.length += 1

    def prepend(self, add_value_start):
        """Adds a node at the beginning of the singly linked list."""
        node = {'value': add_value_start, 'next': self.head}
        self.head = node
        self.length += 1

    def printlist(self):
        """Prints the singly linked list as an array."""
        linked_list_array = []
        current_node = self.head
        while current_node is not None:
            linked_list_array.append(current_node['value'])
            current_node = current_node['next']
        print(linked_list_array)

    def insert(self, index, value_insert):
        """Adds a node at the given index in the singly linked list."""
        if index == 0:
            self.prepend(value_insert)
        elif index >= self.length:
            self.append(value_insert)
        else:
            node = {
                'value': value_insert,
                'next': None,
            }
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node['next']
            node['next'] = current_node['next']
            current_node['next'] = node
            self.length += 1

    def remove(self, index):
        """Removes a node at the given index in the singly linked list."""
        if index == 0:
            self.head['value'] = self.head['next']['value']
            self.head['next'] = self.head['next']['next']
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
            self.length -= 1

        # def reverse_linked_list(self, reverse_linked_list_array):
        #     self.head = self.tail
        #     for i in range(1, len(reverse_linked_list_array)):
        #         self.append(reverse_linked_list_array[i])
        #     return reverse_linked_list_array
        # OR
    def reverse_linked_list(self):
        """Reverses the singly linked list. Returns the singly linked list."""
        global LINKED_LIST_ARRAY
        if self.length == 1:
            return self.head
        else:
            first = self.head
            self.tail = self.head
            second = first['next']
            while second:
                temp = second['next']
                second['next'] = first
                first = second
                second = temp
            self.head['next'] = None
            self.head = first
        return self.printlist()


my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(1)
my_linked_list.insert(2, 99)
my_linked_list.remove(4)
my_linked_list.printlist()
print(my_linked_list.reverse_linked_list())
print(my_linked_list.head)
