import collections


def test3(input_):
    words = [word for word in input_]
    counts = collections.Counter(words)
    arr = []
    cnt = 0

    for _ in range(len(counts)):
        arr.append(counts.popitem())

    for i in range(len(arr)):
         if arr[i][1] == 2:
             cnt += 1

    if cnt == 2:
        return "Yes"
    else:
        return "No"


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        input_ = input()
        answer = test3(input_)

        print(f'#{test_case} {answer}')


main()
