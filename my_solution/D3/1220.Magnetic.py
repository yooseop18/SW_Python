def test3(N, arr):
    cnt = 0
    # 1 : N, 2 : S 성분
    # 아래는 S극, 위는 N극

    # 새로운 리스트 만들어서, 0 빼고 전부 삽입 -> 그러면 전부 연결됨
    # 리스트 길이가 1이면 버려, 2 이상인 경우!

    for j in range(N):
        # 0 빼고 새로운 리스트에 숫자 넣음
        new_arr = []
        for i in range(N):
            if arr[i][j] != 0:
                new_arr.append(arr[i][j])
        # 길이가 1이면 버림
        if len(new_arr) <= 1:
            continue
        # 맨 앞 숫자 2이면 버리고, 맨 뒤 숫자 1이면 버림
        while True:
            if new_arr[0] == 2:
                new_arr.pop(0)

            elif new_arr[-1] == 1:
                new_arr.pop()

            else:
                break
        # 교착상태 카운트
        for k in range(len(new_arr) - 1):
            if new_arr[k] == 1 and new_arr[k] != new_arr[k + 1]:
                cnt += 1

    return cnt


def main():
    for test_case in range(1, 11):
        N = int(input())
        arr = [list(int(x) for x in input().split()) for _ in range(N)]
        answer = test3(N, arr)
        print(f'#{test_case} {answer}')


main()
