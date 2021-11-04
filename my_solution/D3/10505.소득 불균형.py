def test3(N, arr):
    avg = 0
    cnt = 0
    for i in arr:
        avg += i
    avg /= N

    for i in arr:
        if i <= avg:
            cnt += 1
    return cnt


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        arr = [int(x) for x in input().split()]
        answer = test3(N, arr)
        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()
