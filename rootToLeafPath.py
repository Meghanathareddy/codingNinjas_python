from re import L
from turtle import right


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

def numNodes(root):
    if root == None:
        return 0
    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)
    return 1 + leftCount + rightCount
def nodeToRootPath(root,s):
    if root == None:
        return None
    if root.data == s:
        l = list()
        l.append(root.data)
        return l
    leftOutput = nodeToRootPath(root.left, s)
    if leftOutput != None:
        leftOutput.append(root.data)
        return leftOutput
    rightOutput = nodeToRootPath(root.right, s)
    if rightOutput != None:
        rightOutput.append(root.data)
        return rightOutput
    else:
        return None

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
print(numNodes(root))
print(nodeToRootPath(root, 5))