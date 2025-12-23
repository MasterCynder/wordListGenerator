import sys
import argparse
from lib import word as wd
from lib import open_file as of
from lib import write_file as wf
from lib import usage as us
from lib import separator as sp
from lib import progress_bar as pb
from lib import date_gen as dg

def main():
    # Setup Argument Parser for modern CLI management
    parser = argparse.ArgumentParser(description="Word list generator v0.1")
    
    # Files options
    parser.add_argument("-w", "--write", help="Output path for the wordlist")
    parser.add_argument("-k", "--keywords", required=True, help="Input path for keywords file")
    
    # Transformation options
    parser.add_argument("-l", "--leet", action="store_true", help="Apply leet conversion")
    parser.add_argument("-C", "--uppercase", action="store_true", help="Apply uppercase conversion")
    parser.add_argument("-c", "--lowercase", action="store_true", help="Apply lowercase conversion")
    parser.add_argument("-e", "--camel", action="store_true", help="Apply camelcase conversion")
    parser.add_argument("-o", "--optional", action="store_true", help="Make each word optional")
    parser.add_argument("-d", "--disorder", action="store_true", help="Generate all possible word orders")
    
    # Punctuation options
    parser.add_argument("-a", "--startpunctuation", action="store_true", help="Add punctuation at the start")
    parser.add_argument("-z", "--endpunctuation", action="store_true", help="Add punctuation at the end")
    parser.add_argument("-m", "--middlepunctuation", action="store_true", help="Add punctuation between words")
    
    # Date options
    parser.add_argument("-y", "--year", action="store_true", help="Add years (100 past to 30 future)")
    parser.add_argument("-j", "--ddmm", action="store_true", help="Add days (EU format: ddmm)")
    parser.add_argument("-J", "--mmdd", action="store_true", help="Add days (US format: mmdd)")
    parser.add_argument("-D", "--dateeu", action="store_true", help="Add full dates (EU format: ddmmyyyy)")
    parser.add_argument("-U", "--dateus", action="store_true", help="Add full dates (US format: mmddyyyy)")
    
    # Tool options
    parser.add_argument("-s", "--simulation", action="store_true", help="Only simulate the number of combinations")

    args = parser.parse_args()

    # Verify requirements
    if not args.write and not args.simulation:
        print("Error: -w/--write or -s/--simulation required")
        sys.exit(2)

    # Load and process keywords
    keyWordFile = of.OpenFile(args.keywords)
    keyWordFile.read()
    keyWordFile.loadKeyWord()
    keyWordList = keyWordFile.returnKeyWord()
    
    globalTab = []

    # Process each keyword and its transformations
    for possibilities in keyWordList:
        wordsTab = []
        for string in possibilities:
            clean_str = string.strip()
            if not clean_str: continue
            
            myWord = wd.Word(clean_str)
            if args.leet: myWord.addLeet()
            if args.lowercase: myWord.addLowerCase()
            if args.uppercase: myWord.addUpperCase()
            if args.camel: myWord.addCamelCase()
            if args.optional: myWord.addOptionalWord()
            
            myWord.loadNumbers()
            wordsTab.append(myWord)
        if wordsTab: globalTab.append(wordsTab)
    
    # Initialize the Separator (assembly engine)
    mySeparator = sp.Separator(globalTab)
    if args.disorder: mySeparator.addPermutation()
    if args.startpunctuation: mySeparator.addCharStarted()
    if args.endpunctuation: mySeparator.addCharEnded()
    if args.middlepunctuation: mySeparator.addCharSeparated()
        
    # Inject date options into the generator
    if args.year: mySeparator.addDates(dg.get_years())
    if args.ddmm: mySeparator.addDates(dg.get_days_eu())
    if args.mmdd: mySeparator.addDates(dg.get_days_us())
    if args.dateeu: mySeparator.addDates(dg.get_dates_eu())
    if args.dateus: mySeparator.addDates(dg.get_dates_us())
    
    mySeparator.loadNumbers()
    total_nb = mySeparator.returnNbCombination()

    if args.simulation:
        print(f"{total_nb} possible combinations.")
        return

    # Generation loop
    file = wf.WriteFile(args.write)
    progressBar = None
    seen = set() # Duplicate filter
    
    for i in range(total_nb):
        word = mySeparator.convertNumberInCombination(i)
        
        # Only write unique results
        if word not in seen:
            file.write(word + "\n")
            seen.add(word)
            
        # UI Progress feedback
        if i % max(1, (total_nb // 100)) == 0 or i == total_nb - 1:
            label = f"Processing ({i}/{total_nb})"
            if progressBar is None:
                progressBar = pb.ProgressBar(i, total_nb, label=label)
            else:
                progressBar.updateProgress(i + 1, label)
                
    print("\nGeneration completed successfully.")
    file.close()

if __name__ == "__main__":
    main()
