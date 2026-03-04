class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        #the same as the before, but here we are shifting by one to the left or write instead of adding a number for that range 
        #z = (ord(letter)-ord('a'))%26 to make the wrapping work
        #shifting a character -> right -> chr(ord(char)+1) -> left -> chr(ord(char)-1)

        #first get the prefix sum based on the characters ascii then add it to the s after converting them to .. 
        shift = [0] * len(s)
        for start, end, direction in shifts:
            if direction == 1: 
                shift[start] += 1
                if end < len(shift)-1: 
                    shift[end+1] -= 1
            else: 
                shift[start] -= 1
                if end < len(shift)-1: 
                    shift[end+1] += 1
            
        #now create the prefix sum 
        _sum = 0
        pref_sum = [_sum := _sum + shift[i] for i in range(len(shift))]
        s = list(s)
        for i in range(len(s)): 
            new_pos = (pref_sum[i] + ord(s[i]) - ord('a')) %26
            s[i] = chr(new_pos + ord('a'))

        return "".join(s)