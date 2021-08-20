def calculate_min_time(n, camel_num, camel_times):
    total_time = 0

    # 낙타가 한마리일 경우
    if camel_num == 1:
        total_time = camel_times[0]
        print('#{0} {1}'.format(n + 1, total_time))

    elif camel_num == 2:
        total_time = camel_times[1]

    elif camel_num == 3:
        total_time = camel_times[0] + camel_times[1] + camel_times[2]

    # 낙타가 두마리 이상일 경우
    else:
        # 건너간 낙타들의 리스트를 생성
        cross_camel = []

        while len(camel_times) != 0:
            # 최소 시간의 낙타를 찾기 위한 정렬
            camel_times.sort()

            # 상위 2마리를 타고 건너감
            first_camel = camel_times[0]
            second_camel = camel_times[1]
            del camel_times[0]
            del camel_times[0]
            cross_time = second_camel
            total_time += cross_time
            cross_camel.append(first_camel)
            cross_camel.append(second_camel)

            # 모든 낙타가 건너갔는지 확인
            if len(camel_times) == 0:
                print('#{0} {1}'.format(n + 1, total_time))
                break

            # 최소의 시간을 갖는 낙타를 타고 돌아옴
            back_camel = min(cross_camel)
            min_index = cross_camel.index(back_camel)
            del cross_camel[min_index]
            total_time += back_camel
            camel_times.append(back_camel)
            camel_times.sort()

            # 하위 2마리를 타고 건너감
            first_camel = camel_times[-1]
            second_camel = camel_times[-2]
            del camel_times[-1]
            del camel_times[-1]
            cross_time = first_camel
            total_time += cross_time
            cross_camel.append(first_camel)
            cross_camel.append(second_camel)

            # 모든 낙타가 건너갔는지 확인
            if len(camel_times) == 0:
                print('#{0} {1}'.format(n + 1, total_time))
                break

            # 최소의 시간을 갖는 낙타를 타고 돌아옴
            back_camel = min(cross_camel)
            min_index = cross_camel.index(back_camel)
            del cross_camel[min_index]
            total_time += back_camel
            camel_times.append(back_camel)
            camel_times.sort()


def main():
    # 텍스트 파일을 읽은 후 리스트에 저장
    f = open(r'sample_input.txt')
    text = f.readlines()
    f.close()

    # 테스트 케이스의 개수
    test_case = int(text[0])

    # 낙타의 수와 소요 시간을 저장한 뒤 사용
    for i in range(0, test_case):
        camel_num = int(text[2 * i + 1].strip())
        camel_times = text[2 * i + 2].split()
        camel_times = list(map(int, camel_times))
        calculate_min_time(i, camel_num, camel_times)


if __name__ == '__main__':
    main()