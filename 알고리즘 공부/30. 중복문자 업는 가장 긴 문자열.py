def length_(input_: str) -> int:
    used = {}   # dict 선언. key-val 값으로 하는 것이 편리
    max_length = start = 0

    # 문자열에서
    for index, char in enumerate(input_):
        # 해당 글자가 처음 등장한게 아니라면, (used 안에 있다면) start 점을 한칸 이동
        if char in used:
            start = used[char] + 1
        # 해당 글자가 처음 등장한 것이면, max_length 길이를 구함
        else:
            max_length = max(max_length, index - start + 1)

        # used: {char : index} 해시테이블
        used[char] = index

    return max_length


def main():
    input_ = 'abacdabacdebb'

    answer = length_(input_)

    print(answer)


main()
