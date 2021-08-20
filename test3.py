import collections

input_ = [1, 2, 3, 4]

d = lambda: list(range(0, 5))

a = collections.defaultdict(d)

print(a[1])
