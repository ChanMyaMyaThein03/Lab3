import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr) 

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])


def test_bubble_sort_greaterThan10():
     input_arr = [64, 34, 25, 12, 22, 11, 90, 56, 43, 23, 11]
     result = Lab3.bubble_sort(input_arr,Lab3.SORT_ASCENDING)
     assert (result == 1)

def test_bubble_sort_empty():
    input_arr = []
    result = Lab3.bubble_sort(input_arr,Lab3.SORT_ASCENDING)
    assert(result == 0)

def test_bubble_sort_notInteger():
    input_arr = [64, 34,"22", 25, 12, 22, 11, 90, 23, 45, 55, 12]
    result = Lab3.bubble_sort(input_arr,Lab3.SORT_ASCENDING)
    assert(result == 2)