import sys
import getopt
import lib
from lib import word as wd
from lib import open_file as of
from lib import write_file as wf
from lib import usage as us
from lib import combination as co

def main(argv):

    writeFilePath = ''
    keyWordsFilePath = ''
    leet = False
    lowercase = False
    uppercase = False
    simulation = False

    try:                                
        opts, args = getopt.getopt(argv, "w:k:lCcs", ["write=", "keywords=", "leet", "uppercase", "lowercase", "simulation"])
    except getopt.GetoptError:          
        us.usage()                         
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            us.usage()
            sys.exit()
        elif opt in ("-w", "--write"):
            writeFilePath = arg
        elif opt in ("-k", "--keywords"):
            keyWordsFilePath = arg
        elif opt in ("-l", "--leet"):
            leet = True
        elif opt in ("-c", "--lowercase"):
            lowercase = True
        elif opt in ("-C", "--uppercase"):
            uppercase = True
        elif opt in ("-s", "--simulation"):
            simulation = True
            
    if writeFilePath == '':
        print("Error: -w/--write option required")
        us.usage()
        sys.exit(2)        
    if keyWordsFilePath == '':
        print("Error: -k/--keywords option required")
        us.usage()
        sys.exit(2)
        
    keyWordFile = of.OpenFile(keyWordsFilePath)
    keyWordFile.read()
    keyWordFile.loadKeyWord()
    keyWordList = keyWordFile.returnKeyWord()
    globalTab = []
    
    weight = 1
    tmpWeight = 0
    for possibilities in keyWordList:
        wordsTab = []
        for string in possibilities:
            myWord = wd.Word(string)
            if (leet == True):
                myWord.addLeet()
            if (lowercase == True):
                myWord.addLowerCase()
            if (uppercase == True):
                myWord.addUpperCase()
            myWord.loadNumbers()
            tmpWeight = tmpWeight + myWord.weightPossibilities()
            wordsTab.append(myWord)
        weight = weight * tmpWeight
        globalTab.append(wordsTab)
            
    myCombination = co.Combination(globalTab)
    myCombination.loadNumbers()
    nb = myCombination.returnNbCombination()
    
    if simulation == False:
        file = wf.WriteFile(writeFilePath)
        for i in range(nb):
            file.write(myCombination.convertNumberInCombination(i)+"\n")
        file.close()
    if simulation == True:
        print(str(nb) + " Combinations")
        # print(str(weight / 1024) + " Ko")

if __name__ == "__main__":
    main(sys.argv[1:])
