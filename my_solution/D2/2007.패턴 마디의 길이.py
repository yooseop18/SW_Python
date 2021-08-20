T = int(input())

for test_case in range(1, T + 1):

    word = input()
    arr = []

    for i in range(len(word)):
        arr.append(word[i])
        j = i + 1
        if word[i] == arr[0] and len(arr) != 1 and word[j] == arr[1]:
            answer = "".join(arr[:-1])
            print("#{0} {1}".format(test_case, len(answer)))
            break
        else:
            pass

