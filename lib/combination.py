class Combination:
    def __init__(self, tab):
        self.tabOrigin = tab # Matrix of Word objects

    def loadNumbers(self):
        """Calculates total combinations by multiplying the number of 
        variations available for each position."""
        self.combinationNumber = 1
        for word_variant_list in self.tabOrigin:
            # Total variations for this position = Sum of combinations of all words on this line
            line_total = sum(w.returnNbCombination() for w in word_variant_list)
            self.combinationNumber *= line_total

    def convertNumberInCombination(self, number):
        """Finds which word from the line to use and which variation."""
        self.tabResult = []
        for word_variant_list in self.tabOrigin:
            # 1. Calculate total possibilities for this line
            line_total = sum(w.returnNbCombination() for w in word_variant_list)
            current_line_index = number % line_total
            number //= line_total
            
            # 2. Find which specific word object corresponds to the index
            running_sum = 0
            selected_word = word_variant_list[0]
            for word_obj in word_variant_list:
                if current_line_index < (running_sum + word_obj.returnNbCombination()):
                    selected_word = word_obj
                    # Adjust index to be relative to this specific word
                    relative_index = current_line_index - running_sum
                    self.tabResult.append(selected_word.convertNumberInCombination(relative_index))
                    break
                running_sum += word_obj.returnNbCombination()
                
        return "".join(self.tabResult)

    def returnNbCombination(self):
        """Returns the total number of combinations calculated in loadNumbers."""
        return self.combinationNumber

    def returnTabCombination(self):
        """Returns the list of generated words for the current index."""
        return self.tabResult
