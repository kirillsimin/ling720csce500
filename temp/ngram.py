# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:40:43 2015

@author: Kirill
"""

def ngrams(input, n, pos):
  output = []
  for i in range(len(input)-n+1):
      if i == pos:
          output.append(input[i-n:i+(n+1)])
  return output

asd = list(range(0,100))

print(ngrams(asd, 2, 13))