#!/usr/bin/env python
import sys
import string

stops = ['and', 'the', 'i', 'he', 'she', 'they', 'them', 'us', 'but', 'am', 'on', 'me', 'you', 'up', 'down',
	'left', 'right', 'over', 'under', 'about', 'if', 'her', 'him']

#create translator for mapping punctuations to whitespace
#see https://stackoverflow.com/questions/34860982/replace-the-punctuation-with-whitespace/34922745
translator = string.maketrans(string.punctuation, ' '*len(string.punctuation))

#iterate over each line
for line in sys.stdin:
    #remove leading and trailing whitespace
    line = line.strip().lower()
    line = line.translate(translator)
    
    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if word not in stops:
        	print '%s\t%s' % (word, "1")
