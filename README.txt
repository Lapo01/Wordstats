This code must be run from terminal, its input is a book written in a txt file from https://www.gutenberg.org/. Though one, if needed, can adapt the code for txt files modifying the code if cycle on the presence of the -noIntro key.


IMPORTANT!!!!!!!! One must use python3 and install loguru module for python in order to run the code.


The main cmd line to type in the wordstats folder (use cd and insert the path) is:

python3 wordstats.py name.txt  
# This line will return the number of characters found and time elapsed from code start in seconds.

This line can be concatenated with the following keys

-help 
#This line returns further description of all the keys

-noIntro 
#This line removes any content not included in the book, as specifided at the beginning one can modify the if section depending on this key in the code in order to adapt the code for more txt files.

-hist
#This line return an histogram with the relative occurencies for each letter, special character included. 

-Info
#This line return words count, char counts, lines counts and time elapsed from the code start in seconds.
