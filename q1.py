

'''
Link: https://bytebytego.com/exercises/coding-patterns/two-pointers/pair-sum-sorted


Problem:    
    Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers
    in the array that sum to the target. The order of the indexes in the result doesn't matter. If no pair is found, 
    return an empty array.
'''

from typing import List

def pair_sum_sorted_bf(nums: List[int], target: int) -> List[int]:

    #brute
    size = len(nums)
    for i in range(size):
        for j in range(i+1, size):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def pair_sum_sorted(nums: List[int], target: int) -> List[int]:

    #binary search
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        if current_sum < target:
            left += 1
        else:
            right -= 1
    return []

def pair_sum_sorted_two_pointers(nums: List[int], target: int) -> List[int]:

    #two pointers
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        if current_sum < target:
            left += 1
        else:
            right -= 1
    return []


def pair_sum_sorted_hash_table(nums: List[int], target: int) -> List[int]:

    #hash table
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []


def pair_sum_set(nums: List[int], target: int) -> List[int]:

    #set
    seen = set()
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [nums.index(complement), i]
        seen.add(num)
    return []




if __name__ == "__main__":
    some_nums = [2, 7, 11, 15]
    TARGET = 9
#    print(pair_sum_sorted_bf(nums, TARGET)) # [0, 1]
    assert pair_sum_sorted_bf(some_nums, TARGET) == [0, 1]
    assert pair_sum_sorted(some_nums, TARGET) == [0, 1]
