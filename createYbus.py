# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:22:34 2019

@author: ignac
"""

from readData import*
import numpy as np

def createY():
    Nodes, Generators, Lines= importData()
    N=len(Nodes)
    R = np.zeros((N,N))
    X = np.zeros((N,N))
    G = np.zeros((N,N))
    B = np.zeros((N,N))
    Zbase = 0
    
    for k in range(len(Lines)):
        node_i = int(Lines[k,0])
        node_j = int(Lines[k,1])
        Sbase = Lines[k,6]
        Vbase = Lines[k,7]
        large = Lines[k,4]

        Zbase = Vbase**2/Sbase
        r = Lines[k,2]*large/Sbase
        x = Lines[k,3]*large/Sbase
 
        R[node_i,node_j] = r
        R[node_j,node_i] = r
        X[node_i,node_j] = x
        X[node_j,node_i] = x
    
    for i in range(N):
        for j in range(i+1,N):
            r=R[i,j]
            x=X[i,j]
            den = (r**2 + x**2)        
            g = r/den
            b = -1*x/den
            G[i,j] = g
            B[i,j] = b
            G[j,i] = g
            B[j,i] = b
#        yij = g+1j*b
#        Y[i,j] = -1*yij
#        Y[j,i] = -1*yij
    G=-G
    B=-B
    
    for i in range(N):
        G[i,i] = -1*sum(G[:,i])
        B[i,i] = -1*sum(B[:,i])
    
    return G+1j*B


    

#def neighbours(Lines,Nodes):
#    N=len(Nodes)
#    A = [[]for x in range(N)]
#    for k in range(len(Lines)):
#         node_i = int(Lines[k,0])
#         node_j = int(Lines[k,1])
#         A[node_i].insert(0,node_j)
#         A[node_j].insert(0,node_i)
#    return A
#
#A = neighbours(Lines,Nodes)
#
#for i in range(N):
#    gii=0
#    bii=0
#    gii += G[i,x] for x in A[i]
#    bii += B[i,x] for x in A[i]
    
        


    
    