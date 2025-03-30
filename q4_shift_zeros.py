from typing import List
"""
Q4: Given an array of integers, modify the array in place to move all zeros 
to the end while maintaining the relative order of non-zero elements.
"""
def shift_zeros_to_the_end(nums: List[int]) -> None:
    if not nums or len(nums) == 1:
        return
    
    nums_length = len(nums)
    first_index = 0
    second_index = 1
    while(second_index < nums_length):
        if(nums[second_index] == 0 and nums[first_index] != 0):
            # Swap and increment 
            nums[second_index] = nums[first_index]
            first_index += 1
            second_index += 1
        elif(nums[first_index]== 0 and nums[second_index] == 0):
            # Increment both indices 
            first_index += 1
            second_index += 1
        elif(nums[first_index] != 0 and nums[second_index] != 0):
            # Increment both indices
            first_index += 1
            second_index += 1
        elif(nums[first_index] == 0 and nums[second_index] != 0):
            # Increment both indices
            first_index += 1
            second_index += 1   

    print(nums)

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 2]
    shift_zeros_to_the_end(nums)
    print("All done")