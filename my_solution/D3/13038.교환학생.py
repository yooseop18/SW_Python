def test3(n, day):
    min_date = 10**6

    for _ in range(7):
        total_date = 0
        val_date = 0
        while val_date != n:
            for i in day:
                total_date += 1
                if i == 1:
                    val_date += 1
                if val_date == n:
                    break

        if total_date < min_date:
            min_date = total_date

        day.append(day.pop(0))

    return min_date


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        n = int(input())
        day = [int(x) for x in input().split()]
        answer = test3(n, day)
        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()
