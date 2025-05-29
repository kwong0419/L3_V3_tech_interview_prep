from problems import maximum_subarray, minimum_size_subarray_sum, longest_substring_without_repeating_characters

def test_maximum_subarray():
    assert maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert maximum_subarray([1]) == 1
    assert maximum_subarray([5,4,-1,7,8]) == 23

def test_minimum_size_subarray_sum():
    assert minimum_size_subarray_sum(7, [2,3,1,2,4,3]) == 2
    assert minimum_size_subarray_sum(4, [1,4,4]) == 1
    assert minimum_size_subarray_sum(11, [1,1,1,1,1,1,1,1]) == 0

def test_longest_substring_without_repeating_characters():
    assert longest_substring_without_repeating_characters("abcabcbb") == 3
    assert longest_substring_without_repeating_characters("bbbbb") == 1
    assert longest_substring_without_repeating_characters("pwwkew") == 3

if __name__ == "__main__":
    test_maximum_subarray()
