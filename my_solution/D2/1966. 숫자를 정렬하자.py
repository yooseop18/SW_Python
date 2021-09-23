def test3(arr):
    arr.sort()
    return arr


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        arr = [int(x) for x in input().split()]
        answer = test3(arr)

        print(f'#{test_case}', end=" ")
        for i in answer:
            print(f'{i}', end=" ")
        print("")


if __name__ == '__main__':
    main()
