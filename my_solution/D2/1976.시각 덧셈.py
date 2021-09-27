def test3(arr):
    # 두 시간을 더하기
    hour = arr[0] + arr[2]
    time = arr[1] + arr[3]
    # 분이 60분이 넘어가면, 시간에 더해주고 분-60
    if time > 60:
        time -= 60
        hour += 1
    # 12시간 체계로 만들기
    if hour // 12 != 0:
        hour %= 12
    # 예외처리 : 0시 -> 12시
    if hour == 0:
        hour = 12

    return hour, time


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        arr = [int(x) for x in input().split()]
        answer = test3(arr)
        print(f'#{test_case} {answer[0]} {answer[1]}')


if __name__ == '__main__':
    main()
