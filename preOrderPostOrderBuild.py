def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #If there's nothing, return nothing
        if len(inorder) == 0:
            return None
        #If there's only one element all we need to do is create the node and return it
        if len(inorder) == 1:
            return TreeNode(preorder.pop(0))
        else:
            #The first element in the preorder list is always the root
            root = preorder.pop(0)
            #Use the inorder list to figure out left and right subtrees
            rootIndex = inorder.index(root)
            #Create the left and right inorder lists to pass down
            lInorder, rInorder = inorder[:rootIndex], inorder[rootIndex+1:]
            #Because we always pop off the first element in the preorder: we can pass it
            #as-is because we call left first and then right. The first element will always be
            #correct
            #Create the new node and calculate its children
            rootNode = TreeNode(root)
            rootNode.left = self.buildTree(preorder, lInorder)
            rootNode.right = self.buildTree(preorder, rInorder)
            return rootNode