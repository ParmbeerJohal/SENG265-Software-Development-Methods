#Parm Johal
#V00787710
#Seng265 Assignment 3
#filename: formatter.py

#!/opt/local/bin/python

import sys
import calendar
import re

class Formatter:
	#intialize attributes
	def __init__(self, filename=None, inputlines=None):
		self.outputlines = []
		self.inputlines = inputlines
		self.filename = filename
		self.format_dict = {"fmt" : False, "mrgn" : 0, "maxwidth" : 0, "maxwidth_set" : False, "cap" : False, "monthchange" : False, "wordFind": "", "wordReplacement": "", "isReplace" : False}
		self.wordHolder = []

	def get_lines(self):
		if len(self.inputlines) is not 0:
			readlines = self.inputlines
		else:
			readlines = self.filename
		#Reading string of lines from list readlines
		for line in readlines:
			linesplit = line.split()
			#if empty line
			if len(linesplit) is 0:
				finalstring = ""
				self.outputlines.append(finalstring)
			#if format line
			elif linesplit[0] == "?fmt" or linesplit[0] == "?maxwidth" or linesplit[0] == "?cap" or linesplit[0] == "?mrgn" or linesplit[0] == "?monthabbr" or linesplit[0] == "?replace":

				self.detectLine(linesplit)
			else:
				finalstring = self.processLines(line)
				self.outputlines.append(finalstring)
		return self.outputlines



	#This function changes the date format
	def abbreviatemonth(self, line):
		split = line.split()
		monthPattern = re.compile("(\d\d).(\d\d).(\d\d\d\d)?")
		replace = ""
		for m in split:
			match = monthPattern.match(m)
			if match:
				monthlist = match.groups()
				abbr = calendar.month_abbr[int(monthlist[0])]
				replace = abbr + ". " + monthlist[1] + ", " + monthlist[2]
				split[split.index(m)] = replace
		split = [m.rstrip() for m in split]
		line = " ".join(split)
		return line

	#This function replaces a given word
	def replaceword(self, line):
		line = re.sub(self.format_dict["wordFind"], self.format_dict["wordReplacement"], line)
		return line
	#This function changes the margin of the line
	def changemargin(self, line):
		margin = ""
		while len(margin) < int(self.format_dict["mrgn"]):
			margin += " "
		line = margin + line

		return line

	#This function applies formatting on the line
	def processLines(self, line):

		#print("WORDHOLDER AT THE START OF THE METHOD IS:")
		#print(self.wordHolder)


		#if len(self.wordHolder) > 0:
			#for word in self.wordHolder:
				#line.insert(0, word)
			#self.wordHolder = []
			#print("wordholder:")
			#print(self.wordHolder)

		if self.format_dict["fmt"] == False:
			return line
		else:
			if self.format_dict["monthchange"] is True:
				line = self.abbreviatemonth(line)

			if self.format_dict["isReplace"] is True:
				line = self.replaceword(line)

			if self.format_dict["mrgn"] is not 0:
				line = self.changemargin(line)

			#if self.format_dict["maxwidth"] is not 0:
				#string = " ".join(line)
				#charcount = len(string)
				#if len(string) > int(self.format_dict["maxwidth"]):
					#while charcount > int(self.format_dict["maxwidth"]):
						#self.wordHolder.append(line[len(line)-1])
						#wordPopped = line.pop()
						#charcount -= (len(wordPopped) + 1)
				#loop = 0
				#if len(line) == 1:
					#while charcount < int(self.format_dict["maxwidth"]):
						#line[0] += " "
						#loop = loop + 1
						#charcount = charcount + 1
				#else:
					#while charcount < int(self.format_dict["maxwidth"]):
						#line[loop % (len(line) - 1)] += " "
						#loop = loop + 1
						#charcount = charcount + 1
				#print("AFTER BOTH LOOPS, THE FINAL STRING TO RETURN IS:")
		#output = " ".join(line)

		return line


	#This function detects any formatting in the line
	def detectLine(self, line):
		if line[0] == "?fmt":
			if line[1] == "on":
				self.format_dict["fmt"] = True
			else:
				self.format_dict["fmt"] = False
			return None

		if line[0] == "?mrgn":
			self.format_dict["fmt"] = True
			if line[1][0] == "+":
				self.format_dict["mrgn"] = int(self.format_dict["mrgn"]) + int(line[1])
				if int(self.format_dict["mrgn"]) > int(self.format_dict["maxwidth"]) - 20 and self.format_dict["maxwidth_set"] == True:
					self.format_dict["mrgn"] = int(self.format_dict["maxwidth"]) - 20

			elif line[1][0] == "-":
				self.format_dict["mrgn"] =  int(self.format_dict["mrgn"]) + int(line[1])
				if self.format_dict["mrgn"] < 0:
					self.format_dict["mrgn"] = 0

			else:
				self.format_dict["mrgn"] = int(line[1])
			return None

		if line[0] == "?maxwidth":
			self.format_dict["maxwidth_set"] = True

			if line[1][0] == "+":
				self.format_dict["maxwidth"] = int(self.format_dict["maxwidth"]) + int(line[1])
			elif line[1][0] == "-":
				self.format_dict["maxwidth"] = int(self.format_dict["maxwidth"]) + int(line[1])
			else:
				self.format_dict["maxwidth"] = int(line[1])
			return None

		if line[0] == "?monthabbr":
			if line[1] == "on":
				self.format_dict["monthchange"] = True
			else:
				self.format_dict["monthchange"] = False
			return None

		if line[0] == "?replace":
			self.format_dict["isReplace"] = True
			self.format_dict["wordFind"] = line[1]
			self.format_dict["wordReplacement"] = line[2]
			return None
