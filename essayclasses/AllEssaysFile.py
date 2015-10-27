import sys
import re
import csv

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

from collections import defaultdict

class AllEssaysFile():
    
    
 
    
    def __init__(self,theFile):

        global exportedDB
        exportedDB = 'data/all-essays.csv'
        global studentData
        studentData = 'data/students with countries - existing.txt'
    
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
