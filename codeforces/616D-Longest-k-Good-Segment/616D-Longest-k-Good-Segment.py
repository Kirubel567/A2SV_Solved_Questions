n, k = map(int, input().split())
nums = list(map(int, input().split()))
ans1,ans2= 0,0
mapp = {}

left, curr_max = 0, float('-inf')
for r in range(len(nums)):
    mapp[nums[r]] = mapp.get(nums[r], 0) + 1

    while len(mapp) > k: 
        mapp[nums[left]] = mapp.get(nums[left], 0) -1
        if mapp[nums[left]] == 0: 
            del mapp[nums[left]]
        
        left += 1

    if curr_max < r-left+1: 
        ans1 = left
        ans2 = r
        curr_max = r - left +1
    
    
print(ans1+1, ans2+1)