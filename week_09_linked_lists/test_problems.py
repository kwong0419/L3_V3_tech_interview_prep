class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from problems import reverse_linked_list, detect_cycle, merge_two_sorted_lists

def test_reverse_linked_list():
    # Test case 1: Empty list
    head = None
    reversed_head = reverse_linked_list(head)
    assert reversed_head is None

    # Test case 2: Single node list
    head = ListNode(1)
    reversed_head = reverse_linked_list(head)
    assert reversed_head.val == 1
    assert reversed_head.next is None

    # Test case 3: Multiple node list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    reversed_head = reverse_linked_list(head)
    assert reversed_head.val == 3
    assert reversed_head.next.val == 2
    assert reversed_head.next.next.val == 1
    assert reversed_head.next.next.next is None

    print("All test cases passed!")
    
def test_detect_cycle():
    # Test case 1: Empty list
    head = None
    assert detect_cycle(head) == False

    # Test case 2: Single node list
    head = ListNode(1)
    assert detect_cycle(head) == False

    # Test case 3: List with cycle
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next  # Creates a cycle: 1->2->3->2
    assert detect_cycle(head) == True

    print("All test cases passed!")

def test_merge_two_sorted_lists():
    # Test case 1: Empty lists
    l1 = None
    l2 = None
    merged_head = merge_two_sorted_lists(l1, l2)
    assert merged_head is None

    # Test case 2: One empty list
    l1 = None
    l2 = ListNode(1)
    merged_head = merge_two_sorted_lists(l1, l2)
    assert merged_head.val == 1
    assert merged_head.next is None

    # Test case 3: Both lists have elements
    # Create first list: 1->2->4
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    
    # Create second list: 1->3->4
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    
    merged_head = merge_two_sorted_lists(l1, l2)
    # Expected result: 1->1->2->3->4->4
    assert merged_head.val == 1
    assert merged_head.next.val == 1
    assert merged_head.next.next.val == 2
    assert merged_head.next.next.next.val == 3
    assert merged_head.next.next.next.next.val == 4
    assert merged_head.next.next.next.next.next.val == 4
    assert merged_head.next.next.next.next.next.next is None

    print("All test cases passed!")

if __name__ == "__main__":
    test_reverse_linked_list()
    test_detect_cycle()
    test_merge_two_sorted_lists()