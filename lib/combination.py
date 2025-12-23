class Combination:
    def __init__(self, tab):
        self.tabOrigin = tab # List of Word objects

    def loadNumbers(self):
        """Calculates the product of all word combinations in this specific order."""
        self.combinationNumber = 1
        for word_list in self.tabOrigin:
            # We assume index 0 as each keyword group is handled as a list
            self.combinationNumber *= word_list[0].returnNbCombination()

    def convertNumberInCombination(self, number):
        """Converts a global index into specific variations for each word."""
        self.tabResult = []
        for word_list in self.tabOrigin:
            word_obj = word_list[0]
            nb = word_obj.returnNbCombination()
            self.tabResult.append(word_obj.convertNumberInCombination(number % nb))
            number //= nb
        return "".join(self.tabResult)

    def returnNbCombination(self):
        return self.combinationNumber

    def returnTabCombination(self):
        return self.tabResult
