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
        self._theSentence = theSentence
        self._theSentenceTokenized = nltk.tokenize.word_tokenize(self._theSentence)
        self._theSentenceTokenized = nltk.pos_tag(self._theSentenceTokenized)
        #print(self._theQuestionTokenized)
        
    
    def __str__(self):
        return(self._theSentence)
    
    def getTokens(self):
        """ TOKENIZES THE SENTENCE """
        
        return self._theSentenceTokenized
    
    
    
    
    def countVerbs(self):
        """ RETURNS THE NUMBER OF VERBS IN THE SENTENCE """
        
        self._verbCount = 0
        #print(self._theQuestionTokenized)
        for self._word, self._part in self._theSentenceTokenized:
            if 'VB' in self._part:
                self._verbCount += 1
        #print('{} verbs in this sentence'.format(self._verbCount))
        return self._verbCount


    
    def countDTs(self):
        """ RETURNS THE NUMBER OF DETERMINERS IN THE SENTENCE """
        
        self._dtCount = 0
        #print(self._theQuestionTokenized)
        for self._word, self._part in self._theSentenceTokenized:
            if 'DT' in self._part:
                self._dtCount += 1
        #print('{} determiners in this sentence'.format(self._dtCount))
        return self._dtCount

    def getDTs(self):
        """ RETURNS A LIST: [STEM, WORD, PART OF SPEECH] """
        
        self._sentenceDTs = []
        
        for self._word, self._part in self._theSentenceTokenized:
            if 'DT' in self._part:
                self._tempList = []
                self._stemWord = PorterStemmer().stem_word(self._word)
                self._tempList.append(self._stemWord)
                self._tempList.append(self._word)
                self._tempList.append(self._part)

                self._sentenceDTs.append(self._tempList)
                 
        return self._sentenceDTs        
    
    def getVerbs(self):
        """ RETURNS A LIST: [STEM, WORD, PART OF SPEECH] """
        
        self._sentenceVerbs = []
        
        for self._word, self._part in self._theSentenceTokenized:
            if 'VB' in self._part:
                self._tempList = []
                self._stemWord = PorterStemmer().stem_word(self._word)
                self._tempList.append(self._stemWord)
                self._tempList.append(self._word)
                self._tempList.append(self._part)

                self._sentenceVerbs.append(self._tempList)
                 
        return self._sentenceVerbs


    def posNgrams(self, n=2, pos='DT'):
        """ RETURNS A LIST OF TOUPLES AROUND THE POS """
        self._tempPOSNgram = []
        self._posNgram = []
        self._posNewList = []
        
        for i in range(len(self._theSentenceTokenized)-n+1):
            if self._theSentenceTokenized[i][1] == pos:
                self._tempPOSNgram.append(self._theSentenceTokenized[i-n:i+(n+1)])
        
        for self._posList in self._tempPOSNgram:
            for self._posTouple in self._posList:
                self._posNewList.append(self._posTouple[::-1])
            self._posNgram.append(self._posNewList)
                
        return self._posNgram