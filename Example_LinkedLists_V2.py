#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:54:30 2022

@author: derekfrost
"""
# https://stackoverflow.com/questions/56515975/python-logic-of-listnode-in-leetcode

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"


def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))

def reverseList(head: ListNode) -> ListNode:
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev

#%% Linked Lists Output
l1 = [1,2,3,2,1]
t2 = [2,3,4,5,4,3,2]

t1 = list_to_LL([1,2,3])
t2 = list_to_LL([1,2,3,4])
#%%

# https://leetcode.com/problems/palindrome-linked-list/discuss/1151395/Python-3-or-Easy-Solution
"""
head is defined as ListNode
isPalindrome return a bool value

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
		#vList = valueList
        vList = [] 
		
		#Converting to list
        while head != None:
           vList.append(head.val)
           head = head.next
        
		#nList = newList which will be reverse of vList
        return vList == vList[::-1]
 """       
#%%
head = cur = ListNode(0)
while t1 and t2:
    if t1.val < t2.val:
        cur.next = t1
        t1 = t1.next
    else:
        cur.next = t2
        t2 = t2.next
    cur = cur.next
cur.next = t1 or t2
    
print('while head next: ', head.next)
#%%
# def mergeTwoLists1(l1, t2):
dummy = cur = ListNode(0)
while t1 and t2:
    if t1.val < t2.val:
        cur.next = t1
        t1 = t1.next
    else:
        cur.next = t2
        t2 = t2.next
    cur = cur.next
cur.next = t1 or t2
print(dummy.next)
# return dummy.next
#%%
class Solution:
    def mergeTwoLists(self, l1: ListNode, t2: ListNode) -> ListNode:
        head = cur = ListNode(0)
        print('head next: ', head.next)
        
        while l1 and t2:
            if l1.val <= t2.val:
                cur.next = l1
                print('IF cur.next: ', cur.next)
                l1 = l1.next
                print('L1: ', l1)
            else:
                cur.next = t2
                print("ELSE cur.next: ", cur.next)
                t2 = t2.next
                print('t2: ', t2)
            cur = cur.next
            print('WHILE head next: ', head.next)
        cur.next = l1 or t2  # This line returns the remainder of the second LinkedList that could not have been compared to the first LinkedList
        return head.next
