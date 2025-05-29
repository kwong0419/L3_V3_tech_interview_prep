from problems import binary_search, search_insert_position, first_bad_version

def test_binary_search():
    assert binary_search([-1,0,3,5,9,12], 9) == 4
    assert binary_search([-1,0,3,5,9,12], 2) == -1

def test_search_insert_position():
    assert search_insert_position([1,3,5,6], 5) == 2
    assert search_insert_position([1,3,5,6], 2) == 1
    assert search_insert_position([1,3,5,6], 7) == 4

def test_first_bad_version():
    assert first_bad_version(5) == 4
    assert first_bad_version(1) == 1

if __name__ == "__main__":
    test_binary_search()
    test_search_insert_position()