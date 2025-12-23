import sys
import argparse
from lib import word as wd
from lib import open_file as of
from lib import write_file as wf
from lib import separator as sp
from lib import progress_bar as pb

def main():
    parser = argparse.ArgumentParser(description="Word list generator v0.2")
    parser.add_argument("-w", "--write", help="Path for writing the word list")
    parser.add_argument("-k", "--keywords", required=True, help="Path for reading keywords")
    parser.add_argument("-l", "--leet", action="store_true", help="Using leet conversion")
    parser.add_argument("-C", "--uppercase", action="store_true", help="Using uppercase")
    parser.add_argument("-c", "--lowercase", action="store_true", help="Using lowercase")
    parser.add_argument("-e", "--camel", action="store_true", help="Using camelcase")
    parser.add_argument("-o", "--optional", action="store_true", help="Make each word optional")
    parser.add_argument("-d", "--disorder", action="store_true", help="All possible word orders")
    parser.add_argument("-a", "--startpunctuation", action="store_true", help="Add a punctuation mark at the beginning")
    parser.add_argument("-z", "--endpunctuation", action="store_true", help="Add a punctuation mark at the end")
    parser.add_argument("-m", "--middlepunctuation", action="store_true", help="Add a punctuation mark between the words")
    parser.add_argument("-s", "--simulation", action="store_true", help="Simulation only")

    args = parser.parse_args()

    if not args.write and not args.simulation:
        print("Error: -w/--write or -s/--simulation option required")
        sys.exit(2)

    # Chargement des mots
    keyWordFile = of.OpenFile(args.keywords)
    keyWordFile.read()
    keyWordFile.loadKeyWord()
    keyWordList = keyWordFile.returnKeyWord()
    
    globalTab = []
    for possibilities in keyWordList:
        wordsTab = []
        for string in possibilities:
            if not string.strip(): continue # Skip empty lines
            myWord = wd.Word(string.strip())
            if args.leet: myWord.addLeet()
            if args.lowercase: myWord.addLowerCase()
            if args.uppercase: myWord.addUpperCase()
            if args.camel: myWord.addCamelCase()
            if args.optional: myWord.addOptionalWord()
            myWord.loadNumbers()
            wordsTab.append(myWord)
        if wordsTab: globalTab.append(wordsTab)
    
    mySeparator = sp.Separator(globalTab)
    if args.disorder: mySeparator.addPermutation()
    if args.startpunctuation: mySeparator.addCharStarted()
    if args.endpunctuation: mySeparator.addCharEnded()
    if args.middlepunctuation: mySeparator.addCharSeparated()
    
    mySeparator.loadNumbers()
    nb = mySeparator.returnNbCombination()

    if args.simulation:
        print(f"{nb} Combinations possibles.")
        return

    # Ecriture avec barre de progression optimisée
    file = wf.WriteFile(args.write)
    pbar = None
    
    # On n'update la barre que tous les 1% pour gagner en performance
    step = max(1, nb // 100)
    
    for i in range(nb):
        file.write(mySeparator.convertNumberInCombination(i) + "\n")
        if i % step == 0 or i == nb - 1:
            label = f"Generating ({i}/{nb})"
            if pbar is None:
                pbar = pb.ProgressBar(i, nb, label=label)
            else:
                pbar.updateProgress(i + 1, label)
    
    file.close()
    print("\nTerminé !")

if __name__ == "__main__":
    main()
