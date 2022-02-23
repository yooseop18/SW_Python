T = int(input())

for test_case in range(1, T + 1):
    answer = "No"
    num, dnm = int(input()), 2
    if num == 1:
        answer = "Yes"
    while dnm != 10:
        # print(dnm)
        if (num / dnm) == (num // dnm) and (num / dnm) < 10:
            answer = "Yes"
            break

        dnm += 1

    print(f'#{test_case} {answer}')
