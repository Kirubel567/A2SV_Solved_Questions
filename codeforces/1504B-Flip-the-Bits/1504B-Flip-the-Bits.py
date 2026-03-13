def solve():
        a.append("0")
        b.append("0")
        count_0, count_1 = 0, 0
        for i in range(len(a)-1): 
            if a[i] == "1": 
                count_1 += 1
            else: 
                count_0+=1

            diff = count_1-count_0
            if ((a[i] == b[i]) != (a[i+1]==b[i+1])) and diff != 0: 
                return "NO"
        return "YES" 
    print(solve())