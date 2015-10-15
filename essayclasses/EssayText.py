import sys
import re
import csv

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

from collections import defaultdict

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


