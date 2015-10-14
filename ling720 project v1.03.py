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
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer


from collections import defaultdict






#==============================================================================
# ############# Classes ###########
#==============================================================================

class AllEssaysFile():
    
 
    
    def __init__(self,theFile):

        self.csvfile = open(theFile, "r")
        self.readerAllEssaysInfo = csv.reader(self.csvfile, delimiter=',', quotechar='"')

        # list works better than csv.reader object
        self.essaysInfo = []
        for i in self.readerAllEssaysInfo:
            self.essaysInfo.append(i)
        
        ##
        ## allrow[2] is ID
        ## row[6] is the essay
        ##      
     
        #for self.row in self.essaysInfo:
        #    print(self.row[2])



     
   ##### RETURNS A LIST OF ARABIC SPEAKERS' ESSAY TEXTS ONLY #####
    def getArabicEssays(self):
        
        arabicEssays = []
        self.csvfile = open(studentData, "r")
        self.readerStudentInfo = csv.reader(self.csvfile, delimiter='\t')

        # list works better than csv.reader object
        self.studentInfo = []
        for i in self.readerStudentInfo:
            self.studentInfo.append(i)

        # studentInfoIDs = studentInfo[0]
        ## row[3] is the country
        ##    


        for self.rowAllEssaysInfo in self.essaysInfo:
                
            for self.rowStudentInfo in self.studentInfo:
                
                if self.rowStudentInfo[0].replace('-','') == \
                self.rowAllEssaysInfo[2]:
                    
                    if self.rowStudentInfo[3] == 'Saudi Arabia' or\
                    self.rowStudentInfo[3] == 'Oman' or\
                    self.rowStudentInfo[3] == 'Iraq':
                    
                        self.theText = self.rowAllEssaysInfo[6]
                        self.theText = self.theText.replace('\n', ' ')
                        self.theText = re.sub(' +',' ',self.theText)
                        self.theText = self.theText.replace('\t', ' ')
                        
                        arabicEssays.append(self.theText)
                        break

        return arabicEssays
        
        

   ##### RETURNS A LIST OF ARABIC SPEAKERS' ESSAY TEXTS ONLY #####
    def getNonArabicEssays(self):
        
        arabicEssays = []
        self.csvfile = open(studentData, "r")
        self.readerStudentInfo = csv.reader(self.csvfile, delimiter='\t')

        # list works better than csv.reader object
        self.studentInfo = []
        for i in self.readerStudentInfo:
            self.studentInfo.append(i)

        # studentInfoIDs = studentInfo[0]
        ## row[3] is the country
        ##    


        for self.rowAllEssaysInfo in self.essaysInfo:
                
            for self.rowStudentInfo in self.studentInfo:
                
                if self.rowStudentInfo[0].replace('-','') == \
                self.rowAllEssaysInfo[2]:
                    
                    if self.rowStudentInfo[3] != 'Saudi Arabia' and\
                    self.rowStudentInfo[3] != 'Oman' and\
                    self.rowStudentInfo[3] != 'Iraq':
                    
                        self.theText = self.rowAllEssaysInfo[6]
                        self.theText = self.theText.replace('\n', ' ')
                        self.theText = re.sub(' +',' ',self.theText)
                        self.theText = self.theText.replace('\t', ' ')
                        
                        arabicEssays.append(self.theText)
                        break

        return arabicEssays

       
        
    ##### RETURNS ONLY TEXTS OF ALL ESSAYS #####
    def getAllTexts(self):
        essayTexts = []
        for self.row in self.essaysInfo:
            #print(self.row[2])
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

        
        
    ##### RETURNS THE WORD COUNT OF THE ESSAY ######            
    def wordCount(self):
        self.wordCount = 0
        #self.theEssay = EssayText(self.theText)
        for word in (self.theText.split()):
            self.wordCount += 1
        return self.wordCount
        








