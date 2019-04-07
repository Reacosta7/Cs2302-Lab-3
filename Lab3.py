# Code to implement a binary search tree 
# Programmed by Olac Fuentes
# Last modified February 27, 2019
import numpy as np
import matplotlib.pyplot as plt
import math 
"""
def circle(center,rad):
    n = int(4*rad*math.pi)    
    t = np.linspace(0,6.3,n)      
    x = center[0]+rad*np.sin(t)   
    y = center[1]+rad*np.cos(t) 
    return x,y,
# modify to make it how it needs to be
def draw_circles(ax,n,center,radius,w,modifier):
    if n>0:
        modifier = modifier*w #changes the circle 
        
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax, n-1, [modifier, 0], radius*w, w, modifier)

plt.close("all") 
fig, ax = plt.subplots()
"""

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
class Node: 
    def __init__(self, d): 
        self.data = d 
        self.left = None
        self.right = None
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
        
def iterativeFind(T,k):
        while T is not None and T.item != k:
            if T.item < k:
                T = T.right
            if T.item > k:
                T = T.left
        if T == None:
            return -1
        return T.item

def buildSortedbalancedtree(A):
    if len(A) <= 0 :
        return None
    mid = len(A)//2
    root = Node(A[mid])
    root.left = buildSortedbalancedtree(A[:mid])
    root.right = buildSortedbalancedtree(A[mid+1:])
    return root

def BSTtoSortedArray(T,C):
    if T is None:
        return 
    if T is not None:
        BSTtoSortedArray(T.left,C)
        C.append(T.left.item)
        C.append(T.item)
        BSTtoSortedArray(T.right,C)
        C.append(T.right.item)
    return T

def PrintNodesatDepth(T,d):
    if isleaf and d>0:
        return None
    if d == 0:
        print(T.item)
        return
    PrintNodesatDepth(T.left,d-1)
    PrintNodesatDepth(T.right,d-1)
        
# Code to test the functions above
T = None
A = [10, 4, 15, 2, 8, 12, 18, 1, 3, 5, 6, 7]
for a in A:
    T = Insert(T,a)
    
B = [1, 2, 3, 4, 5, 6, 7, 8, 9]
C = []
InOrder(T)
print()
InOrderD(T,'')
print()

print(SmallestL(T).item)
print(Smallest(T).item)

FindAndPrint(T,40)
FindAndPrint(T,110)

n=60
print('Delete',n,'Case 1, deleted node is a leaf')
T = Delete(T,n) #Case 1, deleted node is a leaf
InOrderD(T,'')
print('####################################')

n=90      
print('Delete',n,'Case 2, deleted node has one child')      
T = Delete(T,n) #Case 2, deleted node has one child
InOrderD(T,'')
print('####################################')

n=70      
print('Delete',n,'Case 3, deleted node has two children') 
T = Delete(T,n) #Case 3, deleted node has two children
InOrderD(T,'')

n=40      
print('Delete',n,'Case 3, deleted node has two children') 
T = Delete(T,n) #Case 3, deleted node has two children
InOrderD(T,'')

IF = iterativeFind(T,17)
print(IF)

print(buildSortedbalancedtree(B))
InOrder(T)
print()
InOrderD(T,'')
print()
BSTtoSortedArray(T,C)
print(C)