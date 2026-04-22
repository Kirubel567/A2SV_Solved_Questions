class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        mapp = {'1': "", '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        #use backtracking, just select all the possible combinations from the starting letter to the rest of the letters, the base case is when the len(path) == len(digits), return here by adding it to the answer 
        ans =[]
        path =[]

        def backtrack(i): 
            if len(path) == len(digits): 
                ans.append(''.join(path))
                return 
            if i >= len(digits): 
                return 
            
            for letter in mapp[digits[i]]: 
                path.append(letter)
                backtrack(i+1)
                path.pop()
            
        backtrack(0)
        return ans 