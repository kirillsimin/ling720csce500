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




import re
import csv

from essayclasses.anessay import AnEssay


exportedDB = 'data/all-essays.csv'
studentData = 'data/students with countries - existing.txt'


class AllEssaysFile():
    
    def __init__(self,theFile):
    
        self._csvfile = open(theFile, "r")
        self._readerAllEssaysInfo = csv.reader(self._csvfile, delimiter=',', quotechar='"')

        # list works better than csv.reader object
        self._essaysInfo = []
        for i in self._readerAllEssaysInfo:
            self._essaysInfo.append(i)
        
        ##
        ## allrow[2] is ID
        ## row[6] is the essay
        ##      
     
        #for self._row in self._essaysInfo:
        #    print(self._row[2])

    def essaysList(self):
        return self._essaysInfo
   
    def getArabicEssays(self):
        """ RETURNS A LIST OF ARABIC SPEAKERS' ESSAY FULL INFO """
        
        theEssays = []
        self._csvfile = open(studentData, "rU")
        self._readerStudentInfo = csv.reader(self._csvfile, delimiter='\t')
        
        # list works better than csv.reader object
        self._studentInfo = []
        for i in self._readerStudentInfo:
            self._studentInfo.append(i)

        # studentInfoIDs = studentInfo[0]
        ## row[3] is the country
        ##    


        for self._rowAllEssaysInfo in self._essaysInfo:
                
            for self._rowStudentInfo in self._studentInfo:
                
                if self._rowStudentInfo[0].replace('-','') == \
                self._rowAllEssaysInfo[2]:
                    
                    if self._rowStudentInfo[3] == 'Saudi Arabia' or\
                    self._rowStudentInfo[3] == 'Oman' or\
                    self._rowStudentInfo[3] == 'Iraq':
                    
                        self._curEssay = self._rowAllEssaysInfo
                        
                        theEssays.append(self._curEssay)
                        break

        return theEssays
        
        

    
    def getNonArabicEssays(self):
        """ RETURNS A LIST OF NON-ARABIC SPEAKERS' ESSAY FULL INFO """
        
        theEssays = []
        self._csvfile = open(studentData, "rU")
        self._readerStudentInfo = csv.reader(self._csvfile, delimiter='\t')
    
        # list works better than csv.reader object
        self._studentInfo = []
        for i in self._readerStudentInfo:
            self._studentInfo.append(i)
    
        # studentInfoIDs = studentInfo[0]
        ## row[3] is the country
        ##    
    
    
        for self._rowAllEssaysInfo in self._essaysInfo:
                
            for self._rowStudentInfo in self._studentInfo:
                
                if self._rowStudentInfo[0].replace('-','') == \
                self._rowAllEssaysInfo[2]:
                    
                    if self._rowStudentInfo[3] != 'Saudi Arabia' and\
                    self._rowStudentInfo[3] != 'Oman' and\
                    self._rowStudentInfo[3] != 'Iraq':
                    
                        self._curEssay = self._rowAllEssaysInfo
                        
                        theEssays.append(self._curEssay)
                        break
    
        return theEssays
        
        

     
   
    def getArabicEssaysText(self):
        """ RETURNS A LIST OF ARABIC SPEAKERS' ESSAY TEXTS ONLY """
     
        theEssays = []
        self._csvfile = open(studentData, "rU")
        self._readerStudentInfo = csv.reader(self._csvfile, delimiter='\t')

        # list works better than csv.reader object
        self._studentInfo = []
        for i in self._readerStudentInfo:
            self._studentInfo.append(i)

        # studentInfoIDs = studentInfo[0]
        ## row[3] is the country
        ##    


        for self._rowAllEssaysInfo in self._essaysInfo:
                
            for self._rowStudentInfo in self._studentInfo:
                
                if self._rowStudentInfo[0].replace('-','') == \
                self._rowAllEssaysInfo[2]:
                    
                    if self._rowStudentInfo[3] == 'Saudi Arabia' or\
                    self._rowStudentInfo[3] == 'Oman' or\
                    self._rowStudentInfo[3] == 'Iraq':
                    
                        self._theText = self._rowAllEssaysInfo[6]
                        self._theText = self._theText.replace('\n', ' ')
                        self._theText = re.sub(' +',' ',self._theText)
                        self._theText = self._theText.replace('\t', ' ')
                        
                        theEssays.append(self._theText)
                        break

        return theEssays
        
        

   
    def getNonArabicEssaysText(self):
        """ RETURNS A LIST OF ARABIC SPEAKERS' ESSAY TEXTS ONLY """
        
        theEssays = []
        self._csvfile = open(studentData, "r")
        self._readerStudentInfo = csv.reader(self._csvfile, delimiter='\t')

        # list works better than csv.reader object
        self._studentInfo = []
        for i in self._readerStudentInfo:
            self._studentInfo.append(i)

        # studentInfoIDs = studentInfo[0]
        ## row[3] is the country
        ##    


        for self._rowAllEssaysInfo in self._essaysInfo:
                
            for self._rowStudentInfo in self._studentInfo:
                
                if self._rowStudentInfo[0].replace('-','') == \
                self._rowAllEssaysInfo[2]:
                    
                    if self._rowStudentInfo[3] != 'Saudi Arabia' and\
                    self._rowStudentInfo[3] != 'Oman' and\
                    self._rowStudentInfo[3] != 'Iraq':
                    
                        self._theText = self._rowAllEssaysInfo[6]
                        self._theText = self._theText.replace('\n', ' ')
                        self._theText = re.sub(' +',' ',self._theText)
                        self._theText = self._theText.replace('\t', ' ')
                        
                        theEssays.append(self._theText)
                        break

        return theEssays

       
        
    
    def getAllTexts(self):
        """ RETURNS ONLY TEXTS OF ALL ESSAYS """
        essayTexts = []
        for self._row in self._essaysInfo:
            #print(self._row[2])
            self._theText = self._row[6]
            self._theText = self._theText.replace('\n', ' ')
            self._theText = re.sub(' +',' ',self._theText)
            self._theText = self._theText.replace('\t', ' ')
            
            essayTexts.append(self._theText)
        return essayTexts
