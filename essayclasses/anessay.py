"""
#
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


import csv

import nltk
#from nltk.stem import PorterStemmer
#from nltk.stem import LancasterStemmer

from essayclasses.asentence import ASentence

studentData = 'data/students with countries - existing.txt'


class AnEssay:
    def __init__(self,theEssay):

        
        self._theText = theEssay[6]
        self._theEssay = theEssay
        
    def getText(self):
        return self._theText

    def getGrade(self):
        """ RETURNS THE ESSAYS'S FINAL GRADE """
        self._theGrade = 0
        
        self._average = self._theEssay[37]
        self._override = self._theEssay[43]
        
        if float(self._override) != 0:
            return float(self._override)
        else:
            return float(self._average)
        

    def isArabic(self):
        """ RETURNS TRUE IF THE AUTHOR'S L1 IS ARABIC """
        
        self._theEssays = []
        self._isArabic = bool
        
        self._csvfile = open(studentData, "rU")
        self._readerStudentInfo = csv.reader(self._csvfile, delimiter='\t')
        
        # list works better than csv.reader object
        self._studentInfo = []
        for i in self._readerStudentInfo:
            self._studentInfo.append(i)

        ## studentInfo[0] is the ID
        ## studentInfo[3] is the country
        ##
        ## theEssay[2] is the ID
        ## theEssay[6] is the essay
                
        for self._rowStudentInfo in self._studentInfo:
            
            if self._rowStudentInfo[0].replace('-','') == \
            self._theEssay[2]:
                
                if self._rowStudentInfo[3] == 'Saudi Arabia' or\
                self._rowStudentInfo[3] == 'Oman' or\
                self._rowStudentInfo[3] == 'Iraq':
                
                    self._isArabic = True
                else:
                    self._isArabic = False

        return self._isArabic
        



    def getQuestions(self):
        """ RETURNS A LIST OF QUESTIONS """
        
        self._sentences = nltk.sent_tokenize(self._theText)
        
        self._listQuestions = []
        for self._sentence in self._sentences:
            if '?' in self._sentence:
                self._listQuestions.append(self._sentence.strip())

        return self._listQuestions

    def getSentences(self):
        """ RETURNS A LIST OF SENTENCES """
        
        self._sentences = nltk.sent_tokenize(self._theText)
        
        self._listSentences = []
        for self._sentence in self._sentences:
            self._listSentences.append(self._sentence.strip())

        return self._listSentences
    
    def countWords(self):
        """ RETURNS THE WORD COUNT OF THE ESSAY """
        
        self._sentences = nltk.sent_tokenize(self._theText)
        
        self._wordCount = 0
        #self._theEssay = EssayText(self._theText)
        for self._sentence in self._sentences:
            for self._words in self._sentence:
                self._wordCount += 1
        print('{} words in this essay'.format(self._wordCount))
        return self._wordCount
        

    
    def countDTs(self):
        """ RETURNS THE DETERMINER COUNT OF THE ESSAY """
        
        self._sentences = nltk.sent_tokenize(self._theText)
        
        self._dtCount = 0
        #self._theEssay = EssayText(self._theText)
        for sentence in (self._sentences):
            self._thisSentence = ASentence(sentence)
            self._dtCount += self._thisSentence.countDTs()
        print('{} determiners in this essay'.format(self._dtCount))
        return self._dtCount


