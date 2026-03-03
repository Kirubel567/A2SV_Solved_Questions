t = int(input())

for _ in range(t): 
    n = int(input())
    p = list(map(int, input().split()))
    ans = [p[0]]
    for i in range(1, len(p)-1): 
        if p[i-1] < p[i] and p[i+1] < p[i] or p[i-1] > p[i] and p[i+1] > p[i]: 
            ans.append(p[i])
        
    
    ans.append(p[len(p)-1])
    print(len(ans))
    print(*ans)