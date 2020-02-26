import sys

class Letter:
    def __init__(self, letter):
        self.letter = letter

    def leet(self):
        # Convert the letter in simply leet (the most common) and return 
        result = []
        if (self.letter == 'a' or self.letter == 'A'):
            result.append('@')
            result.append('4')
        elif (self.letter == 'b' or self.letter == 'B'):
            result.append('8')
        elif (self.letter == 'c' or self.letter == 'C'):
            result.append('(')
        elif (self.letter == 'e' or self.letter == 'E'): 
            result.append('3')
            result.append('€')
        elif (self.letter == 'h' or self.letter == 'H'): 
            result.append('#')
        elif (self.letter == 'i' or self.letter == 'I'): 
            result.append('1')
            result.append('!')
        elif (self.letter == 'l' or self.letter == 'L'): 
            result.append('1')
        elif (self.letter == 'o' or self.letter == 'O'): 
            result.append('0')
        elif (self.letter == 's' or self.letter == 'S'): 
            result.append('5')
            result.append('$')
        elif (self.letter == 't' or self.letter == 'T'): 
            result.append('7')
            result.append('+')
        return result


    def upperCase(self):
        if self.letter.upper() == self.letter:
            return []
        else:
            return [self.letter.upper()]

    def lowerCase(self):
        if self.letter.lower() == self.letter:
            return []
        else:
            return [self.letter.lower()]
