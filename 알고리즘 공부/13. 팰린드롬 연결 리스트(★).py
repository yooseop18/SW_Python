# 문제에는 main() 함수가 나와있지 않아서, 직접 main() 함수까지 구현
# 입력은 배열로 받지만, def is_(: ListNode)임
# arr -> ListNode 로 바꾸는 과정 구현

# ListNode 만들기
class ListNode:
    # None 은 미입력시, None 값으로 됨
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ListNode 로 입력받아 팰린드롬 여부 확인
def is_palindrome(head: ListNode) -> bool:
    q: list = []

    # 예외처리; 입력값이 ListNode 가 아닐 때,
    if not head:
        return -1
    # input 값이 하나 일 때,
    if head.val is None:
        return -1

    node = head

    # input_: ListNode -> q: list
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


# 입력값을 ListNode 로 바꾸기
def arr_to_ListNode(arr: list) -> ListNode:
    # 입력값이 하나 일 때, None 으로 return
    if len(arr) == 1:
        return ListNode(None)

    L = ListNode()

    L.val = arr[0]
    L.next = ListNode(arr[1])
    q = L.next
    '''
    q.val = arr[1]
    q.next = ListNode(arr[2])
    q = q.next

    q.val = arr[2]
    q.next = ListNode(arr[3])
    q = q.next

    '''
    for i in range(1, len(arr) - 1):
        q.val = arr[i]
        q.next = ListNode(arr[i + 1])
        q = q.next

    return L


def main():
    input_ = [int(x) for x in input().split()]

    list_node = arr_to_ListNode(input_)
    answer = is_palindrome(list_node)

    if answer != -1:
        print(answer)
    else:
        print("error!")


if __name__ == '__main__':
    main()


