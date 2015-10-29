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



import nltk
#from nltk.stem import PorterStemmer
#from nltk.stem import LancasterStemmer

from essayclasses.asentence import ASentence



class AnEssay:
    def __init__(self,theEssay):

        
        self._theText = theEssay[6]




    def getQuestions(self):
        """ RETURNS A LIST OF QUESTIONS """
        
        self._sentences = nltk.sent_tokenize(self._theText)
        
        self._listQuestions = []
        for self._sentence in self._sentences:
            if '?' in self._sentence:
                self._listQuestions.append(self._sentence.strip())

        return self._listQuestions

        
        
    
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


