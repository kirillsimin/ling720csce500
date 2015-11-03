# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:52:51 2015

@author: Kirill
"""



import sys


#from nltk.parse import stanford


import essayclasses.allessaysfile
import essayclasses.anessay
import essayclasses.asentence

exportedDB = 'data/all-essays.csv'

allEssaysFile =  essayclasses.allessaysfile.AllEssaysFile(exportedDB)
allEssays = allEssaysFile.essaysList()



arVBtotal = 0
arSentTotal = 0



nArVBtotal = 0
nArSentTotal = 0


for anEssay in allEssays:
    arVB = 0
    arSent = 0
    nArVB = 0
    nArSent = 0
    
    thisEssay = essayclasses.anessay.AnEssay(anEssay)
    essayText = thisEssay.getText()
    
    if thisEssay.isArabic():
        print('ARABIC ESSAY:')
    else:
        print('NON-ARABIC ESSAY:')
    
    for aSentence in thisEssay.getSentences():
        thisSentence = essayclasses.asentence.ASentence(aSentence)
        if thisEssay.isArabic():
            arSent += 1
            arVB += thisSentence.countVerbs()
            #print ('Sentences: ', arSent)
            #print ('Verbs: ', arVB)
        else:
            nArSent += 1
            nArVB += thisSentence.countVerbs()
            #print ('Sentences: ', nArSent)
            #print ('Verbs: ', nArVB)

    if thisEssay.isArabic():
        print('Sentences: ',arSent)
        print('Verbs: ',arVB)
        arVBtotal += arVB
        arSentTotal += arSent
        
    else:
        print('Sentences: ',nArSent)
        print('Verbs: ', nArVB)
        nArVBtotal += nArVB
        nArSentTotal += nArSent 


print ('Arabic Sentences: ',arSentTotal)
print ('Arabic Verbs per Sentence: ', arVBtotal/arSentTotal)
print ('Non-Arabic Sentences: ',nArSentTotal)
print ('Non-Arabic Verbs per Sentence: ', nArVBtotal/nArSentTotal)