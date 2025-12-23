# WordListGenerator

Generate your own word list using your key words

## Required
Python 3+ is required

## Python help documentation:
```
> wordListGenerator.py -h
Word list generator v0.1
Build your own word list using key words that will be transformed with leet, uppercase, lowercase, punctuation, etc.
Usage: python wordListGenerator.py [options]
-h/--help				show this help message and exit
Required:
-w/--write file		    	Specifie the path for writing the word list
-k/--keywords file		    Specifie the path for reading the keywords list
Options:
-l/--leet				    Using leet conversion
-C/--uppercase				Using uppercase conversion
-c/--lowercase				Using lowercase conversion
-e/--camel                  Using camelcase conversion
-o/--optional				Make each word optional
-d/--disorder				Generate combinations with all possible word orders
-a/--startpunctuation		Using optional punctuation sign like '*,!.' and more at the begin of the chain
-z/--endpunctuation			Using optional punctuation sign like '*,!.' and more at the end of the chain
-m/--middlepunctuation		Using optional punctuation sign like '*,!.' and more between each word of the chain
-y/--year                   Add years (100 past to 30 future)
-j/--ddmm                   Add days (EU format: ddmm)
-J/--mmdd                   Add days (US format: mmdd)
-D/--dateeu                 Add full dates (EU format: ddmmyyyy)
-U/--dateus                 Add full dates (US format: mmddyyyy)
-s/--simulation				Only making a simulation of the possibilities number (no wordlist generated)

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
