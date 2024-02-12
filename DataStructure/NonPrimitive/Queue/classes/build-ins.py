from collections import deque

queue = deque(maxlen=3)
queue.append(1)
# print(queue)

import queue as q

queue = q.Queue(maxsize=3)
queue.put(1)
queue.put(2)
# print(queue.qsize)

from multiprocessing import Queue

queue = Queue(maxsize=3)
queue.put(1)
queue.put(2)
print(queue.get())
