def test3(student):
    if student < 3:
        return 0

    max_stu = student // 3
    return max_stu


def main():
    T = int(input())
    for test_case in range(1, T + 1):
        student = int(input())
        answer = test3(student)

        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()
