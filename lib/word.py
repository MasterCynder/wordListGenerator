import sys
import lib
from math import *
from lib import letter as lt
# import letter as lt

class Word:
    def __init__(self, word):
        self.word = word
        
        # optional word
        self.optionalWord = False
        
        i = 0
        self.tabPossibilities = []
        while i < len(word):
            self.tabPossibilities.append([word[i]])
            i = i + 1

    def addLeet(self):
        i = 0
        for eachLetter in self.word:
            self.tabPossibilities[i] = self.tabPossibilities[i] + (lt.Letter(eachLetter).leet())
            i = i + 1

    def addUpperCase(self):
        i = 0
        for eachLetter in self.word:
            self.tabPossibilities[i] = self.tabPossibilities[i] + (lt.Letter(eachLetter).upperCase())
            i = i + 1

    def addLowerCase(self):
        i = 0
        for eachLetter in self.word:
            self.tabPossibilities[i] = self.tabPossibilities[i] + (lt.Letter(eachLetter).lowerCase())
            i = i + 1
    def addCamelCase(self):
        #print (len(self.tabPossibilities))
        if (len(self.tabPossibilities)>0):
            self.tabPossibilities[0] = self.tabPossibilities[0] + (lt.Letter(self.word[0]).upperCase())

    def addOptionalWord(self):
        self.optionalWord = True

    def loadNumbers(self):
    # Load the number of combination for each letter  
        self.tabNumbers = []
        self.combinationNumber = 1
        for tabPossibilitiesLetter in self.tabPossibilities:
            sizeTmp = len(tabPossibilitiesLetter)
            self.tabNumbers.append(sizeTmp)
            self.combinationNumber = self.combinationNumber * sizeTmp
        # optional word
        if self.optionalWord == True:
            self.combinationNumber = self.combinationNumber + 1

    def convertNumberInCombination(self, number):
        result = ''
        i = 0
        # optional word
        if self.optionalWord == True and number == self.returnNbCombination() - 1:    
            return ''
        #all the others combinations
        for letterNumber in self.tabNumbers:
            remainder = number % letterNumber
            number = number // letterNumber
            result = result + self.tabPossibilities[i][remainder]
            i = i + 1
        return result

    def returnNbCombination(self):
        return self.combinationNumber

    def weightPossibilities(self):
        charWeight = 1.25
        return charWeight * self.returnNbCombination() * len(self.word)
