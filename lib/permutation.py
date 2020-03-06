import sys
import itertools
import lib
from lib import combination as co

class Permutation:
    def __init__(self, tab):
        self.tabOrigin = tab
        self.isPermuted = False
        self.tabPermuted = [tab]
        
    def addPermutation(self):
        self.tabPermuted = []
        self.isPermuted = True
        for c in itertools.combinations(self.tabOrigin, len(self.tabOrigin)):
            for p in itertools.permutations(c): 
                self.tabPermuted.append(p)

    def loadNumbers(self):
        self.combinationNumber = 0
        self.tabCombinations = []
        for permuted in self.tabPermuted:
            myCombination = co.Combination(permuted)
            myCombination.loadNumbers()
            self.combinationNumber = self.combinationNumber + myCombination.returnNbCombination()
            self.tabCombinations.append(myCombination)

    def convertNumberInCombination(self, number):
        combination = self.tabCombinations[number//(self.combinationNumber // len(self.tabCombinations))]
        number = number % (self.combinationNumber // len(self.tabCombinations))
        result = combination.convertNumberInCombination(number)
        self.tabResult = combination.returnTabCombination()
        return result

    def returnNbCombination(self):
        return self.combinationNumber
        
    def returnTabCombination(self):
        return self.tabResult