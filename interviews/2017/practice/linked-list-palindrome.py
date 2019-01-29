def find_middle(head):
    """FInd meddle of linked list using 2 runner strategy and return if it's an odd length list
    return middle_node, is_odd(Bool)
    """
    r1 = head
    r2 = head
    while r2.next:
        if not r2.next.next:
            return r1, False
        r1 = r1.next
        r2 = r2.next.next

    return r1, True


def reverse_list(head, end):
    prev = head
    head = head.next
    while head != end:
        next = head.next
        head.next = prev
        prev = next
    head.next = prev


def compare_lists(head1, head2):
    while head1 and head2:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next
    return True

def palindrome(head):
    middle, is_odd = find_middle(head)
    list_2 = middle.next
    reverse_list(head, middle)

    if is_odd:
        list_1 = middle.next
    else:
        list_1 = middle

    result = compare_lists(list_1, list_2)

    reverse_list(middle, head)

    return result



class LinkedListNode:
    data = None
    next = None

    def __init__(self, d):
        self.data = d


l1 = LinkedListNode('p')
l2 = LinkedListNode('o')
l2 = LinkedListNode('o')
l3 = LinkedListNode('p')

l1.next = l2
l2.next = l3


print(palindrome(l1))
