import sys

class Combination:
    def __init__(self, tab):
        self.tabPossibilities = tab

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
            remainderTmp = remainder
            number = number // wordNumber
            j = 0
            indice = 0
            for word in self.tabPossibilities[i]:
                if remainderTmp < word.returnNbCombination():
                    indice = j
                    break
                remainderTmp = remainderTmp - word.returnNbCombination()
                j = j + 1
            result = result + self.tabPossibilities[i][indice].convertNumberInCombination(remainder)
            i = i + 1
        return result

    def returnNbCombination(self):
        return self.combinationNumber
