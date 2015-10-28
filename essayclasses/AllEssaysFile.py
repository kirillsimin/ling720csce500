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



global exportedDB
exportedDB = 'data/all-essays.csv'
global studentData
studentData = 'data/students with countries - existing.txt'


class AllEssaysFile():
    
    def __init__(self,theFile):
    
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

   
    def getArabicEssays(self):
        """ RETURNS A LIST OF ARABIC SPEAKERS' ESSAY FULL INFO """
        
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
        
        

    
    def getNonArabicEssays(self):
        """ RETURNS A LIST OF NON-ARABIC SPEAKERS' ESSAY FULL INFO """
        
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
        
        

     
   
    def getArabicEssaysText(self):
        """ RETURNS A LIST OF ARABIC SPEAKERS' ESSAY TEXTS ONLY """
     
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
        
        

   
    def getNonArabicEssaysText(self):
        """ RETURNS A LIST OF ARABIC SPEAKERS' ESSAY TEXTS ONLY """
        
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

       
        
    
    def getAllTexts(self):
        """ RETURNS ONLY TEXTS OF ALL ESSAYS """
        essayTexts = []
        for self.row in self.essaysInfo:
            #print(self.row[2])
            self.theText = self.row[6]
            self.theText = self.theText.replace('\n', ' ')
            self.theText = re.sub(' +',' ',self.theText)
            self.theText = self.theText.replace('\t', ' ')
            
            essayTexts.append(self.theText)
        return essayTexts
