# import word

class MyWord:
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
            self.tabPossibilities[i] = self.tabPossibilities[i] + (MyLetter(eachLetter).leet())
            i = i + 1  
        print(self.tabPossibilities)
            
    def addMajuscule(self):
        i = 0
        for eachLetter in self.word:
            self.tabPossibilities[i] = self.tabPossibilities[i] + (MyLetter(eachLetter).majuscule())
            i = i + 1  
        print(self.tabPossibilities)
            
    def addMinuscule(self):
        i = 0
        for eachLetter in self.word:
            self.tabPossibilities[i] = self.tabPossibilities[i] + (MyLetter(eachLetter).minuscule())
            i = i + 1
        print(self.tabPossibilities)
        
            
    def loadWordList(self):
        self.wordList = self.listAllPossibilities('', self.tabPossibilities)
        
    def printWordList(self):
        for tmpWord in self.wordList:
            print(tmpWord)
    
    def listAllPossibilities(self, letter, tab):
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
                tab_tmp = self.listAllPossibilities(tab[0][i], tab2)
                j = 0
                while j < len(tab_tmp):
                    result.append(tab[0][i] + tab_tmp[j])
                    j = j + 1
                i = i + 1
            return result
    
        
class MyLetter:
    def __init__(self, letter):
        self.letter = letter
        
    def leet(self):
        result = []
        if (self.letter == 'a' or self.letter == 'A'):
            result.append('@')
            result.append('4')
        if (self.letter == 'e' or self.letter == 'E'): 
            result.append('3')
        if (self.letter == 'i' or self.letter == 'I'): 
            result.append('!')
        if (self.letter == 'l' or self.letter == 'L'): 
            result.append('1')
        if (self.letter == 'o' or self.letter == 'O'): 
            result.append('0')
        return result
        
        
    def majuscule(self):
        result = []
        if (self.letter == 'a'): 
            result.append('A')
        if (self.letter == 'b'): 
            result.append('B')
        if (self.letter == 'c'): 
            result.append('C')
        if (self.letter == 'd'): 
            result.append('D')
        if (self.letter == 'e'): 
            result.append('E')
        if (self.letter == 'f'): 
            result.append('F')
        if (self.letter == 'g'): 
            result.append('G')
        if (self.letter == 'h'): 
            result.append('H')
        if (self.letter == 'i'): 
            result.append('I')
        if (self.letter == 'j'): 
            result.append('J')
        if (self.letter == 'k'): 
            result.append('K')
        if (self.letter == 'l'): 
            result.append('L')
        if (self.letter == 'm'): 
            result.append('M')
        if (self.letter == 'n'): 
            result.append('N')
        if (self.letter == 'o'): 
            result.append('O')
        if (self.letter == 'p'): 
            result.append('P')
        if (self.letter == 'q'): 
            result.append('Q')
        if (self.letter == 'r'): 
            result.append('R')
        if (self.letter == 's'): 
            result.append('S')
        if (self.letter == 't'): 
            result.append('T')
        if (self.letter == 'u'): 
            result.append('U')
        if (self.letter == 'v'): 
            result.append('V')
        if (self.letter == 'w'): 
            result.append('W')
        if (self.letter == 'x'): 
            result.append('X')
        if (self.letter == 'y'): 
            result.append('Y')
        if (self.letter == 'z'): 
            result.append('Z')
            
        return result
           
    def minuscule(self):
        result = []
        if (self.letter == 'A'): 
            result.append('a')
        if (self.letter == 'B'): 
            result.append('b')
        if (self.letter == 'C'): 
            result.append('c')
        if (self.letter == 'D'): 
            result.append('d')
        if (self.letter == 'E'): 
            result.append('e')
        if (self.letter == 'F'): 
            result.append('f')
        if (self.letter == 'G'): 
            result.append('g')
        if (self.letter == 'H'): 
            result.append('h')
        if (self.letter == 'I'): 
            result.append('i')
        if (self.letter == 'J'): 
            result.append('j')
        if (self.letter == 'K'): 
            result.append('k')
        if (self.letter == 'L'): 
            result.append('l')
        if (self.letter == 'M'): 
            result.append('m')
        if (self.letter == 'N'): 
            result.append('n')
        if (self.letter == 'O'): 
            result.append('o')
        if (self.letter == 'P'): 
            result.append('p')
        if (self.letter == 'Q'): 
            result.append('q')
        if (self.letter == 'R'): 
            result.append('r')
        if (self.letter == 'S'): 
            result.append('s')
        if (self.letter == 'T'): 
            result.append('t')
        if (self.letter == 'U'): 
            result.append('u')
        if (self.letter == 'V'): 
            result.append('v')
        if (self.letter == 'W'): 
            result.append('w')
        if (self.letter == 'X'): 
            result.append('x')
        if (self.letter == 'Y'): 
            result.append('y')
        if (self.letter == 'Z'): 
            result.append('z')
            
        return result
           
                   

myWord = MyWord("Pierre")
myWord.addLeet()
myWord.addMajuscule()
myWord.addMinuscule()
myWord.loadWordList()
myWord.printWordList()

