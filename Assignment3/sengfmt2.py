#Parm Johal
#V00787710
#Seng 265 Assignment 3
#Filename: sengfmt.py


import fileinput
import sys
from formatter import Formatter

def main():



	if len(sys.argv) == 1:
		# READ IN FROM STANDARD INPUT
		lines = [line.rstrip() for line in sys.stdin]
		f = Formatter(inputlines = lines)
	else:
		# READ IN FROM TEXT FILE
		inputfile = open(sys.argv[1])
		lines = [line.rstrip() for line in inputfile]
		f = Formatter(inputlines = lines)

	lines = f.get_lines()
	for l in lines:
		print (l)



if __name__ == "__main__":
    main()
