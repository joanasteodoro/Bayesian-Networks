'''Joana Teodoro - 86440, Miguel Rocha - 86482,  Group 24'''

'''Artificial Intelligence's project
         - Bayesian Networks -     '''

#evid = evidence: tuplo q contem os estados dos nodes, 1 = true, 0 = false
    
class Node():
    def __init__(self, prob, parents = []):
        self.parents = parents
        self.prob = prob

    def computeProb(self, evid):
        for i in range(len(evid)):
