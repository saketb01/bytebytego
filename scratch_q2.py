"""
Given an array of integers, return all triplets [a, b, c] 
such that a + b + c = 0 . The solution must not contain duplicate 
triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates). 

If no such triplets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be 
returned in any order.
"""

from typing import List


def triplet_sum(nums: List[int]) -> List[List[int]]:
    response = [] #Or use hashset in combination with sorted tuple 
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in response:
                        response.append(triplet)
    return response    


def triplet_sum_optimization1(nums: List[int]) -> List[List[int]]:

    """
    Fix a, and confirm finding to b and c matching a (i.e. previous problem
    implementation)
    """
    nums = sorted(nums)
    length = len(nums) 
    response = []

    for pos in range(length - 2):
        val = nums[pos]
        if(val > 0):
            break

        left, right = pos + 1, length - 1
        while left < right:
            current_sum = val + nums[left] + nums[right]
            if current_sum == 0:
                triplet = sorted([val, nums[left], nums[right]])
                if triplet not in response:
                    response.append(triplet)
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
       
    return response



if __name__ == "__main__":
    print(triplet_sum([1, 2, -2, -1, 0, 3]))