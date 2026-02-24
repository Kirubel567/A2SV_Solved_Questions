class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack: 
            return -1
        #use two pointers that are moving in the same direction
        #initialize the first pointer when you see the first letter of needle
        #then move the second pointer until len(needle) == j - i
        #if haystack[i:j+1] == needle return i 
        i = 0
        while i < len(haystack):
            j = 0 
            if haystack[i] == needle[0]:
                j = i
                start = 0 
                while (j-i) < len(needle) and j<len(haystack): 
                    if haystack[j] == needle[j-i]: 
                        j += 1
                    else: 
                        break 
                
                if haystack[i:j] == needle: 
                    return i
                i += 1

            else: 
                i += 1
            
        
