n, k, q = map(int, input().split())
max_temp = 200000

diff = [0] * (max_temp + 2)
for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1

coverage = [0] * (max_temp + 1)
curr = 0
for i in range(1, max_temp + 1):
    curr += diff[i]
    coverage[i] = 1 if curr >= k else 0

for i in range(1, max_temp + 1):
    coverage[i] += coverage[i - 1]

for _ in range(q):
    a, b = map(int, input().split())
    print(coverage[b] - coverage[a - 1])