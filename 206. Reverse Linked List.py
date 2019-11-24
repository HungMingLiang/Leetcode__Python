# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        listN=[] #make a list
        while True:
            if head!=None:
                listN.append(head.val) #send node value to list
                head=head.next 
            else:
                break
        listN.reverse() #reverse list

        if listN==[]: #empty linked list
            return head
        a=ListNode(listN[0]) #create new listNode and assign first list value
        b=a #store first node
        for i in range(1,len(listN)):
            a.next=ListNode(listN[i]) #assign list element to new node and set as node.next
            a=a.next

        
        return b

#url: https://leetcode.com/problems/reverse-linked-list/
