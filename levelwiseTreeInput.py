from logging import root
import queue
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

def takeLevelWiseTreeInput():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNodes(rootData)
    q.put(root)
    while (not (q.empty())):
        current_node = q.get()
        print("Enter Left child of ", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNodes(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)
        print("Enter right child of ", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNodes(rightChildData)
            current_node.right = leftChild
            q.put(rightChild)

root = takeLevelWiseTreeInput()
printTreeDetailed(root)