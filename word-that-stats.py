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

arThatCount = 0
narThatCount = 0

count = 0

for anEssay in allEssays:
    
    #if count == 4 : break
    
    thisEssay = essayclasses.anessay.AnEssay(anEssay)
    
    print('')
    
    if thisEssay.isArabic():
        print('ARABIC ESSAY:')
    else:
        print('NON-ARABIC ESSAY:')
    
    for aSentence in thisEssay.getSentences():
        
        for aWord in aSentence.split():
            #print(aWord)
            if aWord.lower() == 'that':
                
                if thisEssay.isArabic():
                    arThatCount += 1
                    print(arThatCount)
                else:
                    narThatCount += 1
                    print(narThatCount)
        

    count += 1


print('')    
print('Arabic thats: ', arThatCount)
print('Non-Arabic thats: ', narThatCount)