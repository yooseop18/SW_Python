def solution(input_cmd, input_speed, current_speed):
    # command에 따라 연산 수행
    if input_cmd == 1:
        current_speed += input_speed

    elif input_cmd == 2:
        if current_speed - input_speed > 0:
            current_speed -= input_speed
        else:
            pass
    else:
        if current_speed - input_speed > 0:
            current_speed += input_speed
        else:
            pass

    # 거리 = 1초당 * 속도, 즉 거리 = 속도
    moving_dist = current_speed * 1
    
    return moving_dist


T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    answer = 0
    current_speed = 0

    for r in range(N):

        input_ = [int(x) for x in input().split()]
        input_cmd = input_[0]
        if input_cmd == 0:
            input_speed = 0
        else:
            input_speed = input_[1]

        return_ = solution(input_cmd, input_speed, current_speed)

        # 총 이동거리 합산
        answer += return_
        # 현재 이동속도 업데이트
        current_speed = return_

    print("#{} {}".format(test_case, answer))


