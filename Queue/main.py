from src.queue import Queue
from src.hot_potato import hot_potato
from src.print_task import simulation

print("========= Basic Queue =========")
q = Queue()

q.enqueue(4)
q.enqueue("dog")
q.enqueue(True)
print(q.size())

print("========= Hot Potato Simulation =========")
print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))

print("========= Lab Printer Simulation =========")
for i in range(10):
    simulation(3600, 5)
