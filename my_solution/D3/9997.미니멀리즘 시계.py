def test3(angle):
    # 1시간 당 시침이 360 / 12 = 30도 씩 전진
    # 30 / 60 -> 1분 당 0.5도씩
    minute = angle / 0.5
    hour = 0
    if minute > 60:
        hour = minute // 60
        minute %= 60

    return hour, minute


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        angle = int(input())
        answer = test3(angle)
        print(f'#{test_case} {int(answer[0])} {int(answer[1])}')


if __name__ == '__main__':
    main()
