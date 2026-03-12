class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        ans = []
        for i in range(len(s)): 
            curr = []
            if s[i] == ']': 
                while stk and stk[-1] != "[": 
                    curr.append(stk.pop())  
                stk.pop() #pop the opening
                num = ''
                while stk and stk[-1].isdigit():
                    num = stk.pop()+num
                k = int(num)
                decoded = "".join(reversed(curr))*k
                for ch in decoded: 
                    stk.append(ch)
            else:
                stk.append(s[i])
   
        return "".join(stk) 
