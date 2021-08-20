T = int(input())

for test_case in range(1, T+1):

    a = input()
    base64_list=[]
    for ch in a:
        if ch >= 'A' and ch <= 'Z':
            base64_list.append(ord(ch) - 65)
        elif ch >= 'a' and ch <= 'z':
            base64_list.append(ord(ch) - 71)
        elif ch >= '0' and ch <= '9':
            base64_list.append(ord(ch) + 4)
        else:
            if ch == '+':
                base64_list.append(62)
            elif ch == "/":
                base64_list.append(63)

    list_by_4btye = []
    #print(base64_list)

    cnt = 0
    long_bin = ""
    for sb in base64_list:
        long_bin += format(sb, '06b')
        cnt += 1
        if cnt == 4:
            list_by_4btye.append(long_bin)
            cnt = 0
            long_bin = ''

    #print(list_by_4btye)

    answer = ''
    for binary in list_by_4btye:
        word = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
        #print(word)
        for c in word:
            answer += c


    print("#{} {}".format(test_case, answer))


