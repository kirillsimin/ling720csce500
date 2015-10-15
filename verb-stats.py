exportedDB = 'data/all-essays.csv'
studentData = 'data/students with countries - existing.txt'

import sys



#from essayclasses.AllEssaysFile import AllEssaysFile
#from essayclasses.EssayText import EssayText
#from essayclasses.ASentence import ASentence

from essayclasses import AllEssaysFile



allEssays = AllEssaysFile(exportedDB)




 


   ###### COUNTS WORDS PER ESSAY, DTs IN SENTENCES, VERBS IN QUESTIONS


arabicEssaysText = allEssays.getArabicEssaysText()
nonArabicEssaysText = allEssays.getNonArabicEssaysText()



arabicWords = 0
nonArabicWords = 0

arabicQVerbs = 0
nonArabicQVerbs = 0

arabicDTs = 0
nonArabicDTs = 0

sys.exit()


# run through each Arabic Essay

for aText in arabicEssaysText:
    
    print('\nESSAY:\n')
        
    thisText = EssayText(aText)

    arabicWords += thisText.countWords()
    
    arabicDTs += thisText.countDTs()
    
    # extracts questions only, counts verbs
    questions = thisText.getQuestions()
    for question in questions:
        thisQuestion = ASentence(question)
        arabicQVerbs += thisQuestion.countVerbs()




# run through each Non-Arabic Essay

for aText in nonArabicEssaysText:
    
    print('\nESSAY:\n')
    
    thisText = EssayText(aText)

    nonArabicWords += thisText.countWords()
    
    nonArabicDTs += thisText.countDTs()
    
    
    # extracts questions only, counts verbs
    questions = thisText.getQuestions()
    for question in questions:
        thisQuestion = ASentence(question)
        nonArabicQVerbs += thisQuestion.countVerbs()






#==============================================================================
# ############## OUTPUT ###########
#==============================================================================


arabicQVerbFreq = arabicQVerbs / len(arabicEssaysText)
nonArabicQVerbFreq = nonArabicQVerbs / len(nonArabicEssaysText)

arabicWordsPerEssay = arabicWords / len(arabicEssaysText)
nonArabicWordsPerEssay = nonArabicWords / len(nonArabicEssaysText)

arabicDTsPerEssay = arabicDTs / len(arabicEssaysText)
nonArabicDTsPerEssay = nonArabicDTs / len(nonArabicEssaysText)

print('\n############## OUTPUT ###########\n')

print('{} arabic essays and {} non-arabic essays'.format(len(arabicEssaysText),len(nonArabicEssaysText)))
print()

print("ARABIC: {} words per essay.".format(arabicWordsPerEssay))
print("NON-ARABIC: {} words per essay.".format(nonArabicWordsPerEssay))

print()

print("ARABIC: {} verbs in questions per essay.".format(arabicQVerbFreq))
print("NON-ARABIC: {} verbs in questions per essay.".format(nonArabicQVerbFreq))
 
print()

print("ARABIC: {} determiners per essay.".format(arabicDTsPerEssay))
print("NON-ARABIC: {} determiners per essay.".format(nonArabicDTsPerEssay))

