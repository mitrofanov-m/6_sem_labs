from hash_map import HashMap


title1 = \
'''
####################### Test of Map #########################

	- creating
	- len
	- appending
	- searching by key
	- removing tree

'''
print(title1)

print('1. Creating:')
mmap = HashMap()
print(f'	mmap = {mmap}\n')
print('2. Appending:')
mmap[1] = "ooops"
mmap[1] = "my"
mmap[22] = "friend"
mmap[0] = "hello"
print(f"	mmap = {mmap}\n")
print('3. Len:')
print(f'	{len(mmap)}\n')

print('4. Searching by key:')
print(f"	mmap[22] = {mmap[22]}\n")
print('6. Removing first tree:')
print(f"	mmap = {mmap}")
mmap.remove_all()
print(f"	mmap = {mmap}")
