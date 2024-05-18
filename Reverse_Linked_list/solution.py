#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __str__(self):
#         values = []
#         node = self
#         while node is not None:
#             values.append(node.val)
#             node = node.next
#         return str(values)


class Solution:
    def recursive(self, last_node:ListNode, head:ListNode):
        if head.next is None:
            head.next = last_node
            return head
        tmp_node = ListNode(head.val, None)
        tmp_node.next = last_node
        return self.recursive(tmp_node, head.next)

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        return self.recursive(None, head)

# nums = [1,2,3,4,5]
# node = ListNode(nums[0], None)
# head = node
# for num in nums[1:]:
#     tmp = ListNode(num, None)
#     node.next = tmp
#     node = node.next

# sol = Solution()
# print(sol.reverseList(head))
