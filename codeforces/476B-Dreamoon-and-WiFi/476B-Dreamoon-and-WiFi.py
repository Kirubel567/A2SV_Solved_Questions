from math import comb

s1 = input().strip()
s2 = input().strip()

target = s1.count('+') - s1.count('-')

current = 0
q = 0

for c in s2:
    if c == '+':
        current += 1
    elif c == '-':
        current -= 1
    else:
        q += 1

diff = target - current

if (diff + q) % 2 != 0:
    print("0.000000000000")
else:
    x = (diff + q) // 2
    if x < 0 or x > q:
        print("0.000000000000")
    else:
        ways = comb(q, x) 
        total = 2 ** q
        print(f"{ways / total:.12f}")