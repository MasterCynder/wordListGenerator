import sys
import itertools
import math
from lib import combination as co

class Permutation:
    def __init__(self, tab):
        self.tabOrigin = tab
        self.isPermuted = False
        self.tabCombinations = []
        self.totalNbPermutations = 1
        
    def addPermutation(self):
        self.isPermuted = True
        # Calcul du nombre de permutations possibles (n!)
        self.totalNbPermutations = math.factorial(len(self.tabOrigin))

    def loadNumbers(self):
        # On calcule les combinaisons sur l'ordre original pour obtenir le poids d'une permutation
        sample_combination = co.Combination(self.tabOrigin)
        sample_combination.loadNumbers()
        self.nbCombPerPermutation = sample_combination.returnNbCombination()
        
        # Nombre total = (nombre de permutations) * (combinaisons par permutation)
        self.combinationNumber = self.totalNbPermutations * self.nbCombPerPermutation

    def convertNumberInCombination(self, number):
        # 1. Trouver quel index de permutation utiliser
        perm_index = number // self.nbCombPerPermutation
        # 2. Trouver l'index de la combinaison au sein de cette permutation
        comb_index = number % self.nbCombPerPermutation
        
        # Générer dynamiquement la n-ième permutation (très efficace en mémoire)
        # On utilise itertools.islice pour ne pas charger toute la liste
        current_perm = next(itertools.islice(itertools.permutations(self.tabOrigin), perm_index, None))
        
        # Appliquer la combinaison sur cet ordre précis
        temp_combination = co.Combination(current_perm)
        temp_combination.loadNumbers()
        
        result = temp_combination.convertNumberInCombination(comb_index)
        self.tabResult = temp_combination.returnTabCombination()
        return result

    def returnNbCombination(self):
        return self.combinationNumber
        
    def returnTabCombination(self):
        return self.tabResult
