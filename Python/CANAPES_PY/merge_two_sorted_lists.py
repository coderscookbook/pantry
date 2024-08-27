'''
Merge Two Sorted Lists
- Topics: Linked list recursion
- You are given the heads of two sorted linked lists (list1, list2)
- Merge the two lists into one sorted list
- List should be made by splicing together the nodes of the first two lists
- Return the head of the merged linked list
Constraints:
- The number of nodes in both lists is in the range [0,50]
  -100 <= Node.val <= 100
= Both list1 and list2 are sorted in non-decreasing order
'''

# Definition for singly-linked list
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
      return l2
    elif not l2:
      return l1
    if l1.val < l2.val:
      l1.next = self.mergeTwoLists(l1
                                   .next, l2)
      return l1
    else: 
      l2.next = self.mergeTwoLists(l1 
                                   , l2.next)
      return l2

# Helper function to convert a list to a linked-list
def listToLinkedList(list):
  if not list:
    return None
  head = ListNode(list[0])
  current = head
  for value in list[1:]:
    current.next = ListNode(value)
    current = current.next
  return head

# Helper functio to print a linked list
def printLinkedList(node):
  while node:
    print(node.val, end=" -> ")
    node = node.next
  print("None")
  
  
if __name__ == '__main__':
  list1 = (1,2,3,4,5)
  list2 = (1.3, 2.3, 2.8, 4, 4.9, 5.001)
  # list1 = [1,2,4]
  # list2 = [1,3,4]

  linked_list_1 = listToLinkedList(list1)
  linked_list_2 = listToLinkedList(list2)

  solution = Solution()
  merged_list = solution.mergeTwoLists(linked_list_1, linked_list_2)

  print("New Merged List:")
  printLinkedList(merged_list)