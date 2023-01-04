# username - complete info
# id1      - 206840126
# name1    - Omer Palevitch
# id2      - 207909409
# name2    - elad shaba

# delete printtree and reper
# after delete check concat
# arrange where each help function is
import math
import random
import printree
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
        self.size = 1

    def __repr__(self):
        return "(" + str(self.value) + ")"

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    # O(1)
    def getLeft(self):
        return self.left

    """returns the right child
    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    # O(1)
    def getRight(self):
        return self.right

    """returns the parent 
    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    # O(1)
    def getParent(self):
        return self.parent

    """return the value
    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    # O(1)
    def getValue(self):
        return self.value

    """returns the height
    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    # O(1)
    def getHeight(self):
        return self.height

    """sets left child
    @type node: AVLNode
    @param node: a node
    """

    # O(1)
    def setLeft(self, node):
        self.left = node

    """sets right child
    @type node: AVLNode
    @param node: a node
    """

    # O(1)
    def setRight(self, node):
        self.right = node

    """sets parent
    @type node: AVLNode
    @param node: a node
    """

    # O(1)
    def setParent(self, node):
        self.parent = node

    """sets value
    @type value: str
    @param value: data
    """

    # O(1)
    def setValue(self, value):
        self.value = value

    """sets the balance factor of the node
    @type h: int
    @param h: the height
    """

    # O(1)
    def setHeight(self, h):
        self.height = h

    """returns whether self is not a virtual node 
    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    # O(1)
    def isRealNode(self):
        if (self.height == -1):
            return False
        return True

    # O(1)
    def getbalance(self):
        lh = self.left.height
        rh = self.right.height
        return lh - rh

    # O(1)
    def getSize(self):
        return self.size

    # O(1)
    def setSize(self, s):
        self.size = s

    """finding successor of node
        @rtype: AVLNode
        """

    # O(log n)
    def succsesor(self):
        if (self.right.isRealNode()):
            node = self.right
            while (node.left.isRealNode()):
                node = node.left
        elif (self.getParent() == None):
            return None
        else:
            node = self
            while (node.getParent() != None):
                node = node.parent
                if (node.if_node_is_left_child):
                    break
        return node

    # O(1)
    def if_node_is_left_child(self):
        if (self.getParent() == None):
            return False
        else:
            parent = self.getParent()
        if (parent.left.value == self.value):
            return True
        else:
            return False

    # O(1)
    def if_node_is_right_child(self):
        if (self.getParent() == None):
            return False
        else:
            parent = self.getParent()
        if (parent.right.value == self.value):
            return True
        else:
            return False

    # O(1)
    def replace_to_virtual(self):
        node = AVLNode(None)
        node.size = 0
        node.height = -1
        return node


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
        self.min = None
        self.max = None

    def __repr__(self):  # no need to understand the implementation of this one
        out = ""
        for row in printree(self.root):  # need printree.py file
            out = out + row + "\n"
        return out

    """returns whether the list is empty
    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    # O(1)
    def empty(self):
        if (self.root == None):
            return True
        return False

    """retrieves the value of the i'th item in the list
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    # O(log n)
    def retrieve(self, i):
        if ((self.empty())or(i<0)or(i>(self.size-1))):
            return None
        else:
            node = self.TreeSelect(i + 1)
            return node.value

    """inserts val at position i in the list
    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    # O(log n)
    def insert(self, i, val):
        Vnode1 = AVLNode("intalizing").replace_to_virtual()  # create virtual Node
        Vnode2 = AVLNode("intalizing").replace_to_virtual()  # create virtual Node
        Node = AVLNode(val)  # create Node to insert
        Node.setLeft(Vnode1)
        Node.setRight(Vnode2)
        Vnode1.setParent(Node)
        Vnode2.setParent(Node)

        if (self.empty()):  # insert root when empty tree
            self.root = Node
            self.min = Node
            self.max = Node
            self.size = 1
            return 0

        if i == 0:  # insertFirst O(1)
            Parent = self.min
            Parent.setLeft(Node)
            self.min = Node
            Node.setParent(Parent)

        elif (i == self.size):  # insertLast
            Parent = self.max
            Parent.setRight(Node)
            self.max = Node
            Node.setParent(Parent)

        else:
            Parent = self.TreeSelect(i + 1)  # TreeSelect to find location
            if (not Parent.left.isRealNode()):  # dosent have left son
                Parent.setLeft(Node)
                Node.setParent(Parent)

            else:
                Parent = self.PredNode(Parent)
                Parent.setRight(Node)
                Node.setParent(Parent)

        self.FixHS(Node)
        rotations = self.CheckInsertion(Node)
        self.size += 1
        return rotations

    """deletes the i'th item in the list
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def help_tree(self, node):
        self.FixHS(node)
        rotations = self.CheckInsertion(node)
        return rotations

    # O(log n)
    def delete(self, i):
        if (self.empty()):
            return -1
        if ((self.size == 1) & (i == 0)):
            self.root = None
            self.max = None
            self.min = None
            return 0
        if((i>(self.size-1))or(i<0)):
            return -1
        self.size -= 1
        node = self.TreeSelect(i + 1)
        # if node is min, we take his secssesor
        if (self.min == node):
            self.min = node.succsesor()
        # if node is max, we find the next max
        if (self.max == node):
            if (node.left.isRealNode() == False):
                self.max = node.parent
            else:
                node_2 = node.getLeft()
                while (node_2.right.isRealNode() == True):
                    node_2 = node_2.getRight()
                self.max = node_2
        # check if leaf
        if ((node.left.isRealNode() == False) & (node.right.isRealNode() == False)):
            if (node.if_node_is_left_child()):
                parent = node.parent
                parent.left = node.replace_to_virtual()
            else:
                parent = node.parent
                parent.right = node.replace_to_virtual()
            return self.help_tree(parent)
        # only left child
        elif ((node.left.isRealNode() != False) & (node.right.isRealNode() == False)):
            if (node.getParent() == None):
                self.root = node.left
                node.left.parent = None
                node.left = node.replace_to_virtual()
                self.root.parent = None
                return self.help_tree(self.root)
            elif (node.if_node_is_left_child()):
                parent = node.parent
                parent.left = node.left
                node.left.parent = parent
                parent.left.parent = parent
                return self.help_tree(parent)
            elif (node.if_node_is_right_child()):
                parent = node.parent
                parent.right = node.left
                node.left.parent = parent
                parent.right.parent = parent
                return self.help_tree(parent)
        # only right child
        elif ((node.left.isRealNode() == False) & (node.right.isRealNode() != False)):
            if (node.getParent() == None):
                self.root = node.right
                node.right.parent = None
                node.right = node.replace_to_virtual()
                self.root.parent = None
                return self.help_tree(self.root)
            elif (node.if_node_is_left_child()):
                parent = node.parent
                parent.left = node.right
                parent.left.parent = parent
                return self.help_tree(parent)
            elif (node.if_node_is_right_child()):
                parent = node.parent
                parent.right = node.right
                parent.right.parent = parent
                return self.help_tree(parent)
        # 2 children
        else:
            # we will replace with succsesor, who is leaf or have right child (left is not possible)
            succsesor = node.succsesor()
            if (succsesor == None):
                return 0

            # sucssesor is a leaf
            if ((succsesor.left.isRealNode() == False) & (succsesor.right.isRealNode() == False)):
                if (succsesor.if_node_is_left_child()):
                    node.value = succsesor.value
                    parent = succsesor.parent
                    parent.left = node.replace_to_virtual()
                    parent.left.parent = node.replace_to_virtual()
                    return self.help_tree(parent)
                elif (succsesor.if_node_is_right_child()):
                    node.value = succsesor.value
                    parent = succsesor.parent
                    parent.right = node.replace_to_virtual()
                    parent.right.parent = node.replace_to_virtual()
                    return self.help_tree(parent)
                elif (succsesor.getParent() == None):
                    return None
            # sucssesor have right child
            else:
                if (succsesor.if_node_is_left_child()):
                    node.value = succsesor.value
                    parent = succsesor.parent
                    parent.left = succsesor.right
                    succsesor.right.parent = parent
                    return self.help_tree(parent)
                elif (succsesor.if_node_is_right_child()):
                    node.value = succsesor.value
                    parent = succsesor.parent
                    parent.right = succsesor.right
                    succsesor.right.parent = parent
                    return self.help_tree(parent)
                elif ((succsesor.getParent() == None)):
                    self.root = succsesor.right
                    succsesor.right.parent = None
                    succsesor.right = node.replace_to_virtual()
                    self.root.parent = None
                    return self.help_tree(self.root)


    """returns the value of the first item in the list
    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    # O(1)
    def first(self):
        return self.min.value

    """returns the value of the last item in the list
    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    # O(1)
    def last(self):
        return self.max.value

    """returns an array representing list 
    @rtype: list
    @returns: a list of strings representing the data structure
    """

    # O(n)
    def listToArray(self):
        if self.size == 0:
            return None
        arr = []
        self.inOrder(self.root, arr)
        return arr

    # travel the Tree inorder, add each element to the array
    # O(1)
    def inOrder(self, node, arr):
        if (node is None or not node.isRealNode()):
            return
        self.inOrder(node.left, arr)
        arr.append(node.value)
        self.inOrder(node.right, arr)

    """returns the size of the list 
    @rtype: int
    @returns: the size of the list
    """

    # O(1)
    def length(self):
        return self.size

    """sort the info values of the list
    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    # O(nlogn)
    def sort(self):
        arr = self.listToArray()
        arr = self.mergeSort(arr, 0, len(arr) - 1)
        sortedTree = AVLTreeList()
        for i in range(len(arr)):
            sortedTree.insert(i, arr[i])
        return sortedTree

    """permute the info values of the list 
    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    """

    # O(n)
    def permutation(self):
        perm = self.listToArray()  # O(n)
        self.ShuffleList(perm)  # O(n)
        shuffeldTree = AVLTreeList()
        shuffeldTree.root = shuffeldTree.BuildTree(perm, 0, len(perm) - 1)
        shuffeldTree.min = shuffeldTree.findMaxMin(False)  # O(log n)-find rightmost
        shuffeldTree.max = shuffeldTree.findMaxMin(True)  # O(log n)-find leftmost
        shuffeldTree.size = shuffeldTree.root.size
        return shuffeldTree

    """concatenates lst to self
    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    # O(log n) -> O(h2-h1+1)
    def concat(self, lst):
        # First we will handle the case if one of the "lists" is empty
        if (self.size == 0):
            self = lst
            return self.root.height

        if (lst.size == 0):
            return self.root.height

        hdiff = abs(self.root.height - lst.root.height)

        # we will handle the simple case - if one of them is of length 1
        if (lst.size == 1 or self.size == 1):
            if (lst.size == 1):
                self.insert(self.size, lst.root.value)
                self.max = lst.root.value
                return hdiff
            if (self.size == 1):
                lst.insert(0, self.root.value)
                lst.min = self.root.value
                self = lst
                return hdiff

        x = self.max
        self.delete(self.length() - 1)
        x.parent = None

        if (self.root.height == lst.root.height):  # same height, "simple" to connect
            x.setLeft(self.root)
            self.root.parent = x
            x.setRight(lst.root)
            lst.root.parent = x
            self.FixHS(x)
            self.root = x
            self.max = lst.max
            self.size = self.size + 1 + lst.size


        elif (self.root.height > lst.root.height):
            self.joinSmaller(x, lst)
            self.CheckInsertion(x)

        elif (self.root.height < lst.root.height):
            self.joinBigger(x, lst)
            self.CheckInsertion(x)

        return hdiff

    """searches for a *value* in the list
    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    # O(n)
    def search(self, val):
        arr = self.listToArray()
        if(arr == None):
            return -1
        for i in range(len(arr)):
            if (arr[i] == val):
                return i
        return -1

    """returns the root of the tree representing the list
    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    # O(1)
    def getRoot(self):
        return self.root

    # help functions:

    # O(1) fix Height and size of the Node
    def FixHS(self, node):
        node.height = 1 + max(node.left.height, node.right.height)
        node.size = node.left.size + node.right.size + 1

    # Find Predecessor- O(log n)
    def PredNode(self, Node):
        if (Node.left.isRealNode()):
            pred = Node.left
            while (pred.right.isRealNode()):
                pred = pred.right
            return pred
        Parent = Node.parent
        while Parent.isRealNode() and Node is Parent.left:
            Node = Parent
            Parent = Node.parent
        return Parent

    # find the "max" or "min" node of the tree-O(log n)
    def findMaxMin(self, Max=True):
        node = self.root
        if (Max):
            while node.getRight().isRealNode():
                node = node.getRight()
            return node

        else:
            while node.getLeft().isRealNode():
                node = node.getLeft()
            return node

    # O O(log n)
    def TreeSelect(self, k):

        return self.TreeSelectRec(self.root, k)

    def TreeSelectRec(self, x, k):
        r = x.left.size + 1
        if (k == r):
            return x
        if (k < r):
            return self.TreeSelectRec(x.left, k)
        else:
            return self.TreeSelectRec(x.right, k - r)

    # O(log n) - fix tree and rotate if need after insertion
    # as we check if rotations are needed, we will fix the parameters of the nodes
    def CheckInsertion(self, curr):
        rotations = 0
        while curr is not None and curr.isRealNode():
            self.FixHS(curr)  # fix height and size of the nodes

            bal = curr.getbalance()

            if bal <= -2:
                if curr.right.getbalance() == 1:
                    self.rightRotate(curr.right)
                    self.FixHS(curr.right)
                    self.leftRotate(curr)
                    self.FixHS(curr)
                    rotations += 2

                else:
                    self.leftRotate(curr)
                    self.FixHS(curr)
                    rotations += 1



            elif (bal >= 2):
                if curr.left.getbalance() == -1:
                    self.leftRotate(curr.left)
                    self.FixHS(curr.left)
                    self.rightRotate(curr)
                    self.FixHS(curr)
                    rotations += 2
                else:
                    self.rightRotate(curr)
                    self.FixHS(curr)
                    rotations += 1

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
    # O(1)
    def leftRotate(self, A):
        temp = None
        if (A.getParent != None):  # edge case for root of tree
            temp = A.getParent()
        B = A.right
        BL = B.left
        A.setRight(BL)
        BL.setParent(A)
        B.setLeft(A)
        A.setParent(B)
        if (temp != None):
            B.setParent(temp)
            if (temp.right == A):
                temp.setRight(B)
            else:
                temp.setLeft(B)
        else:
            self.root = B
            B.parent = None

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

    # O(1)
    def rightRotate(self, B):
        temp = None
        if (B.getParent != None):  # edge case for root of tree
            temp = B.getParent()

        A = B.left
        AR = A.right
        B.setLeft(AR)
        AR.setParent(B)
        A.setRight(B)
        B.setParent(A)
        if (temp != None):
            A.setParent(temp)
            if (temp.right == B):
                temp.setRight(A)
            else:
                temp.setLeft(A)
        else:
            self.root = A
            A.parent = None
        self.FixHS(B)
        self.FixHS(A)

    # help funciton for join- find first node with required height - O(log n)
    def findOnLeftFirstH(self, h):
        node = self.root
        while (node.left.isRealNode and node.height > h):
            node = node.left
        return node

    # help funciton for join- find first node with required height - O(log n)
    def findOnRightFirstH(self, h):
        node = self.root
        while (node.right.isRealNode and node.height > h):
            node = node.right
        return node

    # O(log n)
    def joinSmaller(self, x, T2):  # T1=self is bigger --> T1<x<T2 and |T1|>|T2|
        Connect = self.findOnRightFirstH(T2.root.height)
        x.setLeft(Connect)
        x.setRight(T2.root)
        self.max = T2.max
        self.size = self.size + 1 + T2.size
        if (Connect is not self.root):
            x.setParent(Connect.parent)
            Connect.parent.right = x
            Connect.parent = x
        T2.root.parent = x

    # # O(log n)
    def joinBigger(self, x, T2):  # T1=self is smaller--> T1<x<T2 and |T1|<|T2|
        Connect = T2.findOnLeftFirstH(self.root.height)
        x.setLeft(self.root)
        x.setRight(Connect)
        self.max = T2.max
        self.size = self.size + 1 + T2.size
        if (Connect is not T2.root):
            x.setParent(Connect.parent)
            Connect.parent.left = x
            Connect.parent = x
        self.root.parent = x
        self.root = T2.root

    # O(n)
    def ShuffleList(self, lst):
        index = len(lst) - 1

        while index > 0:
            randInd = random.randint(0, index)
            lst[index], lst[randInd] = lst[randInd], lst[index]
            index = index - 1

        return lst

    # O(n)
    # we will build as we saw in the rec from "sorted" array

    def BuildTree(self, lst, left, right):

        if right < left:
            node = AVLNode("intalizing").replace_to_virtual()  # create virtual Node
            return node
        mid = (left + right) // 2  # take median of list
        node = AVLNode(lst[mid])
        node.setLeft(self.BuildTree(lst, left, mid - 1))  # rec left
        node.setRight(self.BuildTree(lst, mid + 1, right))  # rec right
        self.FixHS(node)
        node.getRight().setParent(node)
        node.getLeft().setParent(node)
        return node

    # helper for mergesort
    # O(n log n)
    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    # l is for left index and r is right index of the
    # sub-array of arr to be sorted

    # O(n log n)
    def mergeSort(self, arr, l, r):
        if l < r:
            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            m = l + (r - l) // 2

            # Sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)
        return arr

    def append(self, val):
        self.insert(self.length(), val)

    def getTreeHeight(self):
        return self.root.height


# T = AVLTreeList()
# L = []
#
# for i in range(20):
#     if i % 3 == 0:
#         T.insert(T.length()//2, i)
#         x= T.listToArray()
#         print(T.listToArray())
#         L.insert(len(L)//2, i)
#     elif i % 3 == 1:
#         T.insert(0, i)
#         x = T.listToArray()
#         print(T.listToArray())
#         L.insert(0, i)
#     else:
#         T.delete(T.length()//2)
#         L.pop(len(L)//2)
