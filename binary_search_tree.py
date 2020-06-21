# this module contains the binary search tree data 

class binaryTreeNode:
    
    """
    Class to create the Node for Binary Search Tree.
    
    Attributes:
        parent(object of the same class): Parent of the node
        key(object): key for the node
        left(object of the same class): Left child of the node
        right(object of the same class): Right child of the node
    """
    def __init__(self, data):
        """
        Initialize the object of binaryTreeNode class
        with parent, left, right = None and key with provided data.
        
        Parameters:
            data(object): Key for the node
        
        """
        self.parent = None
        self.key = data
        self.left = None
        self.right = None
    
    def __str__(self):
        """
        Returns the string representation of the object
        """
        return "Node for Binary Search Tree with key: {}".format(self.key)
    
class binarySearchTree:
    """
    This is the class to create Binary Search Tree object.
    
    Attributes:
        root(object of binaryTreeNode class): Root of the Binary Search Tree.
    """
    def __init__(self):
        """initialize the binary search tree with root None"""
        self.root = None
        
    def __str__(self):
        """
        Returns the string representation of object.
        """
        return "Binary Search Tree with root node key: {}".format(self.root.key) if self.root != None else "Empty Binary Search Tree"
        
    def insertNode(self, data):
        """
        Insert a node in tree.
        
        Parameters:
            data: key for the node you want to insert in your tree.
        """
        new_node = binaryTreeNode(data)
        temp = self.root
        if temp is not None:
            # find the node where the new node will be
            while temp is not None:
                if data <= temp.key:
                    prev = temp
                    temp = temp.left
                else:
                    prev = temp
                    temp = temp.right                
            # insert the node      
            new_node.parent = prev       
            if data <= prev.key:
                prev.left = new_node
            else:
                prev.right = new_node
        
        else:
            self.root = new_node
            
    def minimum(self, node):
        """ 
        Return the minimum of the subtree rooted at node.
        
        parameter:
        node(object of binaryTreeNode): root of the tree minimum of which you want to compute. """
        if node is not None:
            while node.left is not None:
                node = node.left
            return node.key
        else:
            print("Tree is empty")
            
        
    
    def maximum(self, node):        
        """ 
        Return the maximum of the subtree rooted at node.
        
        parameter:
        node(object of binaryTreeNode): root of the tree maximum of which you want to compute.
        """
        if node is not None:
            while node.right is not None:
                node = node.right
            return node.key
        else:
            print("tree is empty")
            
    def search(self, data):        
        """ It return the node whose key matches the given data.
        
        Parameters:
        data: key of the node which u want to search
        """
        temp = self.root
        while temp is not None:
            if data is temp.key:
                break
            elif data < temp.key:
                temp = temp.left                
            else:
                temp = temp.right
        else:
            print("key Not found")
        return temp
    
    def preorder(self, x):
        """ Return the preorder given the node 
        i.e. first print the root then left subtree then right subtree
        
        Parameter:
        x : Root of the tree for which you want to compute the preorder. 
        """
        if x is not None:
            print(x.key)
            self.preorder(x.left)
            self.preorder(x.right)
            
    def inorder(self, x):
        """ Return the inorder given the Node:
        i.e. first print the left subtree then root and then the right subtree
        
        Parameter:
        x: Root of the tree for which u want to compute the inorder.
        """
        if x is not None:
            self.inorder(x.left)
            print(x.key)
            self.inorder(x.right)
            
    def postorder(self, x):
        """ Return the postorder given the node: 
        i.e. first print the left subtree then right subtree and then the root 
        
        Parameter:
        x: Root of the tree for which u want to compute the postorder.
        """
        if x is not None:
            self.postorder(x.left)
            self.postorder(x.right)
            print(x.key)
            
    def sucessor(self, data):
        """ Return the key of sucessor of the given data.
        
        Parameter:
        data: Key of the node for which u want to compute the sucessor.
        """
        
        # search for the node which has the matching key
        x = self.search(data)
        
        # if it has the right child
        if x.right is not None:
            
            # return the maximum of the tree rooted at right child of the node
            return self.minimum(x.right)
        else:
            
            # if it does not have the right child then search for the node
            # which is left child of its parent and return its parent
            y = x.parent
            while y is not None and x is not y.left:
                x = y
                y = y.parent
                
            try:
                return y.key
            except:
                print("given data is maximum")
                
    def predcessor(self, data):
        """ 
        Return the key of sucessor of the given data 
        
        Parameter:
        data: Key of the node for which u want to compute the predcessor.
        """
        
        # search for the node with the matching key
        x = self.search(data)
        
        # if it has left child
        if x.left is not None:
            # return the maximum of the tree rooted at the x.left
            return self.maximum(x.left)
        else:
            
            # if it doesnot has the left child
            # find the node which is the right child of its parent and return the parent of the node
            y = x.parent
            while y is not None and y.right is not x:
                x = y
                y = y.parent
                
            try:
                return y.key
            except:
                print("give data is minimum")
                
    def transplant(self, u, v):
        """Replaces subtree rooted at u to subtree rooted at v.
        
        Paraameters:
        u (object of class binaryTreeNode): Node which you want to remove.
        v (object of class binaryTreeNode): Node which you want to add.
        """
        
        # if u is root node
        if u.parent is None:
            self.root = v
        
        # if u is left child of its parent   
        elif u is u.parent.left:
            u.parent.left = v
        
        # if u is right child of its parent
        else:
            u.parent.right = v
            
        # change the parent of the v to parent of u   
        if v is not None:
            v.parent = u.parent
            
    def deleteNode(self, data):
        """ 
        Delete the node which matches the given data.
        
        Parameter:
        data: key of the node which u wnat to delete.
        """
        
        # serch for the node which has the given data
        u = self.search(data)
        
        # if the node has no left child replace it with its right child
        if u.left is None:
            self.transplant(u, u.right)
        
        # if it does not have the right child replace it with the right child
        elif u.right is None:
            self.transplant(u, u.left)
        
        # if it has both the child
        else:
            
            # find its sucessor
            y = self.minimum(u.right)
            
            # if it is not the imidiate child if the node to be deleted
            if y.parent is not z:
                
                # replace the y by its right child
                self.transplant(y, y.right)
                
                # make a new branch with the root as y and then add
                #the right child of the node to be deleted as its right child
                y.right = z.right
                y.right.parent = y
            
            # transplant z by y   
            self.transplant(z, y)
            
            # assigign the left child of z to the right child of y
            y.left = z.left
            y.left.parent = y
       
    def heightOfTree(self, node):
        """
        Returns the height of the tree rooted at given node.
        
        Parameters:
        node(object of binaryTreeNode class): root of the tree whose height you want to compute
        """
        if node is None:
            return 0
        else:
            lheight = self.heightOfTree(node.left)
            rheight = self.heightOfTree(node.right)
            return lheight+1 if lheight > rheight else rheight + 1
        