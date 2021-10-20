arr = [int(x) for x in range(10)]

num = 0
# try, except 문
# except 문에 에러코드를 작성하면 해당 에러 시 동작을 정의할 수 있음
# IndexError 를 사용하면 배열에서 조건 탐색 시 유용하게 사용할 수 있음
while True:
    try:
        print(arr[num], end=", ")
        num += 1
    except IndexError:
        print("End!")
        break
