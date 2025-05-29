"""
1. Binary Search (Basic)
2. Search Insert Position
3. First Bad Version
"""

def binary_search(nums, target): 
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def isBadVersion(version): # This would typically be provided by the API and is an example of a real world scenario
    if version >= 4:
        return True
    return False

def first_bad_version(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left
"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""