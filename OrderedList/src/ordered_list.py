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


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()

        return count

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
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def search(self, target_data):
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.get_data() == target_data:
                found = True
            else:
                if current.get_data() > target_data:
                    # target_data 를 찾지 못한 상태에서 current data 가 찾고자 하는 data 보다 클 때
                    # 이후 뒤를 탐색해도 없을 것이기 때문에 (ordered list) stop 한다
                    stop = True
                else:
                    current = current.get_next()

        return found

    # head 쪽에 노드 추가
    def add(self, new_data):
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.get_data() > new_data:
                stop = True
            else:
                previous = current
                current = current.get_next()

        new_node = Node(new_data)

        if previous is None:
            # 요소가 하나 밖에 없는 리스트일 때
            new_node.set_next(self.head)
            self.head = new_node
        else:
            new_node.set_next(current)
            previous.set_next(new_node)





