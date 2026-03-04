from collections import Counter
t = int(input())
for _ in range(t): 
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))

    left_c = Counter(socks[:l])
    right_c = Counter(socks[l:])

    for key, value in left_c.items(): 
        if key in right_c: 
            mn = min(right_c[key], left_c[key])
            left_c[key] -= mn
            right_c[key] -= mn 

    #create the left and right arrays from the frequency 
    left = []
    right = []
    for key, value in left_c.items(): 
        left.extend([key]*value)
    for key, value in right_c.items(): 
        right.extend([key]*value)
    
    #now the common elemetns are removed from both arrays 
    if len(right) == len(left): 
        print(len(left))
        continue 
    
    # ans = 2*transfered + min(len(left), len(right))
    
    mn = min(len(right), len(left))
    transfer = abs(len(right)-len(left))//2

    if len(right)>len(left): 
        _max = right
    else: 
        _max = left
    max_count = Counter(_max)
    ans = 2*transfer + mn

    #decreament the number of same elements in the _max from the anser as we don't need recoloring for them just leg chaning 
    for color in range(1, n+1): 
        while transfer > 0 and max_count[color] >1: 
            transfer -= 1
            ans -= 1
            max_count[color] -= 2
    
    print(ans)