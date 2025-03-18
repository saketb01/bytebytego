"""
LinK: 

TripletSum Problem: https://bytebytego.com/exercises/coding-patterns/two-pointers/triplet-sum

Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0 . The solution must not contain 
duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates). If no such triplets are found, 
return an empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.
"""

from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    result = []
    size = len(nums)
    for i in range(size):
        for j in range(i+1, size):
            for k in range(j+1, size):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

    return result


if __name__ == "__main__":
    print(triplet_sum([2, -5, 3, -1, -1 ]))