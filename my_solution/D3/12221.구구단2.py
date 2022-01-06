T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    result = -1
    if A < 10 and B < 10:
        result = A * B

    print(f'#{test_case} {result}')
