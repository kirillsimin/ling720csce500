# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:52:51 2015

@author: Kirill
"""



import sys


#from nltk.parse import stanford

from collections import defaultdict

import essayclasses.allessaysfile
import essayclasses.anessay
import essayclasses.asentence

exportedDB = 'data/all-essays.csv'

allEssaysFile =  essayclasses.allessaysfile.AllEssaysFile(exportedDB)
allEssays = allEssaysFile.essaysList()

arDTtotal = 0
arAtotal = 0
arTheTotal = 0
arSentTotal = 0

narDTtotal = 0
narAtotal = 0
narTheTotal = 0
narSentTotal = 0

arDTdict = defaultdict(int)
narDTdict = defaultdict(int)

count = 0

for anEssay in allEssays:
    
    #if count == 4 : break
    
    arDT = 0
    arA = 0
    arThe = 0
    arSent = 0
    
    narA = 0
    narThe = 0
    narDT = 0
    narSent = 0
    
    thisEssay = essayclasses.anessay.AnEssay(anEssay)
    essayText = thisEssay.getText()
    
    print('')
    
    if thisEssay.isArabic():
        print('ARABIC ESSAY:')
    else:
        print('NON-ARABIC ESSAY:')
    
    for aSentence in thisEssay.getSentences():
        thisSentence = essayclasses.asentence.ASentence(aSentence)
        
        indefArt = 0
        defArt = 0

        dts = thisSentence.getDTs()
        for dt in dts:
            dt = dt[0].lower()
            
            if dt == 'a' or dt == 'an':
                indefArt += 1
            if dt == 'the':
                defArt += 1
            
            if thisEssay.isArabic():
                arDTdict[dt] += 1
            else:
                narDTdict[dt] += 1
                
        if thisEssay.isArabic():
            arSent += 1
            arA += indefArt
            arThe += defArt
            arDT += thisSentence.countDTs()
            #print ('Sentences: ', arSent)
            #print ('Verbs: ', arDT)
        else:
            narSent += 1
            narA += indefArt
            narThe += defArt
            narDT += thisSentence.countDTs()
            #print ('Sentences: ', narSent)
            #print ('Verbs: ', narDT)

    if thisEssay.isArabic():
        print('Sentences: ',arSent)
        print('DTs: ',arDT)
        print('A\'s: ', arA)
        print('The\'s: ', arThe)
        arAtotal += arA
        arTheTotal += arThe
        arDTtotal += arDT
        arSentTotal += arSent
        
    else:
        print('Sentences: ',narSent)
        print('DTs: ', narDT)
        print('As: ', narA)
        print('The\'s: ', narThe)
        narAtotal += narA
        narTheTotal += narThe
        narDTtotal += narDT
        narSentTotal += narSent
    
    count += 1

arDTList = []
tuplesDTsCount = arDTdict.items()
for i in tuplesDTsCount:
    if i[1] >= 10:
        arDTList.append(i[::-1])
    
narDTList = []
tuplesDTsCount = narDTdict.items()
for i in tuplesDTsCount:
    if i[1] >= 10:
        narDTList.append(i[::-1])

print('')
print('Arabic DT\'s:')
print(sorted(arDTList, reverse = True))
print('')
print('Non-Arabic DT\'s:')
print(sorted(narDTList, reverse = True))

print('')
print ('Arabic Sentences: ',arSentTotal)
print ('Arabic DTs per Sentence: ', arDTtotal/arSentTotal)
print ('Arabic A\'s per Sentence: ', arAtotal/arSentTotal)
print ('Arabic The\'s per Sentence: ', arTheTotal/arSentTotal)

print('')

print ('Non-Arabic Sentences: ',narSentTotal)
print ('Non-Arabic DTs per Sentence: ', narDTtotal/narSentTotal)
print ('Non-Arabic As per Sentence: ', narAtotal/narSentTotal)
print ('Non-Arabic The\'s per Sentence: ', narTheTotal/narSentTotal)