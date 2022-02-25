T = int(input())

for test_case in range(1, T + 1):
    num_len = int(input())
    arr = [int(x) for x in input().split()]
    cnt = 0

    for i in range(1, num_len - 1):
        if arr[i-1] < arr[i] < arr[i + 1] or arr[i + 1] < arr[i] < arr[i - 1]:
            cnt += 1

    print(f'#{test_case} {cnt}')
