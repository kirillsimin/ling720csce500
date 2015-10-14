# -*- coding: utf-8 -*-
"""
#  Created on Thu Sep 10 09:24:50 2015
#
#  @author: Kirill Simin
#
#
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
"""

############# import libraries ###########

import nltk

from collections import defaultdict






############# Classes ###########







############# Functions ###########


    






############# declare vars ###########

fileEssays = open('data/shakespeare-hamlet.txt')

partsStat = defaultdict(int)

dictParts = defaultdict(int)

listPartsFreqs = []





### prep essays ###

readEssays = fileEssays.read()

splitEssays = readEssays.split('.')







### build dict of parts of speech ###



sentenceCounter = 0 ### temporary counter
tooManyStentences = 1000 ### temporary limit

for sentence in splitEssays:
    #sentence += '.'
    #print(sentence)
    
    tokens = nltk.word_tokenize(sentence)
    parts = nltk.pos_tag(tokens)
    
    for i in parts:
        
        word = i[0]
        part = i[1]
        
        dictParts[part] += 1
        #print ('%-4s %20s' % (word, part ))


    
    ###  temporary blocker
    if sentenceCounter == tooManyStentences:
        break 
    else:
        sentenceCounter += 1
        continue
    ###  end temporary blocker    







### built list of parts and their freqs ###

tuplesPartsFreqs = dictParts.items() #items() creates TUPLES out of dict

for part,freq in tuplesPartsFreqs:
    listPartsFreqs.append([freq,part])

for i in sorted(listPartsFreqs, reverse = True):
    print(i)




