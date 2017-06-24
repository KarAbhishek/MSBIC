class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        tmp = None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        ll = slow
        self.reverseLl(ll)
        return head

    def reverseLl(self, ll):
        tmp = None  # 1,2,3,4
        firstNode = None
        while ll is not None:
            firstNode = ll  # 1,2,3,4
            ListNodeUtils.print_node(firstNode)
            tmp = ll.next  # 2,3,4
            ListNodeUtils.print_node(tmp)
            firstNode.next = None   # 1
            ListNodeUtils.print_node(firstNode)
            tmp.next = None

            ListNodeUtils.print_node(tmp)
            # ll = ll.next
            return
        pass

    def reverseListNode(self, head):
        new_node = None
        tmp = None
        while head is not None:
            tmp = head.next
            head.next = new_node
            new_node = head
            head = tmp
        return new_node

class ListNode:
    def __init__(self):
        self.val = None
        self.next = None


class ListNodeUtils:
    @staticmethod
    def print_node(head):
        while head is not None:
            print(head.val, end=' ')
            head = head.next
        print()

    @staticmethod
    def create_list_node(ls):
        node = ListNode()
        head = node
        prev = head
        for elem in ls:
            node.val = elem
            prev = node
            node.next = ListNode()
            node = node.next

        prev.next = None
        return head

    @staticmethod
    def create_list_node_param(ls):
        head = ListNode(ls[0])
        ll = head
        for elem in ls[1:]:
            ll.next = ListNode(elem)
            ll = ll.next
        return head

    @staticmethod
    def reverseListNode(head):
        new_node = None
        tmp = None
        while head is not None:
            tmp = head.next
            head.next = new_node
            new_node = head
            head = tmp
        return new_node

    @staticmethod
    def delete_node(head, target_node):
        ll = head
        prev = None
        while ll is not None:
            if ll.val == target_node:
                # delete Node
                if prev is None:
                    head = head.next
                else:
                    prev.next = ll.next
            # else:
            prev = ll
            ll = ll.next
        return head

ls = [5, 6, 1, 2, 3, 4]
list_node = ListNodeUtils.create_list_node(ls)
l = ListNodeUtils.delete_node(list_node, 5)
ListNodeUtils.print_node(l)
