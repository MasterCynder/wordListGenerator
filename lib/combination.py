import sys

class Combination:
    def __init__(self, tab):
        self.tabPossibilities = tab
        
    def loadCombinationList(self):
        self.combinationList = self.genOrdererCombination(self.tabPossibilities)
        
    def returnCombinationList(self):
        return self.combinationList
        
    def genOrdererCombination(self, tab):
        if (len(tab) == 1):
            return tab[0]
        else:
            result = []
            i = 1
            tab2  = []
            while i < len(tab):
                tab2.append(tab[i])
                i = i + 1
            i = 0
            while i < len(tab[0]):
                tab_tmp = self.genOrdererCombination(tab2)
                j = 0
                while j < len(tab_tmp):
                    result.append(tab[0][i] + tab_tmp[j])
                    j = j + 1
                i = i + 1
            return result
            
    def loadNumbers(self):
    # Load the number of combination for each word
        self.tabNumbers = []
        self.combinationNumber = 1
        for line in self.tabPossibilities:
            sizeTmp = 0
            for possibilitiesWord in line:
                sizeTmp = sizeTmp + possibilitiesWord.returnNbCombination()
            self.combinationNumber = self.combinationNumber * sizeTmp
            self.tabNumbers.append(sizeTmp)
            
    def convertNumberInCombination(self, number):
        result = ''
        i = 0
        for wordNumber in self.tabNumbers:
            remainder = number % wordNumber
            number = number // wordNumber
            numberTmp = number
            j = 0
            indice = 0
            for word in self.tabPossibilities[i]:
                if number < word.returnNbCombination():
                    indice = j
                    break
                number = number - word.returnNbCombination()
                j = j + 1
            result = result + self.tabPossibilities[i][indice].convertNumberInCombination(remainder)
            i = i + 1
        return result
        
    def returnNbCombination(self):
        return self.combinationNumber