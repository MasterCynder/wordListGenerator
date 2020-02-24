import sys

def usage():
    print("Word list generator v0.1")
    print("Build your own word list using key word that will be transformed with leet, uppercase, lowercase, punctuation, etc. ")
    print("Usage:")
    print("wordListGenerator [options]")
    print("-w/--write       (Required)  specifie the path for writing the word list")
    print("-k/--keywords    (Required)  specifie the path for writing the word list")
    print("-l/--leet                    using leet conversion")
    print("-C/--uppercase               using uppercase conversion")
    print("-c/--lowercase               using lowercase conversion")
    print("-s/--simulation              only making a simulation of the possibilities number (no wordlist generated)")