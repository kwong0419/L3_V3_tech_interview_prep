"""
1. Maximum Subarray
2. Minimum Size Subarray Sum
3. Longest Substring Without Repeating Characters
"""
def maximum_subarray(nums):
    if not nums:
        return 0
    
    left = 0
    current_sum = 0
    max_sum = float('-inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        max_sum = max(max_sum, current_sum)
        
        # If current_sum becomes negative, we reset the window
        if current_sum < 0:
            current_sum = 0
            left = right + 1
            
    return max_sum
# Time Complexity: O(n)
# Space Complexity: O(1)


def minimum_size_subarray_sum(target, nums):
    left, right = 0, 0
    min_length = float('inf')
    current_sum = 0
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    return min_length if min_length != float('inf') else 0
# Time Complexity: O(n)
# Space Complexity: O(1)


def longest_substring_without_repeating_characters(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
# Time Complexity: O(n)
# Space Complexity: O(min(n, m))
