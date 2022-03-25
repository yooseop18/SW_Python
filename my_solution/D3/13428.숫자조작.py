def test3(input_num):
    # 각 자리수 마다 움직이면서 최소, 최대값 찾기
    num_arr = []
    max_num, min_num = input_num, input_num

    while input_num != 0:
        num_arr.append(input_num % 10)
        input_num //= 10
    num_arr.reverse()
    num_arr = list(map(str, num_arr))

    for i in range(len(num_arr) - 1):

        for j in range(i + 1, len(num_arr)):
            change_arr = [x for x in num_arr]
            change_arr[i], change_arr[j] = change_arr[j], change_arr[i]
            if change_arr[0] != '0':
                change_num = "".join(change_arr)

                if int(change_num) < min_num:
                    min_num = int(change_num)
                elif int(change_num) > max_num:
                    max_num = int(change_num)

            change_arr.clear()

    return min_num, max_num




def main():
    T = int(input())

    for test_case in range(1, T + 1):
        input_num = int(input())

        answer = test3(input_num)

        print(f'#{test_case} {answer[0]} {answer[1]}')


main()
