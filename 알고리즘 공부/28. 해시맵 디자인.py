# 개별 체이닝 방식. test.py에 구현
from test import MyHashmap


def main():
    H = MyHashmap()

    H.put(1, 100)
    H.put(2, 100)
    H.put(3, 100)
    answer1 = H.get(1)
    answer2 = H.get(2)
    answer3 = H.get(3)

    print(answer1)
    print(answer2)
    print(answer3)

    H.remove(2)


if __name__ == '__main__':
    main()
