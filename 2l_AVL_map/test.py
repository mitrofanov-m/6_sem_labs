from AVLTree import *
from Map import Map
tree = AVLTree()
tree.insert(0)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.insert(-1)
print(tree)

tree.remove(7)
print(tree)
print(f"Len of tree is: {len(tree)}")
print(f"Tree contains value = 0 : {0 in tree}")
print("---------------" + "\n")
for i in tree:
    print(i)


mmap = Map()

mmap[1] = "my"
# print(mmap._Map__VALTYPE)
mmap[2] = "friend"
mmap[0] = "hello"

del mmap[0]
inorder = []
for i in mmap:
    inorder.append(i)

print(inorder)