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
from nltk.stem import PorterStemmer






class ASentence:
    
    def __init__(self,theSentence):
        self.theSentence = theSentence.lower()
        self.theSentenceTokenized = nltk.tokenize.word_tokenize(self.theSentence)
        self.theSentenceTokenized = nltk.pos_tag(self.theSentenceTokenized)
        #print(self.theQuestionTokenized)
        
    
    
    
    def getTokens(self):
        """ TOKENIZES THE SENTENCE """
        
        return self.theSentenceTokenized
    
    
    
    
    def countVerbs(self):
        """ RETURNS THE NUMBER OF VERBS IN THE SENTENCE """
        
        self.verbCount = 0
        #print(self.theQuestionTokenized)
        for self.word, self.part in self.theSentenceTokenized:
            if 'VB' in self.part:
                self.verbCount += 1
        #print('{} verbs in this sentence'.format(self.verbCount))
        return self.verbCount


    
    def countDTs(self):
        """ RETURNS THE NUMBER OF DETERMINERS IN THE SENTENCE """
        
        self.dtCount = 0
        #print(self.theQuestionTokenized)
        for self.word, self.part in self.theSentenceTokenized:
            if 'DT' in self.part:
                self.dtCount += 1
        #print('{} determiners in this sentence'.format(self.dtCount))
        return self.dtCount
        
    
    def getVerbs(self):
        """ RETURNS A LIST: [STEM, WORD, PART OF SPEECH] """
        
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
