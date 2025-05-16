def contains_duplicate(nums):
    return len(nums) != len(set(nums))

def two_sum(nums, target):
    for i in range(len(nums)):
        if target - nums[i] in nums[i+1:]:
            return [i, nums.index(target - nums[i])]

def is_anagram(s, t):
    return sorted(s) == sorted(t)