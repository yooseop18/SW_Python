def moving_camel(start_arr, time):
    cnt = 0
    time += start_arr[-1]

    del start_arr[-1]
    del start_arr[-1]

    return time, cnt, start_arr


def main():
    T = int(input())
    for test_case in range(1, T + 1):
        N = int(input())
        start_arr = [int(x) for x in input().split()]
        start_arr = sorted(start_arr)

        if N == 1:
            time = start_arr[0]
            print("#{} {}".format(test_case, time))

        elif N == 2:
            time = start_arr[1]
            print("#{} {}".format(test_case, time))

        elif N == 3:
            time = start_arr[1] + start_arr[0] + start_arr[2]
            print("#{} {}".format(test_case, time))

        else:

            time = 0

            carry_camel = start_arr[1]

            carry_camel_to_end = start_arr[0] + start_arr[1] + start_arr[1]

            time += carry_camel_to_end - carry_camel
            #        print(time)
            del start_arr[1]
            #            print(start_arr)

            while (len(start_arr) >= 3):
                answer = moving_camel(start_arr, time)
                time = answer[0]
                cnt = answer[1]
                start_arr = answer[2]

                time += carry_camel_to_end * cnt

                if len(start_arr) == 2:
                    time += carry_camel
                else:
                    time += carry_camel * 2

            print("#{} {}".format(test_case, time))


main()