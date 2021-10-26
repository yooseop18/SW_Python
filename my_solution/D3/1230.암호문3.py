def test3(input_length, input_arr, cmd_length, cmd_arr):
    # cmd_arr 의 idx 값. 0부터 탐색하며 값 갱신
    cmd_idx = 0
    while cmd_idx != len(cmd_arr):
        # 입력값 I 일 때
        if cmd_arr[cmd_idx] == 'I':
            for i in range(int(cmd_arr[cmd_idx + 2]) - 1, -1, -1):
                input_arr.insert(int(cmd_arr[cmd_idx + 1]), int(cmd_arr[cmd_idx + 3 + i]))
            # 삽입할 숫자의 갯수
            y = int(cmd_arr[cmd_idx + 2])
            cmd_idx += y + 3
            continue
        # 입력값 D 일 때
        elif cmd_arr[cmd_idx] == 'D':
            for i in range(int(cmd_arr[cmd_idx + 2])):
                input_arr.remove(input_arr[int(cmd_arr[cmd_idx + 1])])
            cmd_idx += 3
            continue
        # 입력값 A 일 때
        elif cmd_arr[cmd_idx] == 'A':
            for i in range(int(cmd_arr[cmd_idx + 1]) - 1, -1, -1):
                input_arr.insert(-1, int(cmd_arr[cmd_idx + 2 + i]))
            y = int(cmd_arr[cmd_idx + 1])
            cmd_idx += y + 2
            continue
        # 예외 처리
        else:
            cmd_idx += 1
            continue


    return input_arr[0:10]


def main():
    for test_case in range(1, 11):
        input_length = int(input())                 # 원본 암호문의 길이
        input_arr = [int(x) for x in input().split()]    # 원본 암호문
        cmd_length = int(input())                   # 명령어의 개수
        cmd_arr = [x for x in input().split()]      # 명령어

        answer = test3(input_length, input_arr, cmd_length, cmd_arr)
        print(f'#{test_case}', end=" ")
        for i in range(len(answer)):
            print(answer[i], end=" ")
        print("")


if __name__ == '__main__':
    main()
