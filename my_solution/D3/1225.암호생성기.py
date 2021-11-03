def test3(arr):
    # cnt = 감소값
    cnt = 1
    while True:
        # 한 사이클 돌면 cnt 값 초기화
        if cnt > 5:
            cnt = 1
        # 맨 뒤의 값 <= 0 이면 0으로 변환 후 break
        if arr[-1] <= 0:
            arr[-1] = 0
            break
        # 비밀번호 연산
        num = arr.pop(0) - cnt
        arr.append(num)
        cnt += 1

    return arr


def main():
    for _ in range(10):
        tc = int(input())
        arr = [int(x) for x in input().split()]
        answer = test3(arr)
        print(f'#{tc}', end=' ')
        for i in answer:
            print(i, end=' ')
        print('')


if __name__ == '__main__':
    main()
