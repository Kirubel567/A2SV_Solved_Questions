class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        check={'1': "", '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        path = []
        ans=[]
        n = len(digits)
        def backtrack(idx): 
            if len(path) == n: 
                ans.append("".join(path.copy()))
                return  

            st = check[digits[idx]]
            for j in range(len(st)):
                path.append(st[j])
                backtrack(idx+1)
                path.pop()

        backtrack(0)
        return ans  


