from lib import letter as lt

class Word:
    def __init__(self, word):
        self.word = word
        self.optionalWord = False
        # Each letter is stored as a list of its possible variants
        self.tabPossibilities = [[char] for char in word]

    def _apply_transformation(self, func):
        """Internal helper to apply mappings while avoiding duplicates."""
        for i, char in enumerate(self.word):
            variants = func(lt.Letter(char))
            for v in variants:
                if v not in self.tabPossibilities[i]:
                    self.tabPossibilities[i].append(v)

    def addLeet(self): self._apply_transformation(lambda l: l.leet())
    def addUpperCase(self): self._apply_transformation(lambda l: l.upperCase())
    def addLowerCase(self): self._apply_transformation(lambda l: l.lowerCase())

    def addCamelCase(self):
        """Adds uppercase version for the first letter only."""
        if self.tabPossibilities:
            first_up = lt.Letter(self.word[0]).upperCase()
            for v in first_up:
                if v not in self.tabPossibilities[0]:
                    self.tabPossibilities[0].append(v)

    def addOptionalWord(self):
        self.optionalWord = True

    def loadNumbers(self):
        """Calculates total combinations for this word."""
        self.tabNumbers = [len(p) for p in self.tabPossibilities]
        self.combinationNumber = 1
        for n in self.tabNumbers:
            self.combinationNumber *= n
        # If optional, we add a virtual state (empty string)
        if self.optionalWord:
            self.combinationNumber += 1

    def convertNumberInCombination(self, number):
        """Maps a unique index to a specific word variation."""
        if self.optionalWord and number == self.combinationNumber - 1:
            return ''
            
        result = []
        for i, count in enumerate(self.tabNumbers):
            result.append(self.tabPossibilities[i][number % count])
            number //= count
        return "".join(result)

    def returnNbCombination(self):
        return self.combinationNumber
