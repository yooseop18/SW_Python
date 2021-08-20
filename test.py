import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashmap:
    # 초기화
    def __init__(self):
        self.size = 10000
        self.table = collections.defaultdict(ListNode)

    # put 메서드
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 예외 처리
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        p = self.table[index]
        while p:
            # 키 값이 똑같다면, 그냥 value 값을 업데이트 하고 종료
            if p.key == key:
                p.value = value
                return
            # 해시 충돌이 없다면 while 종료
            if p.next is None:
                break
            # 키 값이 다르고, 해시 충돌이 있다면 -> 연결 리스트 생성
            p = p.next

        # 연결 리스트에 새 노드 연결
        p.next = ListNode(key, value)


    def get(self, key: int) -> int:
        index = key % self.size
        # 예외 처리
        if self.table[index].value is None:
            return -1

        # 인덱스 값에 해당 되는 해시 값 출력
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next

        return -1


    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트의 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

