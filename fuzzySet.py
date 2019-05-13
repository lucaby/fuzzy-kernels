#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:47:44 2019

@author: jorgeluisguevaradiaz
"""
import skfuzzy 
import numpy as np
from kernelsOnFuzzySets import crossProductLinear


class FuzzySet:
    _elements = None             # use x or e as variable name?
    _elementType = None        # {real, array, matrix, string, graph, logicalPredicate, probabilityDistribution, etc}
    _membershipFunction  = None  # use the same name as given in scikit fuzzy  gaussmf, for example
    _functionParams=None         # use params as variable name?
    _membershipDegrees = None    # use md as variable name?
    
    # Constructor
    #*args is the parameter list
    def __init__(self, elements, membershipFunction, *args):
        """
        initializes a fuzzy set
    
        Args:
            elements: (Type: Set) elements of the set
            membershipFunction: (Type: String) scikit fuzzy name of the membership function gaussmf, for example
            *args: (list of real values) function's parameters
        """
        self._elements=elements
        self._functionParams = flatten(args)
        self._membershipFunction=membershipFunction
        self._membershipDegrees = self._membershipFunction(elements,*self._functionParams)
 
#CLASS FUZZY SET       
#TODO  (1)      
    elements={a1,a2,a3}
    #examplo
    - {2,3,4} # we are here
    #criar conjuntos fuzzy com este tipo de elements e funcao de pertinencia gaussiano
    - {[2, 3.5], [3,5], [4.5, 3.7]}
        params= mean=[d1,d2] sigma=matriz de 2x2
    - {[2,3.5, 4], [3,5,2, 6], [4.5,3.7,8, 8]}
        params= mean=[d1,d2,d3] sigma=matriz de 3x3
    # fazer o check to do type dos elements (assert)    
    #futuro    
    - { [], [], [].. }
    - {(V1,A1), (V2,A2),..}
    membershipFunction=gaussMF
    parametrosDaFuncao=[mean, std]
    membershipDegrees={0.4, 0.3, 0.2}

#TODO  (2)
    - criar plots (metodo dentro da classFuzzy)    
    - elements=   {2,3,4} , x-axis= elements y=axis = membership degrees
     - elements= {[2, 3.5], [3,5], [4.5, 3.7]} 
             ou contourn plot (x1, x2) a cor depende do membership degrees
             ou plot 3D plot (x1=x, x2=y) eixo z depende do membership degrees
     - {[2,3.5, 4], [3,5,2, 6], [4.5,3.7,8, 8]}
            plot 3D, (x,y,z) a cor depende do membership degrees
            
#TODO jupyter notebook com os plots           
     #objetivo
     # explorar a criacao de conjuntos fuzzy, plots
     # explorar as similarity measures via kernels
     #pensar num exemplo
                   
        
def main(): 
    elements = np.random.uniform(0, 100, 3)
    membershipFunction=skfuzzy.gaussmf
    params=[np.mean(elements),np.std(elements)]
    X=FuzzySet(elements, membershipFunction,params)
    print(X._elements)
    print(X._membershipFunction)
    print(X._functionParams)
    print(X._membershipDegrees)
    # linear cross product kernel on fuzzy sets
    X=FuzzySet(elements, membershipFunction,params)
    Y=FuzzySet(elements, membershipFunction,params)
    crossProductLinear(X,Y)
     
     
         
         
         

         
        
     
     
     
     
     
