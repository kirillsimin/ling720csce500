# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:52:51 2015

@author: Kirill
"""



import sys
import csv


#from nltk.parse import stanford


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

listAsInSentences = []
listAsInSentences.append(['arabic','non-arabic'])

listThesInSentences = []
listThesInSentences.append(['arabic','non-arabic'])

listDTsInSentences = []
listDTsInSentences.append(['arabic','non-arabic'])


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
        listArabicNonArabicAs = [0,0]
        listArabicNonArabicThes = [0,0]
        listArabicNonArabicDTs = [0,0]

        dts = thisSentence.getDTs()
        for dt in dts:
            dt = dt[0]
            if dt.lower() == 'a':
                indefArt += 1

            if dt.lower() == 'the':
                defArt += 1

        if thisEssay.isArabic():
            arSent += 1
            arA += indefArt
            arThe += defArt
            #arDT += thisSentence.countDTs()
            
            listArabicNonArabicAs[0] = indefArt
            listArabicNonArabicThes[0] = defArt
            listArabicNonArabicDTs[0] = thisSentence.countDTs()
            
            #print ('Sentences: ', arSent)
            #print ('Verbs: ', arDT)
        else:
            narSent += 1
            narA += indefArt
            narThe += defArt
            #narDT += thisSentence.countDTs()
            
            listArabicNonArabicAs[1] = indefArt
            listArabicNonArabicThes[1] = defArt
            listArabicNonArabicDTs[1] = thisSentence.countDTs()
            
            #print ('Sentences: ', narSent)
            #print ('Verbs: ', narDT)
            
        listAsInSentences.append(listArabicNonArabicAs)
        listThesInSentences.append(listArabicNonArabicThes)
        listDTsInSentences.append(listArabicNonArabicDTs)

    if thisEssay.isArabic():
        print('Sentences: ',arSent)
        print('DTs: ',arDT)
        print('A\'s: ', arA)
        print('The\'s: ', arThe)
        #arAtotal += arA
        #arTheTotal += arThe
        #arDTtotal += arDT
        #arSentTotal += arSent
        
    else:
        print('Sentences: ',narSent)
        print('DTs: ', narDT)
        print('As: ', narA)
        print('The\'s: ', narThe)
        #narAtotal += narA
        #narTheTotal += narThe
        #narDTtotal += narDT
        #narSentTotal += narSent
    
    count += 1


with open("dt-ind-art.csv", "w", newline='\n') as f:
    writer = csv.writer(f)
    
    for i in listAsInSentences:
        writer.writerows([i])

with open("dt-def-art.csv", "w", newline='\n') as f:
    writer = csv.writer(f)
    
    for i in listThesInSentences:
        writer.writerows([i])

with open("dt-all-dt.csv", "w", newline='\n') as f:
    writer = csv.writer(f)
    
    for i in listDTsInSentences:
        writer.writerows([i])
