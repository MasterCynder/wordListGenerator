import sys
import getopt
import lib
from lib import word as wd
from lib import open_file as of
from lib import write_file as wf
from lib import usage as us
from lib import combination as co

# myWord = Word("Pierre")
# myWord.addLeet()
# myWord.addUpperCase()
# myWord.addLowerCase()
# myWord.loadWordList()
# myWord.printWordList()

def main(argv):

    writeFilePath = ''
    keyWordsFilePath = ''
    leet = False
    lowercase = False
    uppercase = False

    try:                                
        opts, args = getopt.getopt(argv, "w:k:lCc", ["write=", "keywords=", "leet", "uppercase", "lowercase"])
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
            myWord.loadWordList()
            result = myWord.returnWordList()
            wordsTab = wordsTab + result
        globalTab.append(wordsTab)
            
    myCombination = co.Combination(globalTab)
    myCombination.loadCombinationList()
    result = myCombination.returnCombinationList()
   
   
            
    # myWord = wd.Word("Pierre")
    # if (leet == True):
        # myWord.addLeet()
    # if (lowercase == True):
        # myWord.addLowerCase()
    # if (uppercase == True):
        # myWord.addUpperCase()
        
    # myWord.loadWordList()
    # result = myWord.returnWordList()
    
    file = wf.WriteFile(writeFilePath)
    for line in result:
        file.write(line+"\n")
    file.close()


if __name__ == "__main__":
    main(sys.argv[1:])
