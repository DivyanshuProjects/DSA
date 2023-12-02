# 1. Two Sum using linked list

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# leetcode solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}  
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return None
    



    # full solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def two_sum_linked_list(head, target):
    seen = {}
    current = head
    index = 0

    while current:
        complement = target - current.val
        if complement in seen:
            return [seen[complement], index]
        seen[current.val] = index
        current = current.next
        index += 1

    return None

# Example usage
nums = [2, 5, 3]
target = 9

# Create a linked list from the given numbers
head = ListNode(nums[0])
current = head
for num in nums[1:]:
    current.next = ListNode(num)
    current = current.next

result = two_sum_linked_list(head, target)

if result is not None:
    print(result)
else:
    print("No indices found.")
