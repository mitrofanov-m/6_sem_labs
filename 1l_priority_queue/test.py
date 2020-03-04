from priority_queue import PriorityQueue


q = PriorityQueue((5, 100, -10, 33, 12))
print("\nCreate an interger priority queue:")
print(f"> {q}")
try:
    to_push = 1
    print(f"Pushing integer {to_push}:")
    q.push(1)
    print(f"> {q}")
    to_push = "Oops!"
    print(f"Pushing another type value '{to_push}':")
    q.push(to_push)
except TypeError as err:
    print(err.args[0])

any_q = PriorityQueue()
print("\nCreate an optional type priority queue:")
print(f"> {any_q}")
print(f"Type of queue is: {any_q.get_type()}")
print(f"Appending float value:")
any_q.push(3.45)
print(f"> {any_q}")
print(f"Type of queue is: {any_q.get_type()}")
