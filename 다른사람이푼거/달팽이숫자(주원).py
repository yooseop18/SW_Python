def make_matrix(n):
    # 공갈 행렬 생성용 함수

    matrix = [[0 for i in range(n)] for j in range(n)]

    return matrix


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())  # 개수 입력
    print('#%d' % test_case)

    # 여기는 for문으로 달팽이 만들기전에 선언할 변수들
    n = N
    mat = make_matrix(N)  # 공갈 행렬 생성
    print(mat)
    r = 0
    c = -1
    count = 1
    alt = 1
    # 여기까지

    while n > 0:
        for i in range(n):
            # column 방향으로 진행하면서 달팽이 만드는 반복문
            c += alt
            mat[r][c] = count
            count += 1

        n -= 1
        for i in range(n):
            # row 방향으로 진행하면서 달팽이 만드는 반복문
            r += alt
            mat[r][c] = count
            count += 1

        alt *= -1  # 달팽이의 진행방향이 반대로 향햐도록 하는 부분

    for i in range(N):
        for j in range(N):
            print(mat[i][j], end=" ")
        print()