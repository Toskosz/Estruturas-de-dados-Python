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


def print_singly_linked_list(node):
    while node:
        node = node.next
        if node:
            print(node.data)


def insertNodeAtTail(head, data):
    if head:
        return insertNodeAtTail(head.next, data)
    else:
        head = SinglyLinkedListNode(data)
        return head


def main():
    llist_count = 5

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)


main()
