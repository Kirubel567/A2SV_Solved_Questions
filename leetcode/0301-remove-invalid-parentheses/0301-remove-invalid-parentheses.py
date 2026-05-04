class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        #have a set to store the final anslwer, and a variable to store the longest_answer to compare inorder to remove the minimum number of parenthesis 
        longest = -1
        ans = set()

        def dfs(curr_idx, curr_res, string, l_count, r_count): 
            nonlocal ans 
            nonlocal longest

            if curr_idx >= len(string): 
                if l_count == r_count: 
                    if len(curr_res) > longest: 
                        longest = len(curr_res)

                        ans = set()
                        ans.add("".join(curr_res))
                    elif len(curr_res) == longest: 
                        ans.add("".join(curr_res))
            else: 
                curr_chr = string[curr_idx]

                if curr_chr == "(": 
                    #take it
                    curr_res.append(curr_chr)
                    dfs(curr_idx+1, curr_res, string, l_count+1, r_count)
                    curr_res.pop()

                    #don't take it
                    dfs(curr_idx+1, curr_res, string, l_count, r_count)
                elif curr_chr == ")": 
                    #don't take it
                    dfs(curr_idx+1, curr_res, string, l_count, r_count)

                    #take it
                    #when you take it you first have to check if the number of opening parenthesis are greater than the right ones, you only take the closing when the l_count is greater than the r_count 
                    if l_count > r_count: 
                        curr_res.append(curr_chr)
                        dfs(curr_idx+1, curr_res, string, l_count, r_count+1)
                        curr_res.pop()
                else: #when the character is a letter just append it 
                    curr_res.append(curr_chr)
                    dfs(curr_idx+1, curr_res, string, l_count, r_count)
                    curr_res.pop()
        dfs(0, [], s, 0, 0)
        return list(ans)