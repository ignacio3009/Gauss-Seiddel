# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:40:46 2019

@author: ignac
"""
from createYbus import*
from readData import*
import numpy as np


Nodes, Generators, Lines= importData()
N = len(Nodes)
#Start variable
epsilon=0.01
Y = createY()
global Dm, Dn, Vm,Vn, Pm, Pn, Qm, Qn, Im, In
Dm = np.zeros((N),dtype=complex)
Vm = np.ones((N),dtype=complex)
Pm = np.zeros((N),dtype=complex)
Qm = np.zeros((N),dtype=complex)
Im = np.zeros((N),dtype=complex)


Dn = np.zeros((N),dtype=complex)
Vn = np.ones((N),dtype=complex)
Pn = np.zeros((N),dtype=complex)
Qn = np.zeros((N),dtype=complex)
In= np.zeros((N),dtype=complex)

#Pinj = Pgen - Pcons
def startVariables():
    global Pn, Qn, Pm, Qm, Vn, Vm
    for i in range(N):
        Pgen=Nodes[i,1]
        Pcons=Nodes[i,3]
        Qgen = Nodes[i,2]
        Qcons = Nodes[i,4]
        
        Pn[i] = Pgen-Pcons
        Qn[i] = Qgen-Qcons
        
        Pm[i] = Pgen-Pcons
        Qm[i] = Qgen-Qcons
        
    for i in range(N):
        typ = Nodes[i,5]
        if typ==0:
            Vm[i]=1.05
            Vn[i]=1.05
        elif typ==1:
           Vm[i]=1.02
           Vn[i]=1.02

    
#0 slack
#1 PV
# PQ


def toPolar(z):
    zmod =abs(z)
    angle = np.angle(z)
    print(str(zmod)+'<'+str(angle))
    

def calculateV(i):
    vbus = 1/Y[i,i]*((Pn[i] - 1j*Qn[i])/np.conj(Vn[i])- sum(Y[i,x]*Vn[x] for x in range(i+1,N)) - sum(Y[i,x]*Vn[x] for x in range(0,i)))
    return vbus

def calculateQ(i):
    qbus = -1*np.imag(np.conj(Vn[i])*sum(Y[i,k]*Vm[i,k] for k in range(0,N)))
    return qbus

def calculatePQ(i):
    global Vm
    Vm[i] = calculateV(i)

def calculatePV(i):
    global Qn, Vm
    Qn[i] = calculateQ(i)
    Vbus = calculateV(i)
    Vm[i] = abs(Vn[i])*Vbus/abs(Vbus)
    
    
def verifyError(epsilon):
    global Vm, Vn
    e = Vm - Vn
    print('Vn')
    print(Vn)
    print('Vm')
    print(Vm)
    emax = max(abs(e))
    print('emax = ',emax)
    if emax<epsilon:
        return False
    Vn = Vm
    return True



def main():
    cnt=0
    startVariables()
    for i in range(N):
        typ = getType(Nodes[i,0])
        if typ==1:
            calculatePV(i)
        elif typ==2:
            calculatePQ(i)
    cnt = cnt+1
    print('Iteracion '+str(cnt))
    while(verifyError(epsilon)):
        for i in range(N):
            typ = getType(Nodes[i,0])
            if typ==1:
                calculatePV(i)
            elif typ==2:
                calculatePQ(i)
        cnt+=1
        print('Iteracion '+str(cnt))
       
        
    
if __name__ == '__main__':
    main()
    
            