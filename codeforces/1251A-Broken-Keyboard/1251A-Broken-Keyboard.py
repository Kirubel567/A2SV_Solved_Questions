t = int(input())

for _ in range(t): 
    st = input()
    ans  = []
    holder = 0

    while holder < len(st): 
        seeker = holder
        while seeker < len(st) and st[holder] == st[seeker]: 
            seeker += 1

        if (seeker-holder)%2 != 0: 
            if st[holder] not in ans: 
                ans.append(st[holder])
        holder = seeker

    print("".join(sorted(ans)))