# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:10:00 2015

@author: Kirill
"""

import sys
import os
from nltk.parse import stanford

from nltk.tag.stanford import StanfordPOSTagger

my_sentence = "Such errors can cause accidents to the lives and properties which also leading to big loss for the companies."

java_path = "C:/Program Files/Java/jre1.8.0_65/bin/java.exe"

os.environ['JAVAHOME'] = java_path

os.environ['STANFORD_PARSER'] = \
'C:/stanford_data/stanford-parser.jar'

os.environ['STANFORD_MODELS'] = \
'C:/stanford_data/stanford-parser-3.5.2-models.jar'

parser = stanford.StanfordParser(model_path= \
"C:/stanford_data/englishPCFG.ser.gz")


parsed_sentences = parser.raw_parse( \
(my_sentence))

for i in parsed_sentences:
    for k in i:
        print(k)

#==============================================================================
# # GUI
# for line in parsed_sentences:
#     for sentence in line:
#         sentence.draw()
#==============================================================================


st = StanfordPOSTagger(r'C:/stanford_data/english-bidirectional-distsim.tagger',r'C:/stanford_data/stanford-postagger.jar')

bobo = st.tag(my_sentence.split())

print(bobo)

for i in bobo:
    print(i)
    
