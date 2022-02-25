# 문자열이 주어졌을 때, collection을 사용하여 갯수 세기
# for 문에서 if 절 사용하는법

import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
         .lower().split()
         if word not in banned]

# dict 형식으로 전환 됨 {'ㅁㅁ' : 1, ~~}
counts = collections.Counter(words)

print(words)
print(counts)

print(counts.most_common(1))