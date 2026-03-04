t = int(input())

for _ in range(t): 
    n, k = map(int, input().split())
    colors = list(input().strip())

    w_count = colors[:k].count("W")
    min_count = w_count 

    for i in range(k, len(colors)): 
        if colors[i-k] == "W": 
            w_count -= 1
        
        if colors[i] == "W": 
            w_count += 1
        min_count = min(min_count, w_count)

    print(min_count)