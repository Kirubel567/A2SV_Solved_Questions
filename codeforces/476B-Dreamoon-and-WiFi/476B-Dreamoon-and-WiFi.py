#first get all the possibilities 
#for each levels where pos[i] == "?" check both possibilities by making it + or -
#after building all the possibilities array compare how many of them are the same result as the right ones 


#move from left to right, if the curr_idx >= len(recieved) then add count to the possibilities 

target_s = list(input().strip())
target = 0
for ch in target_s: 
    if ch == "+": 
        target += 1
    else: 
        target -= 1

recieved = list(input().strip())
possibilities = []

def dfs(curr_idx, count, recieved): 
    if curr_idx >= len(recieved): 
        possibilities.append(count)
        count = 0
        return 
    
    #check each characters 
    ch = recieved[curr_idx]

    #if ch == "+" add one to count
    #if ch == "-" subtract one from count 
    #else try two different ways 
    #make the "?" "+" and call the dfs
    #or make the "?" "-" and call the dfs 

    if ch == "+": 
        dfs(curr_idx+1, count+1, recieved)
    elif ch == "-":
        dfs(curr_idx+1, count-1, recieved)
    else: 
        #make "?" a "+"
        curr_str = recieved[:]

        curr_str[curr_idx] = "+"
        dfs(curr_idx+1, count+1, curr_str)
        curr_str[curr_idx] = "?"

        #make "?" a "-"
        curr_str[curr_idx] = "-"
        dfs(curr_idx+1, count-1, curr_str)
        curr_str[curr_idx] = "?"

dfs(0, 0, recieved)
total = len(possibilities)
right_pos = 0

for num in possibilities: 
    if target == num: 
        right_pos+=1

print("%.12f" % (right_pos / total))