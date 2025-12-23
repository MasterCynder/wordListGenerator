class Letter:
    def __init__(self, letter):
        self.letter = letter

    def leet(self):
        """Common leet speak mapping."""
        mapping = {
            'a': ['@', '4'], 'A': ['@', '4'],
            'b': ['8'], 'B': ['8'],
            'c': ['('], 'C': ['('],
            'e': ['3', '€'], 'E': ['3', '€'],
            'h': ['#'], 'H': ['#'],
            'i': ['1', '!'], 'I': ['1', '!'],
            'l': ['1'], 'L': ['1'],
            'o': ['0'], 'O': ['0'],
            's': ['5', '$'], 'S': ['5', '$'],
            't': ['7', '+'], 'T': ['7', '+']
        }
        return mapping.get(self.letter, [])

    def upperCase(self):
        return [self.letter.upper()] if self.letter.upper() != self.letter else []

    def lowerCase(self):
        return [self.letter.lower()] if self.letter.lower() != self.letter else []
            
    def addPunctuation(self):
        """Standard set of punctuation for wordlist generation."""
        return ['', '&', '~', '"', '#', "'", '{', '(', '[', '-', '|', '`', '_', '^', '@', ')', ']', '+', '=', '}', '$', '%', '*', '>', '<', '?', ',', '.', ';', '/', ':', '!']
