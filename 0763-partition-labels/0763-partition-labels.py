class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #have a last index holder of each characters 
        last = {}
        for i in range(len(s)): 
            last[s[i]] = i
    
        #iterate over the array and determine where the last of the character is found, then while iterating through the current last index, check if the next elements last is after the firsts
        #eg: abab a's last is 2 up until 2 check if b's last is greater than this one if it's greater then take that range
        #make the maximum as the end, and if we reach the end(the max index) add the size there 
        start, end = 0, -float('inf')
        ans = []
        for i in range(len(s)): 
            end = max(end, last[s[i]]) #current max
            if i == end: #we reached 
                ans.append(end-start+1)
                start = i+1
        return ans 



