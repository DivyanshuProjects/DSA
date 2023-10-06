""" leetcode problem no 24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
Example :1 
Input: head = [1,2,3,4]
Output: [2,1,4,3]"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next

    def append(self):
        current = self.head
        while current and current.next:
            current.data ,current.next.data = current.next.data, current.data
            current= current.next           

ll = Linkedlist()
ll.insert(7)
ll.insert(8)
ll.insert(9)
ll.insert(0)
ll.append()
ll.display()

################## Letcode Solution #########################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            
            node1 = current.next
            node2 = current.next.next

           
            node1.next = node2.next
            node2.next = node1
            current.next = node2

           
            current = node1

        return dummy.next









