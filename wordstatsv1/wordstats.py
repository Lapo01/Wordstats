import argparse
import time
from loguru import logger
from matplotlib import pyplot as plt


parser = argparse.ArgumentParser(prog='wordcount', 
				 description ='This code counts letters in a txt file and return a hist with relative frequency for each letter in the alphabet, total characters and lines count separately and elapsed time for the executon of the code.\n No distinction is made between uppercase and lowercase characters, special char count is not neglected. \n In order to run this code, one must insert after the executing line the file path of the txt file. \n This code works only for books in txt formats from https://www.gutenberg.org/ ')


parser.add_argument('-hist',help = 'Type -hist after the file name.txt in order to display an histogram with relative frequencies of the letters', action = 'store_true' )


parser.add_argument('-noIntro',help ='Type -noIntro after the file name.txt in order to use only the book content to make the statistic ', action = 'store_true') 


parser.add_argument('infile')

parser.add_argument('-Info', help = 'Type -info for number of lines, number of characters and number of words.', action = 'store_true')
"""
The upward code section is used to make --help section

"""



def process_file(file_path):
	"""
	"""
	logger.info(f'Opening input file{file_path}...')
	with open(file_path) as input_file:
		global data                                   
		"""
		global is used to make avaiable to the code the variable after using the cmd 				 	
		program	
		"""	
		data = input_file.read()
	logger.info(f'Done, {len(data)} character(s) found.')
	
	

if __name__ == '__main__': # will only be executed if from command line, if imported it won't
	args = parser.parse_args()  
	process_file(args.infile)
print(args)


tic = time.time()

lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

uppercase = ['A','B','C','D','E','F','G','H','U','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

placeholder = range(1, len(uppercase)+1)
count = [0] * len(lowercase)
if args.noIntro:
	logger.info(f'Statistics is being done just for the book content')
	a = data.split('*** START OF THE PROJECT GUTENBERG EBOOK THE REPUBLIC ***')
	data = a[1]


for i, item1 in enumerate(lowercase):
	for item2 in data:
		if item2 == item1:
			count[i]+=1
		if item2 == 'è' or item2 =='é' :
			count[5] +=1 
		if item2 == 'à' :
			count[1]+=1
		if item2 == 'ò':
			count[15]+=1
		if item2 =='ù':
			count[21]+=1
for i, item1 in enumerate(uppercase):
	for item2 in data:
		if item2 == item1:
			count[i] += +1

	
count = [ii/sum(count) for ii in count]
	
 #i use those two variable to start the count of lines and words.
lines = 0
words = 0 #i use those two variable to start the count of lines and words.
for item in data:
	if item == '\n':
		lines =lines+1
	
for item in data:
	if item == ' ':
		words = words+1
toc = time.time() - tic


if args.Info:
	logger.info(f'{len(data)} character(s) found.')
	logger.info(f'Number of line(s) is {lines}')
	logger.info(f'Elapsed Time is {toc} second(s)')
	logger.info(f'{words} word(s) found.')




if args.hist:
	

	plt.bar(placeholder, count, align ='center')
	plt.ylabel('Counts')
	plt.xlabel('Letter[enumerated with numbers from 1 to 26]')
	plt.show()




logger.info(f'Elapsed Time is {toc} second(s)')




