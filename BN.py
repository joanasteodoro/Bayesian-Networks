# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""



class Node():
    def __init__(self, prob, parents = []):
        self.parents = parents
        self.prob = prob
    
    def computeProb(self, evid):
        parents_size = len(self.parents)
        print("tamanho: " + str(parents_size))
        parents_sublist = []
        result_list = []
        if(parents_size == 0):
            result_list.append(1 - self.prob)
            result_list.append(self.prob)
        else:
            for i in range(parents_size):
                print("Sou o i : " + str(i))
                if(evid[i] == 0 and i != parents_size - 1):
                    parents_sublist = self.prob[0]
                if(evid[i] == 0 and i == parents_size - 1):
                    result_list.append(1 - parents_sublist[0])
                    result_list.append(parents_sublist[0])
                if(evid[i] == 1 and i != parents_size - 1):
                    print("oi")
                    parents_sublist = self.prob[1]
                    print(parents_sublist)
                if(evid[i] == 1 and i == parents_size - 1):
                    result_list.append(1 - parents_sublist[1])
                    result_list.append(parents_sublist[1])                   
        return result_list
    
class BN():
    def __init__(self, gra, prob):
        pass

    def computePostProb(self, evid):
        pass
               
        return 0
        
        
    def computeJointProb(self, evid):
        pass
        
        return 0