# this module contains the binary search tree data 

class binaryTreeNode:
    """ Creates a node for the tree"""
    def __init__(self, data):
        self.parent = None
        self.key = data
        self.left = None
        self.right = None
        
class binarSearchTree:
    def __init__(self):
        """create the empty binary search tree"""
        self.root = None
        
    def insertNode(self, data):
        """ Add the node to the tree"""
        new_node = binaryTreeNode(data)
        temp = self.root
        if temp != None:
            # find the node where the new node will be
            while temp != None:
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
        """ return the minimum of the subtree rooted at node:
        go to the left till u reach the leaf node and print the leaf node """
        if node != None:
            while node.left != None:
                node = node.left
            return node.key
        else:
            print("Tree is empty")
            
        
    
    def maximum(self, node):        
        """ Return the maximum of the subtree rooted at node: 
        go right to the tree till u reach the leaf then print the leaf"""
        if node != None:
            while node.right != None:
                node = node.right
            return node.key
        else:
            print("tree is empty")
            
    def search(self, data):        
        """ it return the node whose key matches the given data """
        temp = self.root
        while temp != None:
            if data == temp.key:
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
        i.e. first print the root then left subtree then right subtree"""
        if x != None:
            print(x.key)
            self.preorder(x.left)
            self.preorder(x.right)
            
    def inorder(self, x):
        """ Return the inorder given the Node:
        i.e. first print the left subtree then root and then the right subtree"""
        if x != None:
            self.inorder(x.left)
            print(x.key)
            self.inorder(x.right)
            
    def postorder(self, x):
        """ Return the postorder given the node: 
        i.e. first print the left subtree then right subtree and then the root """
        if x != None:
            self.postorder(x.left)
            self.postorder(x.right)
            print(x.key)
            
    def sucessor(self, data):
        """ Return the key of predcessor of the given data """
        
        # search for the node which has the matching key
        x = self.search(data)
        
        # if it has the right child
        if x.right != None:
            
            # return the maximum of the tree rooted at right child of the node
            return self.minimum(x.right)
        else:
            
            # if it does not have the right child then search for the node
            # which is left child of its parent and return its parent
            y = x.parent
            while y != None and x != y.left:
                x = y
                y = y.parent
                
            try:
                return y.key
            except:
                print("given data is maximum")
                
    def predcessor(self, data):
        """ Return the key of sucessor of the given data """
        
        # search for the node with the matching key
        x = self.search(data)
        
        # if it has left child
        if x.left != None:
            # return the maximum of the tree rooted at the x.left
            return self.maximum(x.left)
        else:
            
            # if it doesnot has the left child
            # find the node which is the right child of its parent and return the parent of the node
            y = x.parent
            while y != None and y.right != x:
                x = y
                y = y.parent
                
            try:
                return y.key
            except:
                print("give data is minimum")
                
    def transplant(self, u, v):
        """replaces subtree rooted at u to subtree rooted at v"""
        
        # if u is root node
        if u.parent == None:
            self.root = v
        
        # if u is left child of its parent   
        elif u == u.parent.left:
            u.parent.left = v
        
        # if u is right child of its parent
        else:
            u.parent.right = v
            
        # change the parent of the v to parent of u   
        if v != None:
            v.parent = u.parent
            
    def deleteNode(self, data):
        """ Delete the node which matches the given data """
        
        # serch for the node which has the given data
        u = self.search(data)
        
        # if the node has no left child replace it with its right child
        if u.left == None:
            self.transplant(u, u.right)
        
        # if it does not have the right child replace it with the right child
        elif u.right == None:
            self.transplant(u, u.left)
        
        # if it has both the child
        else:
            
            # find its sucessor
            y = self.minimum(u.right)
            
            # if it is not the imidiate child if the node to be deleted
            if y.parent != z:
                
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
            
            