class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None


class ListNodeUtils:
    @staticmethod
    def reverse_second_half(ll):
        middle_minus_1 = ListNodeUtils.find_middle_ListNode(ll)
        middle_minus_1.next = ListNodeUtils.reverse_ListNode(middle_minus_1.next)
        return ll

    @staticmethod
    def find_middle_ListNode(ll):
        slow = ll
        fast = ll
        while (fast is not None and fast.next is not None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev

    @staticmethod
    def reverse_ListNode(ll):
        tmp = None
        new_node = None
        while ll is not None:
            tmp = ll.next
            ll.next = new_node
            new_node = ll
            ll = tmp
        return new_node

    @staticmethod
    def create_ListNode(ls):
        head = ListNode(0)
        curr = head
        for elem in ls:
            curr.next = ListNode(elem)
            curr = curr.next

        return head.next

    @staticmethod
    def print_ListNode(ll):
        while ll is not None:
            print(ll.val, end=' ')
            ll = ll.next
        print()

    # if __name__ == '__main__':
    #     ll_1 = ListNodeUtils.create_ListNode([1, 3, 2, 35, 43, 5, 66])
    #     ll_1 = ListNodeUtils.reverse_second_half(ll_1)
    #     ListNodeUtils.print_ListNode(ll_1)

ll_1 = ListNodeUtils.create_ListNode([1, 3, 2, 35, 43, 5, 66])
ll_1 = ListNodeUtils.reverse_second_half(ll_1)
ListNodeUtils.print_ListNode(ll_1)