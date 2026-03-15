class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        curr_bal =[]

        for bill in bills:
            if bill == 5: 
                curr_bal.append(5)
            else: 
                curr_bal.sort()
                i = len(curr_bal)-1

                _sum = 0
                bill -= 5
                while i>-1 and _sum < bill: 
                    if bill >= _sum + curr_bal[i]: 
                        _sum += curr_bal.pop(i)
                    else: 
                        i-=1
                        continue
                    i-=1
                if _sum < bill: 
                    return False
                curr_bal.append(bill+5)
        return True 
                
                
            
             
