### Problems:
# 1. Reverse Linked List
# 2. Detect Cycle in Linked List
# 3. Merge Two Sorted Lists

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
# Time Complexity: O(n)
# Space Complexity: O(1)

def detect_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
# Time Complexity: O(n)
# Space Complexity: O(1)

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
    current.next = l1 or l2
    return dummy.next
# Time Complexity: O(n)
# Space Complexity: O(1)