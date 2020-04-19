from hash_map import HashMap
import random

title1 = \
'''
####################### Test of Map #########################

	- creating
	- len
	- appending
	- searching by key
	- removing map

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


title2 = \
'''
\r###################### Test of Hash ########################
\r
\r	- appending
\r	- get load
\r	- get load_factor
\r  - set load_factor
\r  - compress
'''
print(title2)
lst = []

hmap = HashMap()

for i in range(100000):
	lst.append(i)

random.shuffle(lst)

print('1. Appending with private rehashing:')
print('     Len before: ', len(hmap))
print('     Appended 100000 items.')
for i in lst:
	hmap[i] = i
print('     Len after: ', len(hmap))

print('2. get load:')
print('     hmap.load = ', hmap.load)
print('3. get load factor:')
print('     hmap.load_factor = ', hmap.load_factor)
print('4. set load factor:')
hmap.load_factor = 1.8
print('     hmap.load_factor = ', hmap.load_factor)
print('5. compress:')
print('     last hmap.load = ', hmap.load)
hmap.compress()
print('     new hmap.load = ', hmap.load)
