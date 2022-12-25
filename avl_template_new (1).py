#username - complete info
#id1      - 206840126
#name1    - Omer Palevitch
#id2      - 207909409
#name2    - elad shaba 

#Todo:
#delete printtree and reper
#delete auto generated tree
#check to see that sizes and heights stay updated in big tree
#try to insert a lot of elements to tree and confirm no problems
#after delete check concat
#write time complexity for all
#arrange where each help function is


import random ##check if allowed
from printree import *
"""A class represnting a node in an AVL tree"""

class AVLNode(object):
        """Constructor, you are allowed to add more fields. 

        @type value: str
        @param value: data of your node
        """
        def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None
                self.parent = None
                self.height = 0 
                if(value==None):#virtual node
                        self.height=-1
                        self.size=0
                else:
                        self.size=1
                        
        def __repr__(self):
                return "(" + str(self.value) + ")"
                
        
        """returns the left child
        @rtype: AVLNode
        @returns: the left child of self, None if there is no left child
        """
        #O(1)
        def getLeft(self):
                return self.left
                


        """returns the right child

        @rtype: AVLNode
        @returns: the right child of self, None if there is no right child
        """
        #O(1)
        def getRight(self):
                return self.right
                

        """returns the parent 

        @rtype: AVLNode
        @returns: the parent of self, None if there is no parent
        """
        #O(1)
        def getParent(self):
                return self.parent

        """return the value

        @rtype: str
        @returns: the value of self, None if the node is virtual
        """
        #O(1)
        def getValue(self):
                return self.value

        """returns the height

        @rtype: int
        @returns: the height of self, -1 if the node is virtual
        """
        #O(1)
        def getHeight(self):
                return self.height

        """sets left child

        @type node: AVLNode
        @param node: a node
        """
        #O(1)
        def setLeft(self, node):
                self.left=node

        """sets right child

        @type node: AVLNode
        @param node: a node
        """
        #O(1)
        def setRight(self, node):
                self.right=node

        """sets parent

        @type node: AVLNode
        @param node: a node
        """
        #O(1)
        def setParent(self, node):
                self.parent=node

        """sets value

        @type value: str
        @param value: data
        """
        #O(1)
        def setValue(self, value):
                self.value=value

        """sets the balance factor of the node

        @type h: int
        @param h: the height
        """
        #O(1)
        def setHeight(self, h):
                self.height=h

        """returns whether self is not a virtual node 

        @rtype: bool
        @returns: False if self is a virtual node, True otherwise.
        """
        #O(1)
        def isRealNode(self):
                if (self.height==-1):
                        return False
                return True
        
        #O(1)
        def getbalance(self):
                lh = self.left.height
                rh = self.right.height
                return lh-rh
        #O(1)
        def getSize(self):
                return self.size
        #O(1)
        def setSize(self,s):
                self.size=s
        
                



