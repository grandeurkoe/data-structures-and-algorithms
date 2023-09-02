from binary_search_tree import BinarySearchTree


my_bst = BinarySearchTree()
my_bst.insert(9)
my_bst.insert(12)
my_bst.insert(6)
my_bst.insert(7)
my_bst.insert(11)
my_bst.insert(1)
my_bst.insert(45)
print(my_bst.breadth_first_search_recursive([my_bst.root], [my_bst.root.value]))
