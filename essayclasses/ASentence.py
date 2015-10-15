import sys
import re
import csv

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer


from collections import defaultdict


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
