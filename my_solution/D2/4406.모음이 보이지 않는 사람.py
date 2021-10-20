def test3(word):
    result = []
    arr = ['a', 'e', 'i', 'o', 'u']
    for i in word:
        if i not in arr:
            result.append(i)
    return result


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        word = input()
        answer = test3(word)
        # 출력
        print(f'#{test_case}', end=" ")
        for i in answer:
            print(i, end="")
        print("")


if __name__ == '__main__':
    main()
