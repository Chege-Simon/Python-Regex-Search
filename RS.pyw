#! /usr/bin/python3
import logging
logging.basicConfig(filename='RSLog.txt',level=logging.DEBUG, format=' %(asctime)s -%(levelname)s- %(message)s')

# a program that opens all .txt files in a folder
# searches for anyline that matches a user-supplied regular expression.

import re, os
matches = []

path = '/home/peter/Documents/Python/Regex_Search'
logging.info('Starting program')
print('What are we searching for: ')
emailRegex = re.compile(r'''(
				[a-zA-Z0-9._%+-]+		# username
				@						# @ symbol
				[a-zA-Z0-9.-]+			# domain name
				(\.[a-zA-Z]{2,4})		# dot-something
				)''', re.VERBOSE)
phoneRegex = re.compile(r'''(
				("+254"|\d{3}|\d{4})
				(\s|-|\.)?
				(\d{3}|\d{4}|\d{2})
				(\s|-|\.)?
				(\d{7}|\d{4}|\d{3})
				)''', re.VERBOSE)

choice = input('(phone or email): ').lower()
if choice == 'phone':
	logging.info('Cheking type if is phone search')
	searchRegex = re.compile(phoneRegex)
elif choice == 'email':
	logging.info('Cheking type if is email search')
	searchRegex = re.compile(emailRegex)

logging.info('Getting files')

for file in os.listdir(path):
	if file.endswith('.txt'):
		logging.info('finding matches in: %s' % (file))
		f = open(file,'r')
		text = f.read()
		# result = re.search(searchRegex,text)
		# if result != None:
		# 	matches.append(result[0])
		for groups in searchRegex.findall(text):
			matches.append(groups[0])
		f.close()
if len(matches) > 0:
	print('\n'.join(matches))
else:
	print('None found.')

logging.info('Displaying matches')
logging.info('Closing Program')
