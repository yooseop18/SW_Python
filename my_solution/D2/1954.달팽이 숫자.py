def test3(N: int) -> list[int]:
    def snail_arr(num, start):
        check_arr = []
        for element in arr:
            check_arr += element

        if -1 not in check_arr:
            return -1

        current_i = start
        current_j = start

        for j in range(start, len(arr[0]) - start):

            current_j = j
            if arr[start][j] != -1:
                pass
            else:
                arr[start][j] = num
                num += 1

        for i in range(start, len(arr) - start):

            current_i = i
            if arr[i][current_j] != -1:
                pass
            else:
                arr[i][current_j] = num
                num += 1

        for j in range(current_j, start-1, -1):

            current_j = j
            if arr[current_i][j] != -1:
                pass
            else:
                arr[current_i][j] = num
                num += 1

        for i in range(current_i, start-1, -1):

            if arr[i][current_j] != -1:
                pass
            else:
                arr[i][current_j] = num
                num += 1

        return num

    # N = 입력한 배열 차원 수 (NxN), num = 달팽이 배열 내 들어갈 숫자, result = 리턴 값
    arr = []
    num = 1
    result = []

    # [N][N] 배열 만들고 -1 초기값 넣기
    for _ in range(N):
        arr.append([])

    for i in range(N):
        while len(arr[i]) != N:
            arr[i].append(-1)

    # arr 배열에서 달팽이 숫자 순으로 정렬
    start = 0
    while True:
        num = snail_arr(num, start)
        start += 1
        if num == -1:
            break


    # result: list 에 결과 값 삽입
    for i in range(N):
        for j in range(len(arr[i])):
            result.append(arr[i][j])

    return result


T = int(input())

for test_case in range(1, T + 1):

    input_ = int(input())
    answer = test3(input_)

    print(f'#{test_case}')
    for i in range(len(answer)):
        print(f'{answer[i]}', end=" ")
        if (i + 1) % input_ == 0 and (i + 1) >= input_:
            print()



