def month_cal(month, day):
    month_dic = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return_ = 0

    for i in month_dic.keys():
        if i < month:
            return_ += month_dic[int(i)]
    return_ += day
    return return_


T = int(input())

for test_case in range(1, T + 1):
    arr = [int(x) for x in input().split()]

    answer = month_cal(arr[2], arr[3]) - month_cal(arr[0], arr[1]) + 1

    print("#{} {}".format(test_case, answer))
