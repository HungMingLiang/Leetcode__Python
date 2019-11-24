# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val #make node value = node.next value
        node.next=node.next.next #make node.next connect to node.next.next
        
#url: https://leetcode.com/problems/delete-node-in-a-linked-list/
