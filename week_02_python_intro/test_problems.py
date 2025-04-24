import pytest
from problems import reverse_string, find_max, is_palindrome

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_find_max():
    assert find_max([1, 5, 3, 9]) == 9

def test_is_palindrome():
    assert is_palindrome("racecar")
    assert not is_palindrome("hello")