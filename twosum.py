def twoSum(nums: list[int], target: int) -> list[int]:
    r=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if target==nums[i]+nums[j]:
                r.append([i,j])
    return r if r else [[-1,-1]]
nums=[0,3,7,0,9,7,6]
print(twoSum(nums,9))
