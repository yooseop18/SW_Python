def pen(input_: str) -> bool:
    arr = []
    for i in input_:  # input 값을 한글자씩 문자만 소문자로 배열에 넣기
        if i.isalnum():
            arr.append(i.lower())

    while len(arr) > 1:  # 첫글자와 첫글자씩 배열에서 pop 해서 비교
        if arr.pop(0) != arr.pop():
            return False

    return True


def main():
    answer = pen(input())
    print(answer)


if __name__ == "__main__":
    main()
