#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtTail(head, data):
    # print("-----------------------------")
    # print("{} >>> {}".format(hex(id(head)), data))
    if head == None:
        head = SinglyLinkedListNode(data)
        head.next = None
        # print("{} -> {} => {}".format(hex(id(head)), head.data, hex(id(head.next))))
        return head
    node = head
    while 1:
        # print("+ {} -> {} => {}".format(hex(id(node)), node.data, hex(id(node.next))))
        if node.next == None:
            n = SinglyLinkedListNode(data)
            n.next = None
            node.next = n
            # print("++ {} -> {} => {}".format(hex(id(n)), n.data, hex(id(n.next))))
            break
        node = node.next
    # print("-----------------------------")
    return head
    

if __name__ == '__main__':
    fptr = open("./output/my.txt", 'w')
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
