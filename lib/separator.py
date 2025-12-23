from lib import permutation as pm
from lib import letter as lt

class Separator:
    def __init__(self, tab):
        self.tabOrigin = tab
        self.isPermuted = False
        self.isCharSeparated = False
        self.isCharStarted = False
        self.isCharEnded = False
        self.myTabDates = [] # Suffix dates list
        
    def addPermutation(self): self.isPermuted = True
    def addCharSeparated(self): self.isCharSeparated = True
    def addCharStarted(self): self.isCharStarted = True
    def addCharEnded(self): self.isCharEnded = True
    def addDates(self, dateList): self.myTabDates.extend(dateList)

    def loadNumbers(self):
        """Calculates global combinations including permutations and extras."""
        self.myPermutation = pm.Permutation(self.tabOrigin)
        if self.isPermuted:
            self.myPermutation.addPermutation()
        self.myPermutation.loadNumbers()
        
        self.combinationNumber = self.myPermutation.returnNbCombination()
        
        # Punctuation math
        punct = lt.Letter('').addPunctuation()
        self.myTabSeparator = punct
        nbChar = len(punct)
        
        if self.isCharSeparated:
            self.combinationNumber *= (nbChar ** (len(self.tabOrigin) - 1))
        if self.isCharStarted:
            self.combinationNumber *= nbChar
        if self.isCharEnded:
            self.combinationNumber *= nbChar
        if self.myTabDates:
            self.combinationNumber *= len(self.myTabDates)

    def convertNumberInCombination(self, number):
        """Deconstructs a number into word order, punctuations, and dates."""
        dateStr = ''
        if self.myTabDates:
            dateStr = self.myTabDates[number % len(self.myTabDates)]
            number //= len(self.myTabDates)

        nbP = len(self.myTabSeparator)
        cStart, cEnd = '', ''
        cMid = []

        if self.isCharStarted:
            cStart = self.myTabSeparator[number % nbP]
            number //= nbP
        if self.isCharEnded:
            cEnd = self.myTabSeparator[number % nbP]
            number //= nbP
        if self.isCharSeparated:
            for _ in range(len(self.tabOrigin) - 1):
                cMid.append(self.myTabSeparator[number % nbP])
                number //= nbP

        # Get words from permutation logic
        self.myPermutation.convertNumberInCombination(number)
        words = self.myPermutation.returnTabCombination()
        
        # Assembly
        res = cStart
        for i, w in enumerate(words):
            res += w
            if self.isCharSeparated and i < (len(words) - 1):
                res += cMid[i]
        
        return res + dateStr + cEnd

    def returnNbCombination(self):
        return self.combinationNumber
