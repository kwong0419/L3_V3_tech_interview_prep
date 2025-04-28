// Reverse a string
function reverseString(str) {
  let reversed = ''
  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i]
  }
  return reversed
}

// Find max in array
function findMax(arr) {
  let max = arr[0]
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i]
    }
  }
  return max
}

// Check if palindrome
function isPalindrome(word) {
  let reversed = ''
  for (let i = word.length - 1; i >= 0; i--) {
    reversed += word[i]
  }
  return reversed === word
}

module.exports = {reverseString, findMax, isPalindrome}
