import collections


# 추후 보강할 점: 좀 더 깔끔하게 정리 or 좀 더 쉬운 알고리즘
# BFS 로 구현할 수 있을 것 같음. 더 공부 뒤 다시 풀어보기
def test3(arr, N, K):
    result = 0
    # 가로 탐색
    for i in range(N):
        # defaultdict 으로 흰색 칸 길이 count
        len_dic = collections.defaultdict(int)
        j = 0
        # j를 1씩 추가하면서, 해당 값이 1인 arr[i][j] 찾기
        while j != N:
            if arr[i][j] == 0:
                j += 1
                continue
            # 해당 값이 1이면, range(j, N) 내 연속적으로 1인 구간 찾기 -> len_
            elif arr[i][j] == 1:
                len_ = 0
                for find_1 in range(j, N):
                    if arr[i][find_1] == 1:
                        len_ += 1
                    # 만약, 0이 나오면 break
                    else:
                        break
                # len_dic 에 값 저장
                len_dic[len_] += 1
                # j부터 j + len_ 구간까지 탐색 했으니, [i][j+len_]부터 다시 탐색
                j += len_
        # k 값과 동일한 len_dic key 값 찾고, value 값만큼 더하기
        if K in len_dic:
            result += len_dic[K]

    # 세로 탐색
    # arr[j][i]로, i와 j 값만 변경 뒤 탐색
    for i in range(N):
        len_dic = collections.defaultdict(int)
        j = 0
        while j != N:
            if arr[j][i] == 0:
                j += 1
                continue
            elif arr[j][i] == 1:
                len_ = 0
                for find_1 in range(j, N):
                    if arr[find_1][i] == 1:
                        len_ += 1
                    else:
                        break
                len_dic[len_] += 1
                j += len_

        if K in len_dic:
            result += len_dic[K]

    return result


def main():
    # 테스트 케이스
    T = int(input())

    for test_case in range(1, T + 1):
        # 변수 입력 받기
        N, K = map(int, input().split())
        arr = [list(int(x) for x in input().split()) for _ in range(N)]
        answer = test3(arr, N, K)
        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()
