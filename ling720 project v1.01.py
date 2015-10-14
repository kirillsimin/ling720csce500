# -*- coding: utf-8 -*-
"""
#  Created on Thu Sep 10 09:24:50 2015
#
#  @author: Kirill Simin
#
#
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
"""

#==============================================================================
# ############# import libraries ###########
#==============================================================================

import sys
import re
import csv

import nltk

from collections import defaultdict






#==============================================================================
# ############# Classes ###########
#==============================================================================

class AllEssaysFile():
    
    def __init__(self,theFile):
        csvfile = open(theFile, "r")
        self.allEssayInfo = csv.reader(csvfile, delimiter=',', quotechar='"')
        """
        for self.row in self.allEssayInfo:
            print(self.row[6])
        """
        
    ##### RETURNS ONLY TEXTS OF THE ESSAYS #####
    def getText(self):
        essayTexts = []
        for self.row in self.allEssayInfo:
            self.theText = self.row[6]
            self.theText = self.theText.replace('\n', ' ')
            self.theText = re.sub(' +',' ',self.theText)
            self.theText = self.theText.replace('\t', ' ')
            
            essayTexts.append(self.theText)
        return essayTexts






class EssayText:
    def __init__(self,theText):

        self.sentences = nltk.sent_tokenize(theText)
        self.theText = theText



    ##### RETURNS A LIST OF QUESTIONS #####
    def getQuestions(self):
        listQuestions = []
        for self.sentence in self.sentences:
            if '?' in self.sentence:
                listQuestions.append(self.sentence.strip())
        return listQuestions
        
        
                
    def wordCount(self):
        self.wordCount = 0
        #self.theEssay = EssayText(self.theText)
        for word in (self.theText.split()):
            self.wordCount += 1
        return self.wordCount






class AQuestion:
    
    def __init__(self,theQuestion):
        self.theQuestion = theQuestion.lower()
        self.theQuestionTokenized = nltk.tokenize.word_tokenize(self.theQuestion)
        self.theQuestionTokenized = nltk.pos_tag(self.theQuestionTokenized)
        #print(self.theQuestionTokenized)
        
    
    def getTokenized(self):
        return self.theQuestionTokenized
    
    def countVerbs(self):
        auxCount = 0
        #print(self.theQuestionTokenized)
        for self.word, self.part in self.theQuestionTokenized:
            if 'VB' in self.part:
                auxCount += 1
        return auxCount




#==============================================================================
# ############# Functions ###########
#==============================================================================







#==============================================================================
# ############# declare vars ###########
#==============================================================================

exportedDB = 'data/all-essays.csv'





#==============================================================================
# ############## MAIN BODY ###########
#==============================================================================


allEssays = AllEssaysFile(exportedDB)
textsOnly = allEssays.getText()

for aText in textsOnly:
    
    thisText = EssayText(aText)
    questions = thisText.getQuestions()

    if len(questions) > 0:
        print('WORDS: {}'.format(thisText.wordCount()))

        for question in questions:
            thisQuestion = AQuestion(question)
            numberOfVerbs = thisQuestion.countVerbs()
            
            print('verbs in Q: {}'.format(numberOfVerbs))
    
        print('')

