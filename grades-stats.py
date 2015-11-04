# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 01:24:56 2015

@author: Kirill
"""

import sys

import essayclasses.allessaysfile
import essayclasses.anessay

exportedDB = 'data/all-essays.csv'

allEssaysFile =  essayclasses.allessaysfile.AllEssaysFile(exportedDB)
allEssays = allEssaysFile.essaysList()


arabicGradesTotal = 0
nonArabicGradesTotal = 0

arabicCount = 0
nonArabicCount = 0

for anEssay in allEssays:
    thisEssay = essayclasses.anessay.AnEssay(anEssay)

    if thisEssay.isArabic():
        arabicGradesTotal += thisEssay.getGrade()
        arabicCount += 1
    else:
        nonArabicGradesTotal += thisEssay.getGrade()
        nonArabicCount += 1
        
print('Arabic Avg Grade: ', arabicGradesTotal/arabicCount)
print('Non-Arabic Avg Grade:', nonArabicGradesTotal/nonArabicCount)