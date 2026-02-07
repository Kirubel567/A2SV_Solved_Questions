class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float('inf')

        list2_mapp = {}

        for i in range(len(list2)): 
            list2_mapp[list2[i]] = i
        
        min_mapp = {}

        for i in range(len(list1)): 
            if list1[i] in list2_mapp: 
                min_mapp[list1[i]] = i + list2_mapp[list1[i]]
                min_sum = min(min_sum, i + list2_mapp[list1[i]])

        res = []
        for i in range(len(list1)): 
            if list1[i] in min_mapp and min_mapp[list1[i]] == min_sum: 
                res.append(list1[i])
            
        return res 
