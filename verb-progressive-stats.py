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

auxiliaries = {'be', 'am', 'are', 'is', 'was', 'were', 'being',
               'do', 'did', 'does', 'doing', 'have', 'had',
               'has', 'having'}

arVBtotal = 0
arSentTotal = 0

nArVBtotal = 0
nArSentTotal = 0

count = 0

VBGinSent = False
VBGandAUX = False


for anEssay in allEssays:
    
    if count == 3: break
    
    arVB = 0
    arSent = 0
    nArVB = 0
    nArSent = 0
    
    thisEssay = essayclasses.anessay.AnEssay(anEssay)
    essayText = thisEssay.getText()
    
    if thisEssay.isArabic():
        print('\nARABIC ESSAY:')
    else:
        print('\nNON-ARABIC ESSAY:')
    
    for aSentence in thisEssay.getSentences():
        thisSentence = essayclasses.asentence.ASentence(aSentence)
        
        theseVerbs = thisSentence.getVerbs()
        
        '''There are verbs'''
        if len(theseVerbs) > 0:


            '''There are Progressives'''
            for aVerb in theseVerbs:
                if  'VBG' in aVerb:
                    VBGinSent = True
                else:
                    VBGinSent = False
            
            '''There are Auxiliaries'''
            if VBGinSent == True:
                print('\n',thisSentence.getTokens())
                print('\n',thisSentence)
            
                for aVerb in theseVerbs:
                    if aVerb[1] in auxiliaries:
                        VBGandAux = True
                        break
                    else:
                        VBGandAux = False
                print(VBGandAux)
            


    count += 1