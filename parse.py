#!/usr/bin/env python
# coding: utf-8


# Language Processing Script

import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import itertools
import threading
import time
import sys
import re
import os


##############################################
#
# Important Variables!
#
##############################################
#Auto high frequency detection value (%)
stopFreq = 1

#Stop Characters ignored in sources
stopChars = "(,.;?\-:)"

sourceDir = "sources"

#First run - Install NLTK Dependancy
firstRun = False

##############################################


source = ""



os.chdir(sourceDir)
    
#Loading - it might take awhile!
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rParsing ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rComplete!\n')

if firstRun:
    nltk.download('punkt')
    print("Re-run now with first run turned off!")
    sys.exit()


print ("\033[1m\033[92m  ______ _                          ")
print (" / _____|_)                         ")
print ("( (____  _  ___  _   _ _____ ____   ")
print (" \____ \| |/ _ \| | | (____ |  _ \  ")
print (" _____) ) | |_| | |_| / ___ | | | | ")
print ("(______/|_|\___/|____/\_____|_| |_| ")
print ("                                    ")
print (" ______                             ")
print ("(_____ \                            ")
print (" _____) )____  ____ ___ _____  ____ ")
print ("|  ____(____ |/ ___)___) ___ |/ ___)")
print ("| |    / ___ | |  |___ | ____| |    ")
print ("|_|    \_____|_|  (___/|_____)_|    ")
print ("\033[95mv0.01\033[0m \n")



#Join all sources files found within source directory into 'source'
print ("Parsing Source <" + sourceDir + "> directory...")
for filename in os.listdir(os.getcwd()):
    with open(os.path.join(os.getcwd(), filename), encoding="utf8") as f:
        source = source + f.read()
        print ("Processed: " + filename)
print (str(len(os.listdir(os.getcwd()))) + " File(s) Processed.\n")



#Load Stopwords
os.chdir("../")

#with open(os.getcwd() + '\\stopwords.txt') as f:
#    stopwords = f.read().splitlines()

t = threading.Thread(target=animate)
t.start()

#Clean up input
parsed = ''.join([i for i in source if not i.isdigit()]) #Remove numbers
parsed = parsed.replace('\n', ' ').replace('\r', '') #Remove newline
parsed = re.sub(' +', ' ', parsed) #Remove extra spaces
parsed = re.sub('[' + stopChars + ']', '', parsed) #Remove stop characters
parsed = parsed.lower() #Set to all lowercase

#Begin NLTK Processing
tokens = word_tokenize(parsed)
fdist = FreqDist(tokens)

done = True
time.sleep(0.1)
print ('\033[1m')
print("Top 100 Frequency Distribution")

for i in enumerate(fdist.most_common(100)): 
    print("\t" + str(i[0]+1) + ". " + i[1][0] + " (" + str(i[1][1]) + " times) (" + str(round(fdist.freq(i[1][0])*100,2)) + "%)")
    if round(fdist.freq(i[1][0])*100,2) > stopFreq:
        print ("\033[91m \t\t> High Frequency: Possible Stop Word!\033[0m\033[1m")

print ('\033[0m')

print("\nStop Characters used: " + stopChars)
print("Stop Word Frequency Detection Threshold: " + str(stopFreq) + "%")
print(str(len(tokens)) + " Tokens Generated.")


# In[ ]:




