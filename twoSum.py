from typing import List

def TwoSum(nums: List[int], target: int) -> List[int]:
    hashMap = {}
    for i, num in enumerate(nums): 
        diffBetTarget = target - num
        #hashMap[num] = i 

        if diffBetTarget in hashMap:
            return hashMap[diffBetTarget], i
        
        hashMap[num] = i 


    return None 

print(TwoSum([3, 2,4], 6))
