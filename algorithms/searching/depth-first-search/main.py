from binary_search_tree import BinarySearchTree


my_bst = BinarySearchTree()
my_bst.insert(9)
my_bst.insert(12)
my_bst.insert(6)
my_bst.insert(7)
my_bst.insert(11)
my_bst.insert(1)
my_bst.insert(45)
print(my_bst.depth_first_search_preorder())
print(my_bst.depth_first_search_inorder())
print(my_bst.depth_first_search_postorder())
