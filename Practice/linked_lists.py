# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # """
        # :type l1: ListNode
        # :type l2: ListNode
        # :rtype: ListNode
        # """
        res_ll = ListNode(0)
        head = res_ll
        carry = 0
        # res_ll.next = ListNode()
        while l1 is not None or l2 is not None:
            summ = carry + (l1.val if l1 != None else 0) + (l2.val if l2 != None else 0)
            ll_val = summ%10
            carry = summ//10
            res_ll.next = ListNode(ll_val)
            res_ll = res_ll.next
            l1 = l1.next if l1 != None else l1
            l2 = l2.next if l2 != None else l2
        return head.next


def createListNode(ls):
    ll = ListNode(0)
    head = ll
    for elem in ls:
        ll.next = ListNode(elem)
        ll = ll.next
    return head.next


def print_ll(ll):
    while ll is not None:
        print(ll.val)
        ll = ll.next

if __name__ == '__main__':
    list_node = createListNode([2, 4, 3])
    # print_ll(list_node)
    print_ll(Solution().addTwoNumbers(createListNode([2, 4, 3]), createListNode([5, 6, 4])))


