# Given two non-empty linked lists representing two non-negative integers
# The digits are stored in reverse order, and each of their nodes contains a single digit
# Add the two numbers and return the sum as a linked list

# Ex) input: l1 = [2, 4, 3], l2 = [5, 6, 4]
# Output: [7, 0, 8] because 342 + 465 = 807

#First, convert LinkedList to numbers
def recursion(root: ListNode): 
    if root.next is None: 
        return root.val
    return recursion(root.next) * 10 + root.val 

# Explanation: for l1, the recursion will first each the last node with the value of 3, returning 3.
# Moving up one level, it takes 2 and calculate 3 * 10 + 4 = 34
# Moving up again, it calculates 34 * 10 + 2 = 342. 
# [2, 4, 3] in reverse order = 342, therefore, it correctly converts l1 to the corresponding number.

def num_to_linkedlist(num: int) {
    root = ListNode(num % 10)
    p = root
    num = num // 10
    while num > 0:
        p.next = ListNode(num % 10)
        num = num // 10
        p = p.next
    return root
}

# root = ListNode(342 % 10), root = ListNode(2)
# p set to root poining to ListNode(2)
# num = 342 // 10, num = 34
# 1st iteration: p.next = ListNode(34 % 10), ListNode(4)
# p points to ListNode(4), list becomes 2 -> 4
# num = 34 // 10, num is 3. Repeat
# When num becomes 0, the loop ends and 2 -> 4 -> 3 -> None is generated. 

class Solution:

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # convert l1 and l2 to numbers
    num1 = recursion(l1)
    num2 = recursion(l2) 
    
    # add them and convert them again to LinkedList and return
    return int_to_linked_list(num1 + num2)