# WordListGenerator

Generate your own word list using your key words

## Required
Python 3+ is required

## Python help documentation:
```
> wordListGenerator.py -h
Word list generator v0.1
Build your own word list using key words that will be transformed with leet, uppercase, lowercase, punctuation, etc.
Usage:
wordListGenerator [options]
-h/--help				show this help message and exit
-w/--write file		(Required)	specifie the path for writing the word list
-k/--keywords file	(Required)	specifie the path for reading the keywords list
-l/--leet				using leet conversion
-C/--uppercase				using uppercase conversion
-c/--lowercase				using lowercase conversion
-e/--camel                  using camelcase conversion
-o/--optional				make each word optional
-d/--disorder				generate combinations with all possible word orders
-a/--startpunctuation			using optional punctuation sign like '*,!.' and more at the begin of the chain
-z/--endpunctuation			using optional punctuation sign like '*,!.' and more at the end of the chain
-m/--middlepunctuation			using optional punctuation sign like '*,!.' and more between each word of the chain
-s/--simulation				only making a simulation of the possibilities number (no wordlist generated)
```
## Keywords file
<pre>
The keywords file must respect some details:
	- you can specify multiple words on the same line (separated by a ',') for a variant word
	- differents words are on differents lines
For example:

keywords.txt
```
black,white,grey
hat
```

result.txt
```
blackhat
whitehat
greyhat
Blackhat
[...]
```
</pre>
## Example use and output
```
> wordListGenerator.py -k Desktop\keywords.txt -l -c -C -w Desktop\results.txt
```
