import sys
import lib
from lib import letter as lt
# import letter as lt

class Word:
    def __init__(self, word):
        self.word = word
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
        
            
    def loadWordList(self):
        self.wordList = self.listAllPossibilities(self.tabPossibilities)
        
    def returnWordList(self):
        return self.wordList
        
    def printWordList(self):
        for tmpWord in self.wordList:
            print(tmpWord)
    
    def listAllPossibilities(self, tab):
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
                tab_tmp = self.listAllPossibilities(tab2)
                j = 0
                while j < len(tab_tmp):
                    result.append(tab[0][i] + tab_tmp[j])
                    j = j + 1
                i = i + 1
            return result