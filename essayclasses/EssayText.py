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



class EssayText:
    def __init__(self,theText):

        self.sentences = nltk.sent_tokenize(theText)
        self.theText = theText




    def getQuestions(self):
        """ RETURNS A LIST OF QUESTIONS """
        
        listQuestions = []
        for self.sentence in self.sentences:
            if '?' in self.sentence:
                listQuestions.append(self.sentence.strip())

        return listQuestions

        
        
    
    def countWords(self):
        """ RETURNS THE WORD COUNT OF THE ESSAY """
        
        self.wordCount = 0
        #self.theEssay = EssayText(self.theText)
        for sentence in (self.sentences):
            for words in sentence:
                self.wordCount += 1
        print('{} words in this essay'.format(self.wordCount))
        return self.wordCount
        

    
    def countDTs(self):
        """ RETURNS THE DETERMINER COUNT OF THE ESSAY """
        
        self.dtCount = 0
        #self.theEssay = EssayText(self.theText)
        for sentence in (self.sentences):
            self.thisSentence = ASentence(sentence)
            self.dtCount += self.thisSentence.countDTs()
        print('{} determiners in this essay'.format(self.dtCount))
        return self.dtCount


