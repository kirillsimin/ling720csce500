# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:52:51 2015

@author: Kirill
"""



import sys
import csv

from itertools import zip_longest

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

arAsInSentences = ['arabic']
narAsInSentences = ['non-arabic']

arThesInSentences = ['arabic']
narThesInSentences = ['non-arabic']

arDTsInSentences = ['arabic']
narDTsInSentences = ['non-arabic']

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
            dt = dt[0]
            if dt.lower() == 'a' or dt.lower() == 'an':
                indefArt += 1

            if dt.lower() == 'the':
                defArt += 1

        if thisEssay.isArabic():
            arSent += 1
            arA += indefArt
            arThe += defArt
            #arDT += thisSentence.countDTs()
            
            arAsInSentences.append(indefArt)
            arThesInSentences.append(defArt)
            arDTsInSentences.append(thisSentence.countDTs())
            
            #print ('Sentences: ', arSent)
            #print ('Verbs: ', arDT)
        else:
            narSent += 1
            narA += indefArt
            narThe += defArt
            #narDT += thisSentence.countDTs()
            
            narAsInSentences.append(indefArt)
            narThesInSentences.append(defArt)
            narDTsInSentences.append(thisSentence.countDTs())
            
            #print ('Sentences: ', narSent)
            #print ('Verbs: ', narDT)
            

    if thisEssay.isArabic():
        print('Sentences: ',arSent)
        #print('DTs: ',arDT)
        print('A\'s: ', arA)
        print('The\'s: ', arThe)
        #arAtotal += arA
        #arTheTotal += arThe
        #arDTtotal += arDT
        #arSentTotal += arSent
        
    else:
        print('Sentences: ',narSent)
        #print('DTs: ', narDT)
        print('As: ', narA)
        print('The\'s: ', narThe)
        #narAtotal += narA
        #narTheTotal += narThe
        #narDTtotal += narDT
        #narSentTotal += narSent
    
    count += 1


asInSentences = [arAsInSentences,narAsInSentences]
asInSentences = list(zip_longest(*asInSentences, fillvalue=''))

thesInSentences = [arThesInSentences,narThesInSentences]
thesInSentences = list(zip_longest(*thesInSentences, fillvalue=''))

dtsInSentences = [arDTsInSentences,narDTsInSentences]
dtsInSentences = list(zip_longest(*dtsInSentences, fillvalue=''))



with open("results/dt-ind-art.csv", "w", newline='\n') as f:
    writer = csv.writer(f)
    writer.writerows(asInSentences)
        
with open("results/dt-def-art.csv", "w", newline='\n') as f:
    writer = csv.writer(f)
    writer.writerows(thesInSentences)

with open("results/dt-all-dt.csv", "w", newline='\n') as f:
    writer = csv.writer(f)
    writer.writerows(dtsInSentences)




sys.exit()

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