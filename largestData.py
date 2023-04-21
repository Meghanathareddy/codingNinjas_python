from turtle import left, right


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

def largestData(root):
    if root == None:
        return -1 #ideally return -inf
    leftLargest = largestData(root.left)
    rightLargest = largestData(root.right)
    largest = max(leftLargest, rightLargest, root.data)
    return largest

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
print(largestData(root))