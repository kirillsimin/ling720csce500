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


import essayclasses.allessaysfile

exportedDB = 'data/all-essays.csv'

allEssays =  essayclasses.allessaysfile.AllEssaysFile(exportedDB)

