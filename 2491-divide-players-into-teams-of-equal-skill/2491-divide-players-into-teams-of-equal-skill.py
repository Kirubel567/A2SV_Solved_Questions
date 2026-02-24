class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        start, end, ans = 0, len(skill) -1, 0
        check = skill[start] + skill[end]

        while start < end: 
            if skill[start]+skill[end] != check: 
                return -1
            
            ans += skill[start]*skill[end]
            end -= 1
            start += 1
        return ans 