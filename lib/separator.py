import sys
import lib
from lib import permutation as pm
from lib import letter as lt

class Separator:
    def __init__(self, tab):
        self.tabOrigin = tab
        self.isPermuted = False
        self.isCharSeparated = False
        self.isCharStarted = False
        self.isCharEnded = False
        
    def addPermutation(self):
        self.isPermuted = True
        
    def addCharSeparated(self):
        self.isCharSeparated = True
        
    def addCharStarted(self):
        self.isCharStarted = True
        
    def addCharEnded(self):
        self.isCharEnded = True

    def loadNumbers(self):
        self.permutationNumber = 0
        self.myPermutation = pm.Permutation(self.tabOrigin)
        if self.isPermuted == True:
            self.myPermutation.addPermutation()
        self.myPermutation.loadNumbers()
        self.combinationNumber = self.myPermutation.returnNbCombination()
        mySeparator = lt.Letter('')
        self.myTabSeparator = mySeparator.addPunctuation()
        nbChar = len(self.myTabSeparator)
        if self.isCharSeparated == True:
            self.combinationNumber = self.combinationNumber * ( nbChar ** (len(self.tabOrigin) - 1))
        if self.isCharStarted == True:
            self.combinationNumber = self.combinationNumber * nbChar
        if self.isCharEnded == True:
            self.combinationNumber = self.combinationNumber * nbChar

    def convertNumberInCombination(self, number):
        result = ''
        charStart = ''
        charEnd = ''
        charSeparator = []
        nbTmp = self.returnNbCombination()
        permutationNumber = self.myPermutation.returnNbCombination()
        nbTypeCharSeparator = len(self.myTabSeparator)
        if self.isCharStarted == True:
            remainder = number % nbTypeCharSeparator
            number = number // nbTypeCharSeparator
            charStart = self.myTabSeparator[remainder]
        if self.isCharEnded == True:
            remainder = number % nbTypeCharSeparator
            number = number // nbTypeCharSeparator
            charEnd = self.myTabSeparator[remainder]
        if self.isCharSeparated == True:
            for i in range(len(self.tabOrigin) - 1):
                remainder = number % nbTypeCharSeparator
                number = number // nbTypeCharSeparator
                charSeparator.append(self.myTabSeparator[remainder])
        self.myPermutation.convertNumberInCombination(number)
        if self.isCharStarted == True:
            result = result + charStart
        
        i = 0
        for word in self.myPermutation.returnTabCombination():
            result = result + word
            if self.isCharSeparated == True and i < (len(self.tabOrigin) - 1):
                result = result + charSeparator[i]
            i = i + 1
            
        if self.isCharEnded == True:
            result = result + charEnd
        return result

    def returnNbCombination(self):
        return self.combinationNumber