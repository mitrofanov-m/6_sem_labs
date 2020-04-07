from Btree import Btree
from Map import Map
from math import log
import random

def testing(tree, lst):
	theorem_result = log((len(tree) + 1)/2, tree._t)
	
	theorem = \
	f'''
	t = {tree._t}
	Len of tree = {len(tree)}
	Height of tree = {tree._height}
	By the tree height theorem:
		height ≤ log_t[(n + 1) / 2]
		log(({len(tree)} + 1)/2, {tree._t}) = {round(theorem_result, 2)}
		{tree._height} ≤ {round(theorem_result, 2)}
		{tree._height <= round(theorem_result, 2)}'''
	
	print(theorem)
	check_lst = []
	for i in tree:
		check_lst.append(i)
	
	lst.sort()
	for i in range(len(lst)):
		if lst[i] != check_lst[i]:
			print("Different\n\n")
			break
	else:
		print('	Lists sorted by tree and sort method equals\n\n')



title1 = \
'''
#################### Test of Btree Map ######################
	
	- Tree test		
	- Map test

'''
print(title1)

def tree_test():
	title2 = \
	'''
	\r###################### Test of Tree ########################
	\r		
	\r	- in order appending
	\r	- reverse order appending
	\r	- random appending
	\r
	'''
	print(title2)
	
	print('1. In Order: ')
	t = 50
	tree = Btree(t)
	lst = []
	for i in range(1000000):
		tree.insert(i)
		lst.append(i)
	
	testing(tree, lst)
	
	
	print('2. Reverse Order: ')
	
	tree.remove_all()
	lst = []
	
	for i in range(1000000, 0, -1):
		tree.insert(i)
		lst.append(i)
	
	testing(tree, lst)
	
	print('3. Random Order: ')
	
	tree.remove_all()
	lst = []
	
	for i in range(1000000):
		lst.append(i)
	
	random.shuffle(lst)
	
	for i in lst:
		tree.insert(i)
	
	testing(tree, lst)

tree_test()

title3 = \
'''
####################### Test of Map #########################

	- creating
	- is empty
	- appending
	- copy tree
	- searching by key
	- removing tree

'''
print(title3)

print('1. Creating:')
mmap = Map()
print(f'	mmap = {mmap}\n')
print('2. Is empty:')
print(f'	{mmap.is_empty()}\n')

mmap[1] = "ooops"
mmap[1] = "my"
mmap[22] = "friend"
mmap[0] = "hello"

print('3. Appending:')
print(f"	mmap = {mmap}\n")
print('4. Copy tree:')
another_mmap = Map(last_map=mmap)
print(f'	another_mmap = {another_mmap}\n')
print('5. Searching by key:')
print(f"	another_mmap[22] = {another_mmap[22]}\n")
print('6. Removing first tree:')
mmap.remove_all()
print(f"	mmap = {mmap}")
print(f'	another_mmap = {another_mmap}\n')

