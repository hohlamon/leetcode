# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        values = []
        node = self
        while node is not None:
            values.append(node.val)
            node = node.next
        return str(values)



class Solution:
    def mergeTwoLists(self, list1:list[ListNode], list2: list[ListNode]) -> list[ListNode]:
        node1 = list1
        node2 = list2
        new_head = None
        new_tail = None
        is_head = True

        if not node1 and node2:
            return node2
        if not node2 and node1:
            return node1
        if not node1 and not node2:
            return None

        while node1 is not None or node2 is not None:

            if node1 is None:
                new_tail.next = node2
                break
            if node2 is None:
                new_tail.next = node1
                break

            if node1.val < node2.val:
                if is_head:
                    new_head = ListNode(node1.val)
                    new_tail = new_head
                    node1 = node1.next
                    is_head = False
                else:
                    new_tail.next = ListNode(node1.val)
                    new_tail = new_tail.next
                    node1 = node1.next

            elif node2.val < node1.val:
                if is_head:
                    new_head = ListNode(node2.val)
                    new_tail = new_head
                    node2 = node2.next
                    is_head = False
                else:
                    new_tail.next = ListNode(node2.val)
                    new_tail = new_tail.next
                    node2 = node2.next

            else:
                if is_head:
                    new_head = ListNode(node1.val, ListNode(node1.val))
                    new_tail = new_head.next
                    is_head = False
                    node1 = node1.next
                    node2 = node2.next
                else:
                    new_tail.next = ListNode(node1.val, ListNode(node1.val))
                    new_tail = new_tail.next.next
                    node1 = node1.next
                    node2 = node2.next
        return new_head


# l1 = ListNode(1,ListNode(1, ListNode(2, None)))
# l2 = ListNode(1,ListNode(3, ListNode(4, None)))

# l1 = ListNode(1)
# l2 = ListNode(2)

# sol = Solution()
# print(sol.mergeTwoLists(l1,l2))
