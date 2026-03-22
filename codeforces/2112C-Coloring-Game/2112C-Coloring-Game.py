t = int(input())
for _ in range(t): 
    n = int(input())
    lst = list(map(int, input().split()))

    _max = lst[n-1]
    counter =0
    for k in range(2, len(lst)): #start from 2 as z is the max and elem at 0 and 1 can't be max
        z = lst[k]
        diff = max(z, _max-z)

        i = 0
        j = k-1
        while i < j: 
            if lst[i] + lst[j] > diff: 
                counter += (j-i)
                j -= 1
            else: 
                i += 1
    print(counter)