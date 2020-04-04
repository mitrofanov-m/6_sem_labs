from btree import Btree


tree = Btree(t=2)
tree.insert(5)
tree.insert(10)
tree.insert(1)
tree.insert(1)

print(tree._root.keys)