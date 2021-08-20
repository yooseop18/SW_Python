T = int(input())

for test_case in range(1, T+1):
    list_2Arr = []
    for insert_to_list_2Arr in range(int(input())):
        input_ = [str(x) for x in input().split()]
        list_2Arr.append(input_)
        list_1Arr = sum(list_2Arr, [])

    answer_list = []
    for element in range(0, len(list_1Arr), 2):
        for i in range(int(list_1Arr[element+1])):
            answer_list.append(list_1Arr[element])

    #print(answer_list)
    print("#{}".format(test_case))
    for x in range(0, len(answer_list)//10+1):
        print("".join(answer_list[10*x:10*(x+1)]))

