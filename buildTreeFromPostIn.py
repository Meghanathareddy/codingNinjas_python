class BinaryTreeNodes:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def buildTreeFromPostIn(post, inorder):

    if len(post) == 0:
        return None
    
    rootData = post[-1]
    root = BinaryTreeNodes(rootData)
    rootIndexInInorder = -1
    for i in range(0, len(inorder)):
        if inorder[i] == rootData:
            rootIndexInInorder = i
            break
    if rootIndexInInorder == -1:
        return None

    leftInorder = inorder[0:rootIndexInInorder]
    rightInorder = inorder[rootIndexInInorder+1:]

    lenLeftSubtree = len(leftInorder)

    leftPostOrder = post[0:lenLeftSubtree]
    rightPostOrder = post[lenLeftSubtree:-1]

    leftChild = buildTreeFromPostIn(leftPostOrder, leftInorder)
    rightChild = buildTreeFromPostIn(rightPostOrder, rightInorder)
    root.left = leftChild
    root.right = rightChild
    return root

def printLevelOrder(root):

    #Base case
    if root is None:
        return
    
    #create an empty queue for level order treaversal
    q = []

    #Enqueue root and initialize height
    q.append(root)

    while q:

        #nodeCount (queue size ) indicates number 
        #of nodes at current level
        count = len(q)
        # Dequeue all nodes of current level
        #Enqueue all nodes of next level

        while count > 0:
            temp = q.pop(0)
            print(temp.data, end = " ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            
            count -= 1
        print(' ')

post = [9,1,2,12,7,5,3,11,4,8]
inorder = [9,5,1,7,2,12,8,4,3,11]
root = buildTreeFromPostIn(post, inorder)
printLevelOrder(root)
