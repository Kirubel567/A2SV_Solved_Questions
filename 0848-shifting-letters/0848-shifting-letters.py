class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        #use postfix sum (inclusive)
        #the for each letters in s add the ascii values to the shifts[i]
        #after adding convert to a-z (by subtracting ord('a'))
        #modulo 26 to make it in between a-z (wrapping)
        #then pos(what we found) + ord('a')
        #return chr of the above 
        _sum = 0
        post_fix = [_sum := _sum + shifts[i] for i in range(len(shifts)-1, -1, -1)]
        post_fix.sort(reverse=True)

        ans = []
        for i in range(len(s)): 
            pos = ((ord(s[i]) + post_fix[i]) - ord('a'))%26
            ans.append(chr(pos + ord('a')))
        return "".join(ans)
