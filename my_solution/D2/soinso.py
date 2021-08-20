def solution(num, divide_by):
    sol = num / divide_by

    return sol

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    while N != 0:
        if N % 2 == 0 and N != 0:
            N = solution(N, 2)
            a += 1
        else:
            if N % 3 == 0:
                N = solution(N, 3)
                b += 1
            else:
                if N % 5 == 0:
                    N = solution(N, 5)
                    c += 1
                else:
                    if N % 7 == 0:
                        N = solution(N, 7)
                        d += 1
                    else:
                        if N % 11 == 0:
                            N = solution(N, 11)
                            e += 1
                        else:
                            break

    print("#{} {} {} {} {} {}".format(test_case, a, b, c, d, e))

