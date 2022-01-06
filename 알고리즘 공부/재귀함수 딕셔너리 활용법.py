# 피보나치 수열 같이 재귀함수 사용 시, 러닝타임 줄이는 법!
# 딕셔너리를 만들어서 이미 연산 된 수를 저장
dic = {
    1: 1, 2: 1
}


def f(n):
    if n in dic:
        return dic[n]
    else:
        output = f(n - 1) + f(n - 2)
        dic[n] = output
        return output


print(f(40))
