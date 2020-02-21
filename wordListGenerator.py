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
    print(keyWordList)
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
            myWord.loadNumbers()
            wordsTab.append(myWord)
        globalTab.append(wordsTab)
            
    myCombination = co.Combination(globalTab)
    myCombination.loadNumbers()
    nb = myCombination.returnNbCombination()
    
    file = wf.WriteFile(writeFilePath)
    for i in range(nb):
        file.write(myCombination.convertNumberInCombination(i)+"\n")
    file.close()
   
   
    # 
    # for line in result:
        # file.write(line+"\n")
    # file.close()
    
def test():
    myWord = wd.Word("1111")
    myWord.addLeet()
    myWord.loadNumbers()
    nb = myWord.returnNbCombination()
    myWord2 = wd.Word("2222")
    myWord2.addLeet()
    myWord2.loadNumbers()
    nb2 = myWord2.returnNbCombination()
    myWord3 = wd.Word("1111")
    myWord3.addLeet()
    myWord3.loadNumbers()
    nb3 = myWord3.returnNbCombination()
    myWord4 = wd.Word("2222")
    myWord4.addLeet()
    myWord4.loadNumbers()
    nb4 = myWord4.returnNbCombination()
    myCombination = co.Combination([[myWord, myWord2],[myWord3, myWord4]])
    myCombination.loadNumbers()
    nb5 = myCombination.returnNbCombination()
    
    print(nb)
    print(nb2)
    print(nb3)
    print(nb4)
    print(nb5)
    
    
    print(myCombination.convertNumberInCombination(1562499))
    # myWord.addUpperCase()
    # myWord.addLowerCase()
    # myWord.loadWordList()
    # myWord.printWordList()

if __name__ == "__main__":
    # test()
    main(sys.argv[1:])
