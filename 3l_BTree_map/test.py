from btree import Btree


tree = Btree(t=3)
tree.insert(5)
tree.insert(10)
tree.insert(1)
tree.insert(1)
tree.insert(3)
tree.insert(4)
tree.insert(7)
tree.insert(8)
tree.insert(4)
# print(tree._root.keys)
print(tree._root.leaf)
print(tree)
print(len(tree))