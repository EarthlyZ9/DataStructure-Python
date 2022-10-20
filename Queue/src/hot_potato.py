from .queue import Queue

"""
수건 돌리기 예제

name_list: 참여 인원의 이름
num: 돌리는 횟수 
"""


def hot_potato(name_list, num):
    simqueue = Queue()
    for name in name_list:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            # front 의 사람이 rear 로 들어감
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()
