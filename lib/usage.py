import sys

def usage():
    print("Word list generator v0.1")
    print("Build your own word list using key words that will be transformed with leet, uppercase, lowercase, punctuation, etc. ")
    print("Usage:")
    print("wordListGenerator [options]")
    print("-h/--help						show this help message and exit")
    print("-w/--write file      (Required)  specifie the path for writing the word list")
    print("-k/--keywords file   (Required)  specifie the path for writing the word list")
    print("-l/--leet                        using leet conversion")
    print("-C/--uppercase                   using uppercase conversion")
    print("-c/--lowercase                   using lowercase conversion")
    print("-o/--optional                    make each word optional")
    print("-s/--simulation                  only making a simulation of the possibilities number (no wordlist generated)")