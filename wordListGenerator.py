import sys
import getopt
import lib
from lib import word as wd
from lib import open_file as of
from lib import write_file as wf
from lib import usage as us
from lib import combination as co
from lib import progress_bar as pb

def main(argv):

    writeFilePath = ''
    keyWordsFilePath = ''
    leet = False
    lowercase = False
    uppercase = False
    optional = False
    simulation = False

    try:                                
        opts, args = getopt.getopt(argv, "hw:k:lCcos", ["help", "write=", "keywords=", "leet", "uppercase", "lowercase", "optional", "simulation"])
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
        elif opt in ("-o", "--optional"):
            optional = True
        elif opt in ("-s", "--simulation"):
            simulation = True

    if writeFilePath == '' and simulation == False:
        print("Error: -w/--write or -s/--simulation option required")
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
            if (optional == True):
                myWord.addOptionalWord()
            myWord.loadNumbers()
            tmpWeight = tmpWeight + myWord.weightPossibilities()
            wordsTab.append(myWord)
        weight = weight * tmpWeight
        globalTab.append(wordsTab)
    print(globalTab)
    myCombination = co.Combination(globalTab)
    myCombination.loadNumbers()
    nb = myCombination.returnNbCombination()
    if simulation == False:
        ProgressBar = None
        percent = 0
        file = wf.WriteFile(writeFilePath)
        for i in range(nb):
            file.write(myCombination.convertNumberInCombination(i)+"\n")
            label = "Loading " + "(" + str(i) + "/" + str(nb) + ")"
            if ProgressBar == None:
                ProgressBar = pb.ProgressBar(i, nb, label = label, usePercentage = True)
            elif (i / nb * 100) >= (percent + 1) or i == (nb - 1):
                ProgressBar.updateProgress(i, label)
                percent = percent + 1
        print()
        file.close()
    if simulation == True:
        print(str(nb) + " Combinations")
        # print(str(weight / 1024) + " Ko")

if __name__ == "__main__":
    main(sys.argv[1:])

