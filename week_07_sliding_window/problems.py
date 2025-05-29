"""
1. Maximum Subarray
2. Minimum Size Subarray Sum
3. Longest Substring Without Repeating Characters
"""
def maximum_subarray(nums):
    if not nums:                # If the array is empty, return 0
        return 0
    
    left = 0                    # Start of our window
    current_sum = 0             # Keep track of sum in current window
    max_sum = float('-inf')     # Keep track of best sum we've seen
    
    for right in range(len(nums)):    # Move right pointer through array
        current_sum += nums[right]     # Add current number to window sum
        max_sum = max(max_sum, current_sum)  # Update best sum if needed
        
        if current_sum < 0:            # If window sum becomes negative
            current_sum = 0            # Reset window sum
            left = right + 1           # Move window start to next position
            
    return max_sum              # Return the best sum we found
# Time Complexity: O(n)
# Space Complexity: O(1)


def minimum_size_subarray_sum(target, nums):
    left, right = 0, 0                 # Start both pointers at beginning
    min_length = float('inf')          # Keep track of smallest window size
    current_sum = 0                    # Keep track of sum in current window
    
    for right in range(len(nums)):     # Move right pointer through array
        current_sum += nums[right]      # Add current number to window sum
        
        while current_sum >= target:    # While window sum is big enough
            min_length = min(min_length, right - left + 1)  # Update smallest window
            current_sum -= nums[left]   # Remove leftmost number
            left += 1                   # Move left pointer right
            
    return min_length if min_length != float('inf') else 0  # Return smallest window size
# Time Complexity: O(n)
# Space Complexity: O(1)


def longest_substring_without_repeating_characters(s):
    char_set = set()                   # Keep track of unique characters in window
    left = 0                           # Start of our window
    max_length = 0                     # Keep track of longest window size
    
    for right in range(len(s)):        # Move right pointer through string
        while s[right] in char_set:    # If current character is already in window
            char_set.remove(s[left])    # Remove leftmost character
            left += 1                   # Move left pointer right
            
        char_set.add(s[right])         # Add current character to window
        max_length = max(max_length, right - left + 1)  # Update longest window
        
    return max_length                  # Return length of longest window
# Time Complexity: O(n)
# Space Complexity: O(min(n, m))
