import itertools
import math
from lib import combination as co

class Permutation:
    def __init__(self, tab):
        self.tabOrigin = tab
        self.isPermuted = False
        self.totalNbPermutations = 1
        
    def addPermutation(self):
        """Enables full shuffling of word order."""
        self.isPermuted = True
        # Calculate n! (factorial) for permutations
        self.totalNbPermutations = math.factorial(len(self.tabOrigin))

    def loadNumbers(self):
        """Calculates total combinations based on word variations and order."""
        sample_combination = co.Combination(self.tabOrigin)
        sample_combination.loadNumbers()
        self.nbCombPerPermutation = sample_combination.returnNbCombination()
        self.combinationNumber = self.totalNbPermutations * self.nbCombPerPermutation

    def convertNumberInCombination(self, number):
        """Calculates the specific order for a given index without storing all of them."""
        perm_index = number // self.nbCombPerPermutation
        comb_index = number % self.nbCombPerPermutation
        
        # Get the n-th permutation dynamically
        current_perm = next(itertools.islice(itertools.permutations(self.tabOrigin), perm_index, None))
        
        temp_combination = co.Combination(current_perm)
        temp_combination.loadNumbers()
        
        result = temp_combination.convertNumberInCombination(comb_index)
        self.tabResult = temp_combination.returnTabCombination()
        return result

    def returnNbCombination(self):
        return self.combinationNumber
        
    def returnTabCombination(self):
        return self.tabResult
