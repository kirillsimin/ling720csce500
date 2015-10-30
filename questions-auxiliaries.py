# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:52:51 2015

@author: Kirill
"""



import sys


#==============================================================================
# from essayclasses.allessaysfile import AllEssaysFile
# from essayclasses.asentence import ASentence
# from essayclasses.essaytext import EssayText
#==============================================================================


#from nltk.parse import stanford


import essayclasses.allessaysfile
import essayclasses.anessay

exportedDB = 'data/all-essays.csv'

allEssaysFile =  essayclasses.allessaysfile.AllEssaysFile(exportedDB)
allEssays = allEssaysFile.essaysList()



for anEssay in allEssays:
    thisEssay = essayclasses.anessay.AnEssay(anEssay)
    if thisEssay.isArabic():
        print(thisEssay.getGrade())


auxiliaries = ['be', 'am', 'are', 'is', 'was', 'were', 'being', 'can',
               'could', 'do', 'did', 'does', 'doing', 'have', 'had',
               'has', 'having', 'may', 'might', 'must', 'shall', 'should',
               'will', 'would']

