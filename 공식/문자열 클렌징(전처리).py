# 문자열 입력 받았을 때, 문자(+숫자) 외 나머지 삭제하기

import re


'''
\d - 숫자와 매치, [0-9]와 동일한 표현식이다.
\D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
\s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
\S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
\w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
\W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.
'''

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']

# re.sub('교체할 단어', '교체 대상', '문자열')

arr = [word for word in re.sub(r'[\W]', ' ', paragraph)  # r['^\w']도 된다.
       .lower().split()
       if word not in banned]

print(arr)
