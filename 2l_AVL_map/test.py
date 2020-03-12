from AVLTree import *
from Map import Map


print("\n------- Test Tree --------\n")

avltree = AVLTree()
bintree = BinaryTree()
values = [0, 5, 6, 7, 8, 9, -1]

for value in values:
    avltree.insert(value)
    bintree.insert(value)

print("AVL tree:", avltree, sep='\n')
print("Binary tree:", bintree, sep='\n')
avltree.remove(7)
bintree.remove(7)
print("Remove value = 7:")
print("AVL tree:", avltree, sep='\n')
print("Binary tree:", bintree, sep='\n')

print(f"\nLen of AVL tree is: {len(avltree)}")
print(f"Binary tree contains value = 0 : {0 in bintree}")


print("\n\n------- Test Map --------\n")

mmap = Map()
mmap[1] = "my"
mmap[2] = "friend"
mmap[0] = "hello"

del mmap[0]
print(f"mmap = {mmap}")
print(f"mmap[2] = {mmap[2]}")
