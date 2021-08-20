# 2개의 포인터를 이용한 풀이
# 나중에 슬라이싱 윈도우 배우고 다시 해보기

def long_palindrome(s: str) -> str:
    # 2칸(짝수), 3칸(홀수)에서 시작해서 왼쪽 - / 오른쪽 + 하면서 s[왼쪽] == s[오른쪽]인걸 찾기
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:  # 예외 처리
        return s

    result = ''

    for i in range(len(s) - 1):
        result = max(result,    # 팰린드롬 중 가장 긴 값이 result
                     expand(i, i + 1),  # 짝수 범위 탐색
                     expand(i, i + 2),  # 홀수 범위 탐색
                     key=len)
    return result


def main():
    input_ = "123454321"
    answer = long_palindrome(input_)

    if len(answer) < 2:
        print("No palindrome")
    else:
        print(answer)


if __name__ == "__main__":
    main()
