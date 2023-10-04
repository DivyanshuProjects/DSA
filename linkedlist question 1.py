"""Add Two Numbers leetcode question number 

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

### Solution code Leetcode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            current.next = ListNode(carry)
        
        return dummy_head.next


##################### full  code #######################

class Node:
    def __init__(self,data):
        self.data= data 
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head =None

    def insert(self,data):
        node =Node(data)
        if self.head is None :
            self.head = node
        else:
            current= self.head
            while current.next:
                current= current.next
            current.next = node
    def display(self):
        current = self.head
        while current:
            print(current.data ,end="->")
            current = current.next                              

    def add(list1,list2):
        result =Linkedlist()
        carry =0
        current1, current2 = list1.head ,list2.head
        while current1 or current2 or carry:
            val1= current1.data if current1 else 0
            val2 = current2.data if current2 else 0
            total = val1 + val2//10
            result.insert(total%10)

            if current1:
                current1 = current1.next
            if current2:
                current2 = current2.next  
        return result        

list1 = Linkedlist()
list2 = Linkedlist()
list1.insert(7)
list1.insert(1)
list1.insert(6)

list2.insert(5)
list2.insert(9)
list2.insert(2)                 

result = Linkedlist.add(list1,list2)

print("List 1:")
list1.display()
print("List 2:")
list2.display()
print("Result:")
result.display()
