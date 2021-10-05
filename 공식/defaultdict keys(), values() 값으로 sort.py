

# defaultdict(float)로 다음과 같이 입력받았다고 하자
# dict 도 마찬가지임

dic = {1: 74.6, 2: 92.55000000000001, 3: 88.8,
       4: 99.45, 5: 72.35, 6: 85.85000000000001,
       7: 96.25, 8: 68.95, 9: 85.5, 10: 1889.55}




# dic value 값으로 정렬하기
import operator

# itemgetter(0) = key 값, itemgetter(1) = value 값, default = (1)
# reverse = True 는 내림차순, default = false
dic = sorted(dic.items(),
             key=operator.itemgetter(0),
             reverse=True)

print(dict(dic))