"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

        """
        Constructor, you are allowed to add more fields.  

        """
        def __init__(self):
                self.size = 0
                self.root = None
                self.min=None
                self.max=None
                
        def __repr__(self): #no need to understand the implementation of this one
                out = ""
                for row in printree(self.root): #need printree.py file
                    out = out + row + "\n"
                return out


        """returns whether the list is empty

        @rtype: bool
        @returns: True if the list is empty, False otherwise
        """
        #O(1)
        def empty(self):
                if(self.root==None):
                        return True
                return False


        """retrieves the value of the i'th item in the list

        @type i: int
        @pre: 0 <= i < self.length()
        @param i: index in the list
        @rtype: str
        @returns: the the value of the i'th item in the list
        """
        def retrieve(self, i):
                return None

        """inserts val at position i in the list

        @type i: int
        @pre: 0 <= i <= self.length()
        @param i: The intended index in the list to which we insert val
        @type val: str
        @param val: the value we inserts
        @rtype: list
        @returns: the number of rebalancing operation due to AVL rebalancing
        """
        #O(log n)
        def insert(self, i, val):
                Vnode1=AVLNode(None)#create virtual Node
                Vnode2=AVLNode(None)#create virtual Node
                Node=AVLNode(val)#create Node to insert
                Node.setLeft(Vnode1)
                Node.setRight(Vnode2)
                Vnode1.setParent(Node)
                Vnode2.setParent(Node)
                
                if(self.empty()): #insert root when empty tree
                        self.root=Node
                        self.min=Node
                        self.max=Node
                        self.size=1
                        return 0
                
                if i==0: #insertFirst O(1)
                        Parent=self.min
                        Parent.setLeft(Node)
                        self.min=Node
                        Node.setParent(Parent) 
                        
                elif(i==self.size): #insertLast
                        Parent=self.max
                        Parent.setRight(Node)
                        self.max=Node
                        Node.setParent(Parent) 
                               
                else:
                        Parent=self.TreeSelect(i+1)#TreeSelect to find location
                        if(not Parent.left.isRealNode()): #dosent have left son
                                Parent.setLeft(Node)
                                Node.setParent(Parent) 
                                
                        else:
                                Parent=self.PredNode(Parent)
                                Parent.setRight(Node)
                                Node.setParent(Parent) 
                                               
                self.FixHS(Node)
                rotations=self.CheckInsertion(Node)
                self.size+=1
                return rotations
                


        """deletes the i'th item in the list

        @type i: int
        @pre: 0 <= i < self.length()
        @param i: The intended index in the list to be deleted
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
        """
        def delete(self, i):
                return -1


        """returns the value of the first item in the list

        @rtype: str
        @returns: the value of the first item, None if the list is empty
        """
        #O(1)
        def first(self):
                return self.min.value

        """returns the value of the last item in the list

        @rtype: str
        @returns: the value of the last item, None if the list is empty
        """
        #O(1)
        def last(self):
                return self.max.value

        """returns an array representing list 

        @rtype: list
        @returns: a list of strings representing the data structure
        """
        #O(n)
        def listToArray(self):
                if self.size==0:
                        return None
                arr=[]
                self.inOrder(self.root,arr)
                return arr
                

        # travel the Tree inorder, add each element to the array
        #O(1)
        def inOrder(self,node,arr):
                if(node is None or not node.isRealNode()):
                        return
                self.inOrder(node.left,arr)
                arr.append(node.value)
                self.inOrder(node.right,arr)
                

        """returns the size of the list 

        @rtype: int
        @returns: the size of the list
        """
        #O(1)
        def length(self):
                return self.size

        """sort the info values of the list

        @rtype: list
        @returns: an AVLTreeList where the values are sorted by the info of the original list.
        """
        def sort(self):
                return None


        """permute the info values of the list 

        @rtype: list
        @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
        """
        #O(n)
        def permutation(self):
                perm=self.listToArray()#O(n)
                self.ShuffleList(perm)#O(n)
                shuffeldTree=AVLTreeList()
                i=0
                shuffeldTree.root=self.buildTreeFromList(perm,0,len(perm)-1)
                shuffeldTree.min=AVLNode(perm[0])
                shuffeldTree.max=AVLNode(perm[len(perm)-1])
                shuffeldTree.size=shuffeldTree.root.size
                return shuffeldTree
                
        """concatenates lst to self

        @type lst: AVLTreeList
        @param lst: a list to be concatenated after self
        @rtype: int
        @returns: the absolute value of the difference between the height of the AVL trees joined
        """
        #O(log n) -> O(h2-h1+1) ?
        #check if work on lst.size==1 if not, just add as last element and rotate
        def concat(self, lst):
                
                if(self.size==0):
                        self=lst
                        lst=AVLTreeList()#check what happens to self and lst
                        return self.height
                if(lst.size==0):
                        return self.height
                
                hdiff=abs(self.root.height+1-lst.root.height)
                
                if(lst.size==1 or self.size==1): #we will sometimes be able to do the join on O(1) like so 
                        if(lst.size==1):
                                self.insert(self.size,lst.root.value)
                                self.max=lst.root.value
                                lst=AVLTreeList()#check what happens to self and lst
                                return hdiff
                        if(self.size==1):
                                lst.insert(0,self.root.value)
                                lst.min=self.root.value
                                self=lst
                                lst=AVLTreeList()#check what happens to self and lst
                                return hdiff
                        
                x=self.max.value
                self.delete(self.length()-1)
                if(hdiff<=1):
                        x.setLeft(self.root)
                        x.setRight(lst.root)
                        self.max=lst.max
                        self.root=x
                        self.size=self.size+1+lst.size
                        lst=AVLTreeList()#check what happens to self and lst
                        
                        
                if(self.height>lst.height):
                        self.joinSmaller(x,lst)
                        self.CheckInsertion(x,True)
                        #do rotations needed
                       
                        
                else:
                        self.joinBigger(x,lst)
                        self.CheckInsertion(x,True)
                        #do rotations needed
                        
                return hdiff

        """searches for a *value* in the list

        @type val: str
        @param val: a value to be searched
        @rtype: int
        @returns: the first index that contains val, -1 if not found.
        """
        def search(self, val):
                return None



        """returns the root of the tree representing the list

        @rtype: AVLNode
        @returns: the root, None if the list is empty
        """
        #O(1)
        def getRoot(self):
                return self.root
        
        ## Find Predecessor
        #O(log n)
        def PredNode(self,Node):
                if(Node.left.isRealNode()):
                        pred=Node.left
                        while(pred.right.isRealNode()):
                                pred=pred.right
                        return pred
                Parent = Node.parent
                while Parent.isRealNode() and Node is Parent.left:
                        Node = Parent
                        Parent = Node.parent
                return Parent

        #O O(log n)
        def TreeSelect(self,k):
                
                return self.TreeSelectRec(self.root,k)
        
        def TreeSelectRec(self,x,k):
                r=x.left.size+1
                if(k==r):
                        return x
                if(k<r):
                        return self.TreeSelectRec(x.left,k)
                else:
                        return self.TreeSelectRec(x.right,k-r)

        #O(log n)
        # as we check if rotations are needed, we will fix the parameters of the nodes
        def CheckInsertion(self,curr):
                rotations = 0
                while curr is not None and curr.isRealNode():
                        self.FixHS(curr)# fix height and size of the nodes
                        bal=curr.getbalance()
                        
                        if bal == -2:
                                if curr.right.getbalance() <=0:
                                        self.leftRotate(curr)
                                        self.FixHS(curr)
                                        rotations+= 1
                                
                                else:
                                        self.rightRotate(curr.right)
                                        self.FixHS(curr.right)
                                        self.leftRotate(curr)
                                        self.FixHS(curr)
                                        rotations+= 2
                        
                                return 1
                        elif (bal == +2):
                                if curr.left.getbalance() > -1: 
                                        self.rightRotate(curr)
                                        self.FixHS(curr)
                                        rotations+= 1
                                else:
                                        self.leftRotate(curr.left)
                                        self.FixHS(curr.left)
                                        self.rightRotate(curr)
                                        self.FixHS(curr)
                                        rotations+= 2
                        curr = curr.parent
                return rotations

        
  #             left Rotate:                 
  #       A                   B
  #      / \                 / \
  #     AL  B               A   BR
  #        / \       ->    / \   \
  #       BL  BR          AL BL  V
  #            \
  #             v 
        #O(1)
        def leftRotate(self,A):
               temp=None
               if(A.getParent!=None): #edge case for root of tree
                       temp=A.getParent()
               B=A.right
               BL=B.left
               A.setRight(BL)
               BL.setParent(A)
               B.setLeft(A)
               A.setParent(B)
               if(temp!=None):
                       B.setParent(temp)
                       if(temp.right==A):
                               temp.setRight(B)
                       else:
                               temp.setLeft(B)
               else:
                       self.root=B
                       B.parent=None
                
               self.FixHS(A)
               self.FixHS(B)

                                
  #             Right Rotate:                 
  #       B                   A
  #      / \                 / \
  #     A   BR              AL  B
  #    / \       ->        /   / \
  #   AL  AR              v   AR  BR
  #  /
  # v
        #O(1)
        def rightRotate(self,B):
               temp=None
               if(B.getParent!=None): #edge case for root of tree
                        temp=B.getParent()
                
               A=B.left
               AR=A.right
               B.setLeft(AR)
               AR.setParent(B)
               A.setRight(B)
               B.setParent(A)
               if(temp!=None):
                       A.setParent(temp)
                       if(temp.right==B):
                               temp.setRight(A)
                       else:
                               temp.setLeft(A)
               else:
                       self.root=A
                       A.parent=None
               self.FixHS(B)
               self.FixHS(A)
                       
        #O(log n)
        def FixHS(self,node):
                node.height=1+max(node.left.height,node.right.height)
                node.size = node.left.size + node.right.size + 1

        #O(n)
        def ShuffleList(self,lst):
              indexL=len(lst)-1

              while indexL > 0:
                  randomIndex = random.randint(0, indexL)
                  lst[indexL],lst[randomIndex]=lst[randomIndex],lst[indexL]
                  indexL = indexL- 1

              return lst

        
        #O(log n)
        def findFirstH(self,h):
                node=self.root
                while(node.height>h):
                        node=node.left
                return node
                        
        #O(log n)        
        def joinSmaller(T1,x,T2): #self is bigger
                Connect=T1.findFirstH(T2.root.height)
                x.setLeft(Connect)
                x.setRight(T2.root)
                T1.max=T2.max
                T1.size=self.size+1+lst.size
                x.setParent(Connect.parent)
                Connect.parent=x
                T2=AVLTreeList()#check what happens to self and lst
        #O(log n)
        def joinBigger(T1,x,T2): ##self is smaller
                Connect=T2.findFirstH(T1.root.height)
                x.setLeft(T1.root)
                x.setRight(Connect)
                T1.max=T2.max
                T1.size=self.size+1+lst.size
                x.setParent(Connect.parent)
                Connect.parent=x
                T2=AVLTreeList()#check what happens to self and lst

        #O(n)
        #we will build as we saw in the rec
        def buildTreeFromList(self,lst, left, right):
	# if right < left then we return a virtual node
                if right < left:
                        return AVLNode(None)

	# create a node from the center of the list so that the tree will be most balanced
                mid = (left + right) // 2
                node = AVLNode(lst[mid])

	# build left subtree of node
                node.setLeft(self.buildTreeFromList(lst, left, mid - 1))

	# build right subtree of node
                node.setRight(self.buildTreeFromList(lst, mid + 1, right))

	# update parameters of node
                self.FixHS(node)

	# setting node as parent for left and right children
                if node.getRight().isRealNode():
                        node.getRight().setParent(node)
                if node.getLeft().isRealNode():
                        node.getLeft().setParent(node)
                return node
                
                
                
t=AVLTreeList()
for i in range(10):
        t.insert(0,(str)(i))
        







