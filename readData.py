# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 19:19:21 2019

@author: ignac
"""

import pandas as pd
def importData():
    #Nodos
    df=pd.read_excel(r'data.xlsx', sheet_name='Nodes',usecols='A:F',skiprows=0)
    Nodes=df.values
    
    #Generators
    df=pd.read_excel(r'data.xlsx', sheet_name='Generators',usecols='A:E',skiprows=0)
    Generators=df.values
    
    #Loads
    #df=pd.read_excel(r'data.xlsx', sheet_name='Loads',usecols='A:C',skiprows=0)
    #Loads=df.values
    
    #Lines
    df=pd.read_excel(r'data.xlsx', sheet_name='Lines',usecols='A:H',skiprows=0)
    Lines=df.values
    return Nodes,Generators,Lines


