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
               
modals = {'can','could','may', 'might', 'must', 'shall', 'should',
          'will', 'would'}

arAux = 0
arQ = 0

nArAux = 0
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
            for aux in auxiliaries:
                if aWord == aux:
                    if thisEssay.isArabic():
                        arAux += 1
                    else:
                        nArAux += 1
    
print ('Arabic Aux per Question: ', arAux/arQ)
print ('Non-Arabic Aux per Question: ', nArAux/nArQ)