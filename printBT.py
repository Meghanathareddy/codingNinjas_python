class BinaryTreeNodes:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root == None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

btn1 = BinaryTreeNodes(1)
btn2 = BinaryTreeNodes(4)
btn3 = BinaryTreeNodes(5)

btn1.left = btn2
btn1.right = btn3
printTree(btn1)