class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next_node):
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    # 제일 앞에 새로운 노드 생성
    def add(self, new_data):
        temp = Node(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, target_data):
        current = self.head
        found = False
        while current is not None and found:
            if current.get_data() == target_data:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, target_data):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == target_data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            # 제거하고자 하는 노드가 링크드리스트의 head 일
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, new_data):
        new_node = Node(new_data)
        is_tail = False
        current = self.head

        while is_tail is False:
            if current.get_next() is None:
                current.set_next(new_node)
                break

            current = current.get_next()




