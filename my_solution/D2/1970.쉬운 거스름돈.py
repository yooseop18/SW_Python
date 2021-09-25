def test3(N):
    # 거스름돈 딕셔너리
    money = {
        50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0
    }
    # 몫이 0이 될 때 까지 각 화폐단위로 나누고 딕셔너리에 cnt 증가
    for i in money:
        while N // i != 0:
            change = N // i
            N %= i
            money[i] += change
    # values 값만 리스트로 리턴
    return list(money.values())


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        answer = test3(N)
        # 출력
        print(f'#{test_case}')
        for i in answer:
            print(i, end=" ")
        print("")


if __name__ == '__main__':
    main()
