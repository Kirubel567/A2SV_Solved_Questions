t = int(input())
for _ in range(t): 
    r = int(input())
    red = list(map(int, input().split()))
    b = int(input())
    blue = list(map(int, input().split()))

    max_r = 0
    accumulate = 0
    for i in range(len(red)): 
        accumulate += red[i]
        max_r = max(max_r, accumulate)
    max_b = 0
    accumulate = 0
    for i in range(len(blue)): 
        accumulate += blue[i]
        max_b = max(max_b, accumulate)
    print(max_b+max_r)