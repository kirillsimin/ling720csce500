# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:52:51 2015

@author: Kirill
"""



import sys
import csv


import essayclasses.allessaysfile
import essayclasses.anessay
import essayclasses.asentence

exportedDB = 'data/all-essays.csv'

allEssaysFile =  essayclasses.allessaysfile.AllEssaysFile(exportedDB)
allEssays = allEssaysFile.essaysList()

arThatList = []
narThatList = []

count = 0

for anEssay in allEssays:
    
    #if count == 4 : break
    
    thisEssay = essayclasses.anessay.AnEssay(anEssay)
    essayText = thisEssay.getText()
    
    print('')
    
    if thisEssay.isArabic():
        print('ARABIC ESSAY:')
    else:
        print('NON-ARABIC ESSAY:')
    
    for aSentence in thisEssay.getSentences():
        thisSentence = essayclasses.asentence.ASentence(aSentence)
        
        wordNgram = thisSentence.wordNgrams()
        
        #print(wordNgram)

        for thatListOfTouples in wordNgram:
            
            templist = []
            #print('')
            for i in thatListOfTouples:
                #print(i)
                if len(thatListOfTouples) == 5 \
                and thatListOfTouples[2][0] == 'that' :
                    
                    ## POS, word
                    templist.append(i[::-1])
                    
                    ## POS only
                    #templist.append(i[1])
            
            if len(templist) > 0:
                print(templist)
                if thisEssay.isArabic():
                    arThatList.append(templist)
                else:
                    narThatList.append(templist)


    count += 1


    
with open("results/that-ar-concordance.csv", "w", newline='\n') as f:
    writer = csv.writer(f)
    writer.writerows(arThatList)
    
with open("results/that-nar-concordance.csv", "w", newline='\n') as f:
    writer = csv.writer(f)
    writer.writerows(narThatList)
