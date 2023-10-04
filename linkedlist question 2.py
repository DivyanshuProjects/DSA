'''
Remove Nth Node From End of List

Link :- https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

 
'''
### letcode problem 

class Node:
    def __init__(self,data):
        self.next =None
        self.data =data
class Linked:        
    def __init__(self):
        self.head =None

    def insert(self ,data):
        node =Node(data)
        if self.head is  None:
            self.head =node
        else:
            current =self.head
            while current.next:
                current =current.next
            current.next = node
    def display(self):
        current= self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print()    

    def delete(self, data):
        current = self.head
        if current is not None and current.data == data:
            self.head = current.next
            return
        prev = None
        while current is not None:
            if current.data == data:
                break
            prev = current
            current = current.next
        if current is None:
            print(f"{data} not found in the list")
            return
        prev.next = current.next

list1 = Linked()
list1.insert(7)
list1.insert(1)
list1.insert(6)
print("List 1:")
list1.display()
list1.delete(7)
list1.display()


''' solution for letcode problem '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return dummy.next
