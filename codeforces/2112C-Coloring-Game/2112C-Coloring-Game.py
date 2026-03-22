import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    M = a[-1] 
    ans = 0

    for k in range(2, n):
        z = a[k]
        T = max(z, M - z)

        i, j = 0, k - 1

        while i < j:
            if a[i] + a[j] > T:
                ans += (j - i)
                j -= 1
            else:
                i += 1

    print(ans)