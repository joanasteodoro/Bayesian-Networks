# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

#import itertools
from itertools import *
class Node():
    def __init__(self, prob, parents = []):
        self.parents = parents
        self.prob = prob

    #Returns a list [a,b], where a is the probability of a node not happening and b is the probability of a node happening
    def computeProb(self, evid):
        parents_size = len(self.parents)
        parents_sublist = []
        result_list = []
        if(parents_size == 0):
            result_list = [1-self.prob, self.prob]
        else:
            for i in range(parents_size):
                if(len(parents_sublist) == 0):
                    result_list = [1, 0]
                if(evid[i] == 0 and i != parents_size - 1):
                    parents_sublist = self.prob[0]         
                if(evid[i] == 0 and i == parents_size - 1 and len(parents_sublist) > 0):
                    result_list.append(1 - parents_sublist[0])
                    result_list.append(parents_sublist[0])
                if(evid[i] == 1 and i != parents_size - 1):
                    parents_sublist = self.prob[1]
                if(evid[i] == 1 and i == parents_size - 1 and len(parents_sublist) >= 2):
                    result_list.append(1 - parents_sublist[1])
                    result_list.append(parents_sublist[1])                   
        return result_list
    
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
        combos = []
        result = 0
        x = ()
        nx = ()
        a = 0
        for i in evid:
            x += (i,)
            nx += (i,)
            if i == -1:
                x += (1,)
                nx += (0,)
            if(i == []):
                x += ([],)
                nx += ([],)
                a += 1
        combos += combinations_with_replacement([0,1], a)
        combos += permutations([0, 1], a)
        combos = list(set(combos))
        a = 0
        newx = ()
        newnx = ()  
        for i in range(len(evid)):
            newx += (x[i],)
            newnx += (nx[i],)
            if evid[i] == []:
                newnx += (combos[a][0], )
                newnx += (combos[a][1], )
                a+=1
                #result += [self.computeJointProb(newx)/(self.computeJointProb(newx)+self.computeJointProb(newnx))]
                print ("newx\n")
                print (newx)
                print ("newnx\n")
                print (newnx)
        return result
        