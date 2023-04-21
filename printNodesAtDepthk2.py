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

def numLeafNodes(root):
    if root == None:
        return 0
    if root.left is None and root.right is None:
        return 1
    numLeafLeft = numLeafNodes(root.left)
    numLeafRight = numLeafNodes(root.right)
    return numLeafLeft + numLeafRight
def printDepthK(root, k):
    if root == None:
        return
    if k == 0:
        print(root.data)
        return
    printDepthK(root.left, k - 1)
    printDepthK(root.right, k - 1)
    
def printDepthK2(root, k, d = 0):
    if root == None:
        return
    if k == d:
        print(root.data)
        return
    printDepthK2(root.left, d + 1)
    printDepthK2(root.right, d + 1)

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
print(numLeafNodes(root))
print(printDepthK(root, 2))
print(printDepthK2(root, 2))