st = input()
stk= [-1]
max_len=counter=0
for i in range(len(st)): 
    if st[i] == "(": 
        stk.append(i)
    else: 
        stk.pop()

        if not stk: 
            stk.append(i)
        else: 
            length = i - stk[-1]

            if length>max_len: 
                max_len = length
                counter=1
            elif length == max_len: 
                counter+=1
if max_len==0: 
    print("0 1")
else: 
    print(max_len, counter)