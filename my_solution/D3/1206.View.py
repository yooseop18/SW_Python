def test3(N, arr):
    cnt = 0
    for i in range(2, N - 2):
        new_arr = []
        # 새로운 배열 만들어서 arr[i](중앙 값) 기준 좌우 2칸 넣기
        for num in range(-2, 3):
            new_arr.append(arr[i - num])
        # 중앙 값이 최대값이 아니거나 중앙 값과 중복값이 있으면 배제
        if new_arr[2] is not max(new_arr) or new_arr.count(new_arr[2]) >= 2:
            continue

        # arr[i] 과 나머지 값 차이 중 가장 작은 값이 조망권 확보 세대
        center_val = new_arr.pop(2)
        find_min_arr = []
        for k in new_arr:
            find_min_arr.append(center_val - k)
        # cnt 값에 갱신
        cnt += min(find_min_arr)

    return cnt


def main():
    for test_case in range(1, 11):
        N = int(input())
        arr = [int(x) for x in input().split()]
        answer = test3(N, arr)
        print(f'#{test_case} {answer}')


main()
