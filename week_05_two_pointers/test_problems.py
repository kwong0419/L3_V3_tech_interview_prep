from problems import valid_palindrome, two_sum_ii, move_zeroes

def test_valid_palindrome():
    assert valid_palindrome("A man, a plan, a canal: Panama") == True
    assert valid_palindrome("race a car") == False
    assert valid_palindrome(" ") == True

def test_two_sum_ii():
    assert two_sum_ii([2,7,11,15], 9) == [1,2]
    assert two_sum_ii([2,3,4], 6) == [1,3]
    assert two_sum_ii([-1,0], -1) == [1,2]

def test_move_zeroes():
    assert move_zeroes([0,1,0,3,12]) == [1,3,12,0,0]
    assert move_zeroes([0,0,1]) == [1,0,0]
    assert move_zeroes([0]) == [0]

if __name__ == "__main__":
    test_valid_palindrome()
    test_two_sum_ii()
    test_move_zeroes()