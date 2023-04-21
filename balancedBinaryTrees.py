from operator import truediv
import re


class BinaryTreeNodes:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, end = ":")
    if root.left is not None:
        print("L",root.left.data, end = ",")
    if root.right is not None:
        print("R",root.right.data, end = "")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


def getheightAndCheckBalanced(root):
    if root == None:
        return 0, True
    lh, isLeftBalanced = getheightAndCheckBalanced(root.left)
    rh, isRightBalanced = getheightAndCheckBalanced(root.right)

    h = 1 + max(lh, rh)
    if lh - rh > 1 or rh -lh > 1:
        return h, False
    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False

def isBalanced2(root):
    h,isBalanced = getheightAndCheckBalanced(root)
    return isBalanced

def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNodes(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

root = takeInput()
printTreeDetailed(root)

print(isBalanced2(root))