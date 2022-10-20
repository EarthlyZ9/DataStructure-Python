"""
연구실에서 여러 대의 컴퓨터가 한 대의 프린터로 프린트 요청을 보내는 상황

- 10명의 학생이 있고, 한 시간에 두 번 프린트를 하며, 한번 프린트 할 때 1 - 20 장을 랜덤하게 함
- 즉, 한시간에 20 tasks, 1 task 3분 = 180초 에 한번 씩 발생하는 꼴
- 1 ~ 180 의 랜덤한 숫자를 뽑아 180이 나오면 print task 를 생성
"""

import random
from .queue import Queue


class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        # current task 가 있을 때 걸리는 시간에 대한 타이머를 세팅하고 타이머를 1씩 줄여나감
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            # 남은 시간이 0 이하가 되면 task 를 비움 (task 완료)
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):

        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print(
        "Average Wait %6.2f secs %3d tasks remaining."
        % (average_wait, print_queue.size())
    )


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False