class ASentence:
    
    def __init__(self,theSentence):
        self.theSentence = theSentence.lower()
        self.theSentenceTokenized = nltk.tokenize.word_tokenize(self.theSentence)
        self.theSentenceTokenized = nltk.pos_tag(self.theSentenceTokenized)
        #print(self.theQuestionTokenized)
        
    
    
    ##### TOKENIZES THE SENTENCE #####
    def getTokens(self):
        return self.theSentenceTokenized
    
    
    
    ##### RETURNS THE NUMBER OF VERBS IN THE SENTENCE #####
    def countVerbs(self):
        auxCount = 0
        #print(self.theQuestionTokenized)
        for self.word, self.part in self.theSentenceTokenized:
            if 'VB' in self.part:
                auxCount += 1
        return auxCount


    ##### RETURNS THE NUMBER OF VERBS IN THE SENTENCE #####
    def countDTs(self):
        dtCount = 0
        #print(self.theQuestionTokenized)
        for self.word, self.part in self.theSentenceTokenized:
            if 'DT' in self.part:
                dtCount += 1
        return dtCount
        
        
    
    ##### RETURNS A LIST: [STEM, WORD, PART OF SPEECH] #####
    def getVerbs(self):
        sentenceVerbs = []
        
        for self.word, self.part in self.theSentenceTokenized:
            if 'VB' in self.part:
                self.tempList = []
                self.stemWord = PorterStemmer().stem_word(self.word)
                self.tempList.append(self.stemWord)
                self.tempList.append(self.word)
                self.tempList.append(self.part)

                sentenceVerbs.append(self.tempList)
                 
        return sentenceVerbs








#==============================================================================
# ############# Functions ###########
#==============================================================================







#==============================================================================
# ############# declare vars ###########
#==============================================================================

exportedDB = 'data/all-essays.csv'
studentData = 'data/students with countries - existing.txt'




#==============================================================================
# ############## MAIN BODY ###########
#==============================================================================


allEssays = AllEssaysFile(exportedDB)

#textsOnly = allEssays.getAllTexts()


arabicEssays = allEssays.getArabicEssays()
nonArabicEssays = allEssays.getNonArabicEssays()



arabicWords = 0
nonArabicWords = 0

arabicVerbs = 0
nonArabicVerbs = 0

arabicDTs = 0
nonArabicDTs = 0


# run through each Arabic Essay

for aText in arabicEssays:
        
    thisText = EssayText(aText)

    arabicWords += thisText.wordCount()
    
#==============================================================================
#     # extracts determiners -- TAKES A LONG TIME
#     for sentence in aText:
#         thisSentence = ASentence(sentence)
#         arabicDTs += thisSentence.countDTs()
#==============================================================================
    
    # extracts questions
    questions = thisText.getQuestions()
    for question in questions:
        thisQuestion = ASentence(question)
        questionVerbs = thisQuestion.getVerbs()
               
        for aVerb in questionVerbs:
            #print(aVerb)
            arabicVerbs += 1


# run through each Non-Arabic Essay

for aText in nonArabicEssays:
    
    thisText = EssayText(aText)

    nonArabicWords += thisText.wordCount()
    
#==============================================================================
#     # extracts determiners -- TAKES A LONG TIME
#     for sentence in aText:
#         thisSentence = ASentence(sentence)
#         nonArabicDTs += thisSentence.countDTs()
#==============================================================================
    
    # extracts questions
    questions = thisText.getQuestions()
    for question in questions:
        thisQuestion = ASentence(question)
        questionVerbs = thisQuestion.getVerbs()
        
        for aVerb in questionVerbs:
            #print(aVerb)
            nonArabicVerbs += 1
        
        
arabicVerbFreq = arabicVerbs / len(arabicEssays)
nonArabicVerbFreq = nonArabicVerbs / len(nonArabicEssays)

arabicWordsPerEssay = arabicWords / len(arabicEssays)
nonArabicWordsPerEssay = nonArabicWords / len(nonArabicEssays)

arabicDTsPerEssay = arabicDTs / len(arabicEssays)
nonArabicDTsPerEssay = nonArabicDTs / len(nonArabicEssays)


print("ARABIC: {} words per essay.".format(arabicWordsPerEssay))
print("NON-ARABIC: {} words per essay.".format(nonArabicWordsPerEssay))

print()

print("ARABIC: {} verbs in questions per essay.".format(arabicVerbFreq))
print("NON-ARABIC: {} verbs in questions per essay.".format(nonArabicVerbFreq))



#==============================================================================
# print()
# 
# print("ARABIC: {} determiners per essay.".format(arabicDTsPerEssay))
# print("NON-ARABIC: {} determiners per essay.".format(nonArabicDTsPerEssay))
#==============================================================================

