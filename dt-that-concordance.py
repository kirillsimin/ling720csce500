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

arDTlist = []
narDTlist = []

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
        
        dtNgram = thisSentence.posNgrams()
        
        #print(dtNgram)

        for dtListOfTouples in dtNgram:
            
            templist = []
            #print('')
            for i in dtListOfTouples:
                #print(i)
                if len(dtListOfTouples) == 5 \
                and dtListOfTouples[2][0] == 'that' :
                    templist.append(i[::-1])
            
            if len(templist) > 0:
                print(templist)
                if thisEssay.isArabic():
                    arDTlist.append(templist)
                else:
                    narDTlist.append(templist)


    count += 1


    
with open("results/dt-ar-that-concordance.csv", "w", newline='\n') as f:
    writer = csv.writer(f)
    writer.writerows(arDTlist)
    
with open("results/dt-nar-that-concordance.csv", "w", newline='\n') as f:
    writer = csv.writer(f)
    writer.writerows(narDTlist)
