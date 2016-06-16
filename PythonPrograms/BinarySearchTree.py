#binary search tree
#Node class
#1)key,value,leftchild,rightchild,insert,delete,search
#Tree class

Class TreeNode:
    def _init_(self,val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def insert(self,data):
        if self.val==data:
            return False
        elif self.val > data:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild =TreeNode(data)
                return True
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = TreeNode(data)
                return True

    def search(self,data):
        if self.val==data:
            return True
        elif self.val > data:
            if self.leftchild:
                return self.leftChild.search(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.search(data)
            else:
                return False

    def preorder(self):
        if self:
            print (str(self.val))
            if self.leftChild:
                self.leftChild.preorder()
            else:
                self.rightChild.preorder()
    def postorder(self):
        if self:
            if self.lefttChild:
                self.leftChild.postorder()
            else:
                self.rightChild.postorder()
            print str(self.val)
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print str(self.val)
            if self.rightChild():
                self.rightChild.inorder()
class BinarySearchTree:
    def __init__(self):
        self.root =None

    def insert(self,data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = TreeNode(data)
            return True

    def search(self,data):
        if self.root:
            return self.root.search(data)
        else:
            return False
        
    def remove(self,data):
        #if tree is empty
        if self.root is None:
            return False
        elif self.root.val ==data:
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root =None
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.root.rightChild
            elif self.root.leftChild and self.root.rightChild:
                removeParent = self.root
                removeNode = self.root.rightChild
                while removeNode.leftChild:
                    removeParent =removeNode
                    removeNode =removeNode.leftChild
                self.root.val = removeNode.value
                if removeNode.rightChild:
                    removeParent.leftChild = removeNode.rightChild
                else:
                    removeParent.leftChild = None
            return True
        parent =None
        node = self.root
         # find the node to remove
        while node and node.value !=data:
            parent = node
            if data < node.value:
                node = node.leftChild
            else:
                node = node.rightChild
                
        # no data found
        if node is None or node.value !=data:
            return False
        # remove node dat has no child
        elif node.rightChild is None and node.leftChild is None:
            if data < parent.value

####################
            # case 2: remove-node has no children
		elif node.leftChild is None and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = None
			else:
				parent.rightChild = None
			return True
			
		# case 3: remove-node has left child only
		elif node.leftChild and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = node.leftChild
			else:
				parent.rightChild = node.leftChild
			return True
			
		# case 4: remove-node has right child only
		elif node.leftChild is None and node.rightChild:
			if data < parent.value:
				parent.leftChild = node.rightChild
			else:
				parent.rightChild = node.rightChild
			return True
			
		# case 5: remove-node has left and right children
		else:
			delNodeParent = node
			delNode = node.rightChild
			while delNode.leftChild:
				delNodeParent = delNode
				delNode = delNode.leftChild
				
			node.value = delNode.value
			if delNode.rightChild:
				if delNodeParent.value > delNode.value:
					delNodeParent.leftChild = delNode.rightChild
				elif delNodeParent.value < delNode.value:
					delNodeParent.rightChild = delNode.rightChild
			else:
				if delNode.value < delNodeParent.value:
					delNodeParent.leftChild = None
				else:
					delNodeParent.rightChild = None

	def preorder(self):
		if self.root is not None:
			print("PreOrder")
			self.root.preorder()
        
	def postorder(self):
		if self.root is not None:
			print("PostOrder")
			self.root.postorder()
			
	def inorder(self):
		if self.root is not None:
			print("InOrder")
			self.root.inorder()

bst = Tree()
print(bst.insert(10))

bst.preorder()
#bst.postorder()
#bst.inorder()
print(bst.remove(10))
bst.preorder()
Status 
        
                
                
            
        
                
                
            
        
        
    
    
                
                
                
            
        
