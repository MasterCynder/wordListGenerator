import sys
from lib import letter as lt

class Word:
    def __init__(self, word):
        self.word = word
        self.optionalWord = False
        self.tabPossibilities = [[char] for char in word] # Version condensée de ta boucle while

    def _apply_transformation(self, func):
        for i in range(len(self.word)):
            # Récupérer les variantes pour la lettre à la position i
            variants = func(lt.Letter(self.word[i]))
            for v in variants:
                # On ajoute UNIQUEMENT si la variante n'existe pas déjà à cette position
                if v not in self.tabPossibilities[i]:
                    self.tabPossibilities[i].append(v)

    def addLeet(self):
        self._apply_transformation(lambda l: l.leet())

    def addUpperCase(self):
        self._apply_transformation(lambda l: l.upperCase())

    def addLowerCase(self):
        self._apply_transformation(lambda l: l.lowerCase())

    def addCamelCase(self):
        if len(self.tabPossibilities) > 0:
            # On transforme uniquement la première lettre
            upper_first = lt.Letter(self.word[0]).upperCase()
            for t in upper_first:
                if t not in self.tabPossibilities[0]:
                    self.tabPossibilities[0].append(t)

    def addOptionalWord(self):
        self.optionalWord = True

    def loadNumbers(self):
        self.tabNumbers = []
        self.combinationNumber = 1
        for tabPossibilitiesLetter in self.tabPossibilities:
            sizeTmp = len(tabPossibilitiesLetter)
            self.tabNumbers.append(sizeTmp)
            self.combinationNumber *= sizeTmp
        
        if self.optionalWord:
            self.combinationNumber += 1

    def convertNumberInCombination(self, number):
        if self.optionalWord and number == self.combinationNumber - 1:    
            return ''
            
        result = []
        for i, letterNumber in enumerate(self.tabNumbers):
            remainder = number % letterNumber
            number //= letterNumber
            result.append(self.tabPossibilities[i][remainder])
        
        return "".join(result) # Plus rapide que l'addition de chaînes

    def returnNbCombination(self):
        return self.combinationNumber

    def weightPossibilities(self):
        # Estimation du poids en octets (approximatif)
        charWeight = 1.25
        return charWeight * self.combinationNumber * len(self.word)
