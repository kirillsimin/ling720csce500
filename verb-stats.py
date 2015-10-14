import sys
import re
import csv

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer


from collections import defaultdict

import essayclasses

exportedDB = 'data/all-essays.csv'
studentData = 'data/students with countries - existing.txt'


allEssays = AllEssaysFile(exportedDB)