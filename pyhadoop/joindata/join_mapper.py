#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This mapper code will input a <date word, value> input file, and move date into 
#  the value field for output
#  
#  Note, this program is written in a simple style and does not full advantage of Python 
#     data structures,but I believe it is more readable
#
#  Note, there is NO error checking of the input, it is assumed to be correct
#     meaning no extra spaces, missing inputs or counts,etc..
#
# See #  see https://docs.python.org/2/tutorial/index.html for details  and python  tutorials
#
# --------------------------------------------------------------------------



for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    date     = key_value[0].split(" ")   #key is first item in list
    word   = key_value[1].strip()   #value is 2nd item 

	
        
     #concatenate date, blank, and value_in
    if word=='ABC' or word.isdigit():	        
		print( '%s\t%s' % (date,word))  #print a string, tab, and string
   

#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value

