def test3(N, arr):
    selling_date = arr[-1]
    profit = 0
    for i in range(N - 2, -1, -1):
        if arr[i] < selling_date:
            profit += (selling_date - arr[i])
        else:
            selling_date = arr[i]

    return profit


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        arr = [int(x) for x in input().split()]
        answer = test3(N, arr)
        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()
