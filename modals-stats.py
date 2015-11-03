# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 02:01:35 2015

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


               
modals = {'can','could','may', 'might', 'must', 'shall', 'should',
          'will', 'would'}

araM = 0
arQ = 0

nArM = 0
nArQ = 0


for anEssay in allEssays:
    thisEssay = essayclasses.anessay.AnEssay(anEssay)
    questions = thisEssay.getQuestions()
    
    for aQuestion in questions:
        if thisEssay.isArabic():
            arQ += 1
        else:
            nArQ += 1
        for aWord in aQuestion.split():
            for aux in modals:
                if aWord == aux:
                    if thisEssay.isArabic():
                        arM+= 1
                    else:
                        nArM += 1
    
print ('Arabic Modals per Question: ',arM/arQ)
print ('Non-Arabic Modals per Question: ',nArM/nArQ)