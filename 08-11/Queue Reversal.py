from queue import Queue
def reverse_queue(q):
    stack = []
    while not q.empty():
        stack.append(q.get())
    while stack:
        q.put(stack.pop())
def print_queue(q):
    while not q.empty():
        print(q.get(), end=" ")

N = 6
elements = [4, 3, 1, 10, 2, 6]
queue = Queue()
for element in elements:
    queue.put(element)
reverse_queue(queue)
print_queue(queue)
