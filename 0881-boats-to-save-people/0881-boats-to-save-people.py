class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        small, large = 0, len(people)-1
        b_counter = 0
        while small <= large: 
            if people[small]+people[large] <= limit: 
                b_counter += 1
                small += 1
                large -= 1
            else: 
                if people[small] > limit: 
                    large -= 1
                    small += 1
                    b_counter += 2
                else: 
                    large -=1
                    b_counter += 1
        return b_counter
        