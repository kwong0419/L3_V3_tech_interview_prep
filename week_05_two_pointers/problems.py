def valid_palindrome(str) -> bool:
       newStr = ''
       for char in str:
            if char.isalnum():
                newStr += char.lower()
       return newStr == newStr[::-1]
        
def two_sum_ii(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1
    return []

def move_zeroes(nums):
     left = 0
     for right in range(len(nums)):
          if nums[right] != 0:
               nums[left], nums[right] = nums[right], nums[left]
               left += 1
     return nums
     
