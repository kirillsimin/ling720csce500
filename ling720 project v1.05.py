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



   ##### RETURNS A LIST OF ARABIC SPEAKERS' ESSAY FULL INFO #####
    def getArabicEssays(self):
        
        theEssays = []
        self.csvfile = open(studentData, "rU")
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
                    
                        self.curEssay = self.rowAllEssaysInfo
                        
                        theEssays.append(self.curEssay)
                        break

        return theEssays
        
        
        
        
        

    ##### RETURNS A LIST OF NON-ARABIC SPEAKERS' ESSAY FULL INFO #####
    def getNonArabicEssays(self):
        
        theEssays = []
        self.csvfile = open(studentData, "rU")
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
                    
                        self.curEssay = self.rowAllEssaysInfo
                        
                        theEssays.append(self.curEssay)
                        break
    
        return theEssays
        
        

     
   ##### RETURNS A LIST OF ARABIC SPEAKERS' ESSAY TEXTS ONLY #####
    def getArabicEssaysText(self):
        
        theEssays = []
        self.csvfile = open(studentData, "rU")
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
                        
                        theEssays.append(self.theText)
                        break

        return theEssays
        
        

   ##### RETURNS A LIST OF ARABIC SPEAKERS' ESSAY TEXTS ONLY #####
    def getNonArabicEssaysText(self):
        
        theEssays = []
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
                        
                        theEssays.append(self.theText)
                        break

        return theEssays

       
        
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
    def countWords(self):
        self.wordCount = 0
        #self.theEssay = EssayText(self.theText)
        for sentence in (self.sentences):
            for words in sentence:
                self.wordCount += 1
        print('{} words in this essay'.format(self.wordCount))
        return self.wordCount
        

    ##### RETURNS THE DETERMINER COUNT OF THE ESSAY ######            
    def countDTs(self):
        self.dtCount = 0
        #self.theEssay = EssayText(self.theText)
        for sentence in (self.sentences):
            self.thisSentence = ASentence(sentence)
            self.dtCount += self.thisSentence.countDTs()
        print('{} determiners in this essay'.format(self.dtCount))
        return self.dtCount







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
        self.verbCount = 0
        #print(self.theQuestionTokenized)
        for self.word, self.part in self.theSentenceTokenized:
            if 'VB' in self.part:
                self.verbCount += 1
        #print('{} verbs in this sentence'.format(self.verbCount))
        return self.verbCount


    ##### RETURNS THE NUMBER OF DETERMINERS IN THE SENTENCE #####
    def countDTs(self):
        self.dtCount = 0
        #print(self.theQuestionTokenized)
        for self.word, self.part in self.theSentenceTokenized:
            if 'DT' in self.part:
                self.dtCount += 1
        #print('{} determiners in this sentence'.format(self.dtCount))
        return self.dtCount
        
        
    
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


arabicGrade = 0.00
nonArabicGrade = 0

listGrades = set()

for anEssay in arabicEssays:
    
    if anEssay[43] != '0.0':
        #print(anEssay[43])
        arabicGrade += float((anEssay[43]))
        listGrades.add(float(anEssay[43]))
    else:
        #print(anEssay[37])
        arabicGrade += float(anEssay[37])
        listGrades.add(float(anEssay[37]))
    
print(sorted(listGrades))
print(arabicGrade/(len(arabicEssays)))




listGrades = set()
for anEssay in nonArabicEssays:
    
    if anEssay[43] != '0.0':
        #print(anEssay[43])
        arabicGrade += float((anEssay[43]))
        listGrades.add(float(anEssay[43]))
    else:
        #print(anEssay[37])
        nonArabicGrade += float(anEssay[37])
        listGrades.add(float(anEssay[37]))

print(sorted(listGrades))
print(nonArabicGrade/(len(nonArabicEssays)))


sys.exit()



arabicEssaysText = allEssays.getArabicEssaysText()
nonArabicEssaysText = allEssays.getNonArabicEssaysText()



arabicWords = 0
nonArabicWords = 0

arabicQVerbs = 0
nonArabicQVerbs = 0

arabicDTs = 0
nonArabicDTs = 0


# run through each Arabic Essay

for aText in arabicEssaysText:
    
    print('\nESSAY:\n')
        
    thisText = EssayText(aText)

    arabicWords += thisText.countWords()
    
    arabicDTs += thisText.countDTs()
    
    # extracts questions only, counts verbs
    questions = thisText.getQuestions()
    for question in questions:
        thisQuestion = ASentence(question)
        arabicQVerbs += thisQuestion.countVerbs()




# run through each Non-Arabic Essay

for aText in nonArabicEssaysText:
    
    print('\nESSAY:\n')
    
    thisText = EssayText(aText)

    nonArabicWords += thisText.countWords()
    
    nonArabicDTs += thisText.countDTs()
    
    
    # extracts questions only, counts verbs
    questions = thisText.getQuestions()
    for question in questions:
        thisQuestion = ASentence(question)
        nonArabicQVerbs += thisQuestion.countVerbs()






#==============================================================================
# ############## OUTPUT ###########
#==============================================================================


arabicQVerbFreq = arabicQVerbs / len(arabicEssaysText)
nonArabicQVerbFreq = nonArabicQVerbs / len(nonArabicEssaysText)

arabicWordsPerEssay = arabicWords / len(arabicEssaysText)
nonArabicWordsPerEssay = nonArabicWords / len(nonArabicEssaysText)

arabicDTsPerEssay = arabicDTs / len(arabicEssaysText)
nonArabicDTsPerEssay = nonArabicDTs / len(nonArabicEssaysText)

print('\n############## OUTPUT ###########\n')

print('{} arabic essays and {} non-arabic essays'.format(len(arabicEssaysText),len(nonArabicEssaysText)))
print()

print("ARABIC: {} words per essay.".format(arabicWordsPerEssay))
print("NON-ARABIC: {} words per essay.".format(nonArabicWordsPerEssay))

print()

print("ARABIC: {} verbs in questions per essay.".format(arabicQVerbFreq))
print("NON-ARABIC: {} verbs in questions per essay.".format(nonArabicQVerbFreq))


print()

print("ARABIC: {} determiners per essay.".format(arabicDTsPerEssay))
print("NON-ARABIC: {} determiners per essay.".format(nonArabicDTsPerEssay))

