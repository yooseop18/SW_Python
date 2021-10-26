def test3(bit):
    cnt = 0
    comparison_arr = [0 for _ in range(len(bit))]
    while bit != comparison_arr:
        for i in range(len(bit)):
            # 해당 자릿수(i) 일치 확인
            if bit[i] != comparison_arr[i]:
                # 아니라면, com[i:-1] = bit[i]
                for j in range(i, len(comparison_arr)):
                    comparison_arr[j] = bit[i]
                # cnt 증가
                cnt += 1
                continue

    return cnt


def main():
    T = int(input())
    for test_case in range(1, T + 1):
        bit = [int(x) for x in input()]   # 한글자씩 int 로 입력
        answer = test3(bit)
        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()
