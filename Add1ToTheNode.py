#python3 program to add 1 to a linked list
import sys
import math

##Linked List node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
#Function to create a new node with given data

def newNode(data):
    return Node(data)

#Function to reverse the linked List

def reverseList(head):
    if not head:
        return
    curNode = head
    prevNode = head
    nextNode = head.next
    curNode.next = None

    while (nextNode):
        curNode = nextNode
        nextNode = nextNode.next
        
