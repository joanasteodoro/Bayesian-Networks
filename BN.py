# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

#import itertools
from itertools import *
import numpy as np

class Node():
    def __init__(self, prob, parents = []):
        self.parents = parents
        self.prob = prob

    #Returns a list [a,b], where a is the probability of a node not happening and b is the probability of a node happening
    def computeProb(self, evid):
        parents_size = len(self.parents)
        parents_evidences = []
        if(parents_size == 0):
            return [1-self.prob, self.prob]
        else:
            for i in range(parents_size):
                parents_evidences.append(evid[self.parents[i]])
            position = tuple(parents_evidences)
            prob = self.prob[position]
            return [1-prob,prob]
        
                
    
class BN():
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob

    def computeJointProb(self, evid):
        prod = 1
        tamanho = len(self.prob)
        for i in range(tamanho):
            if(evid[i] == 0):
                prod = prod * self.prob[i].computeProb(evid)[0]
            else:
                prod = prod * self.prob[i].computeProb(evid)[1]
        return prod

    def computePostProb(self, evid):
        x = []
        nx = []
        result1 = []
        result2 = []
        indexes = []
        combos = []
        index = 0 
        newEvid = list(evid)
        for i in newEvid:
            if i == -1:
                x+=[1]
                nx+=[0]
            elif i == []:
                indexes += [index]
                x+=[[]]
                nx+=[[]]
            else:
                x+=[i]
                nx+=[i]
            index+=1
        combos += combinations_with_replacement([0,1], len(indexes))
        combos += permutations([0, 1], len(indexes))
        combos = list(set(combos))
        for c in range(len(combos)):
            i = 0
            for index in indexes:
                x[index] = combos[c][i]
                nx[index] = combos[c][i]
                i+=1
            result1+=[self.computeJointProb(tuple(x))]
            result2+=[self.computeJointProb(tuple(nx))]
        total = sum(result1 / (sum(result1)+sum(result2)))
        return total