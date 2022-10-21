
from typing import Counter
from letterMap import *



"""
hager wust yehonshewun enagerlahuegn 
    step -tokenize"
[hager] [wust] [yehonshewun] [enagerlahuegn]

[ha-ge-r]  -- Done

step -2 before this step check for letters combination in word map and replace them so the above step will keep on if the asci if only english letters
otherwise it means it might be some random symbol , emojis or probably the amharic letter which i repace it from word map
[ hagerua]
rua is found in word map ሯ --> so replace it
[hageሯ]
now the tokenization can contniue 
[ha - ge  - ሯ ]  , since the asci value is way beyon the english letters just skip anything rather than 65-91 98-122 A-Z a-z just append them

***** simpler solution since the after cons all the letter are val is handlen in tokenization so , just wait for till finish and do normal swapping
***** SKIP step 2

step 3 :
 check the list of words inside that found in 2d array and 
    if length  == 1 just replace if from word map
        length == 2 get the second one and repalce it with appropriate amaharic letter by calculating its ascii value
        lenght < 3 search for it in word map and replace it if the word is meaningless then replace anyhting u can get and left the others as they are
        if 0 skip 

        by merging them make finally one stting text holder fot return



"""
consonants = [x.upper() for x in consonants]

sentence = "huagerien wust yehonshewun enageralehuegn ".upper() .strip()
sentence = "Mekdimye dewyele..t... Mata edewllshalehu blual".upper() .strip()
# sentence = "Gena ke betegnkrstian ahun yetemelcheskut... Edewlletalehugna tsfalhuegn".upper() .strip()
sentence = "bmn awkie blesh new gin endeza aymslem qenm matam ymil nger ymeslegnal kefeleksh lgemtlsh ቀንም ማታም ነው ምትጋደሚው  kezhi tenesto kehone bozenie milew betam reasonable new malet new".upper().strip()

def lengthChecker(listofwords):
    letterHolder = ""
    for letter in listofwords:
        if len(letter) > 1:
            for insideletter in letter:
                letterHolder += insideletter
        else:
            letterHolder += letter
    return len(letterHolder)-1



def doubleLetterExtractor(sentences):
    
    for doubles in doubleLetters.keys():
        
        counter = 0
        if sentences.__contains__(doubles):
            while counter <= len(lettersNumbersVOWELS)-1:
                fullDouble = doubles +lettersNumbersVOWELS[counter]
                if counter == 5:
                    counter += 1
                    continue
                
                
                if sentences.__contains__(fullDouble):
                    
                    sentences = sentences.replace(fullDouble, chr(ord(doubleLetters.get(doubles))+counter))

                counter += 1
            
            fullDouble =  doubles +lettersNumbersVOWELS[5]
            if sentences.__contains__(fullDouble):
                    sentences = sentences.replace(fullDouble, chr(ord(doubleLetters.get(doubles))+5))

    return sentences
    



def word_toknizer(sentences):
    words = sentence.split(" ")

    sepwords = []
    mainWordsHolder = []

    for word in words:
        counter = 0
        lengthofword = len(word)-1

        temp = ""

        while counter <= lengthofword:
            letter = word[counter]
            
            if letter in consonants:

                try:
                    # cons-cons
                    if (letter in consonants and word[counter + 1] in consonants):

                        if letter.isalpha():
                            temp += letter
                            sepwords.append(temp)
                        else:
                            sepwords.append(letter)

                        if lengthChecker(sepwords) == lengthofword:
                            mainWordsHolder .append(sepwords)
                            mainWordsHolder.append()
                            sepwords = []

                        temp = ""
                    else:  # cons-vowel
                        if letter in consonants:

                            if letter.isalpha():
                                temp += letter
                            else:
                                sepwords.append(letter)

                            counter += 1
                            while counter <= len(word):
                                letter = word[counter]

                                if letter not in consonants:
                                    
                                    if letter.isalpha():
                                        if ord(letter) > 122:
                                            sepwords.append(temp)
                                            temp = ""
                                            sepwords.append(letter)
                                            counter += 1
                                            continue
                                        temp += letter
                                    else:

                                        if len(temp) > 0:
                                        
                                           
                                            sepwords.append(temp)
                                            temp = ""
                                        sepwords.append(letter)

                                    counter += 1
                                else:
                                    
                                    counter -= 1
                                    if len(temp) > 0:
                                        sepwords.append(temp)

                                    if lengthChecker(sepwords) == lengthofword:
                                        mainWordsHolder .append(sepwords)
                                        sepwords = []
                                    temp = ""
                                    break

                except:

                    if letter in consonants:
                        
                        if letter.isalpha():
                            temp += letter
                        else:
                            sepwords.append(letter)

                    if len(temp) > 0:
                        sepwords.append(temp)
                    if lengthChecker(sepwords) == lengthofword:
                        mainWordsHolder .append(sepwords)
                        sepwords = []

                    temp = ""
            else:

                if letter.isalpha():
                    temp += letter
                else:
                    sepwords.append(letter)

                if len(temp) > 0:
                    sepwords.append(temp)
                if lengthChecker(sepwords) == lengthofword:
                    mainWordsHolder .append(sepwords)
                    sepwords = []

                temp = ""

            # print(counter)
            counter += 1

    return mainWordsHolder


def word_mapperFromDefinedVariables(tokenizedWord):
    wordHolder = ""
    tempLetterHolder = ""



    for mainWord in tokenizedWord:
        for word in mainWord:
            length = len(word)
            word = word.upper()
            
            if length > 0:

                if length == 1:
                    if word  in lettersList.keys():
                        tempLetterHolder += chr(ord(lettersList[word])+5)
                    elif word  in lettersNumbersVOWELS:
                        #4768
                        indexoflet = afam.index(word)
                        word = 4768 + indexoflet
                        tempLetterHolder += chr(word)
                        
                    else:
                        tempLetterHolder += word
                elif length == 2:

                    vowelletter = word[1]
                    consLetter = word[0]

                    if word in hafam.keys(): # ha hu hi

                       tempLetterHolder +=  hafam[word]

                    if vowelletter  in lettersNumbersVOWELS: # be - በ

                        indexofVal = lettersNumbersVOWELS.index(vowelletter)
                        consLetter = lettersList[consLetter] 
                
                        consLetter = chr(ord(consLetter)+ indexofVal)
                        tempLetterHolder += consLetter

                    elif word in lettersList.keys(): # gn, ch , ts 

                        tempLetterHolder += chr(ord(lettersList[word])+5)

                    else:
                       pass

                elif length == 3:
                    if word[-2:] == "IE":
                        tempLetterHolder  += chr(ord(word[0]) +4 )
                    if word in otherhualetters.keys():
                        tempLetterHolder += otherhualetters[word]  
                    elif word[0] == "H":

                        if word in huafam:
                            tempLetterHolder += huafam[word]
                        else:
                            tempLetterHolder += word

                    elif word[0] == "Q":

                        if word in quafAM:
                            tempLetterHolder += quafAM[word]
                        else:
                            tempLetterHolder += word
                        
                    elif word[0] == 'G':

                        if word in guafam:
                            tempLetterHolder += guafam[word]
                        else:
                            tempLetterHolder += word
                    else:
                        tempLetterHolder += word
                else:

                    flag = False
                    for quafAM_ in quafAM.keys():
                        if word.rfind(quafAM_) != -1:
                            startingIndex = word.rfind(quafAM_)
                            edingIndex = (len(quafAM_)-1) + startingIndex
                            word_ = word[startingIndex: edingIndex]
                            tempLetterHolder += quafAM[word_]
                            flag = True
                            break
                    
                    if not flag:
                        for huafam_ in huafam.keys():
                            if word.rfind(huafam_) != -1:
                                startingIndex = word.rfind(huafam_)
                                edingIndex = (len(huafam_)-1) + startingIndex
                                word_ = word[startingIndex: edingIndex]
                                tempLetterHolder += huafam[word_]
                                flag = True
                                break
                    if not flag:
                        for guafam_ in guafam.keys():
                            if word.rfind(guafam_) != -1:
                                startingIndex = word.rfind(guafam_)
                                edingIndex = (len(guafam_)-1) + startingIndex
                                word_ = word[startingIndex: edingIndex]
                                tempLetterHolder += guafam[word_]
                                flag = True
                                break

                    if not flag:
                        for otherhualetters_ in otherhualetters.keys():
                            if word.rfind(otherhualetters_) != -1:
                                startingIndex = word.rfind(otherhualetters_)
                                edingIndex = (len(otherhualetters_)-1) + startingIndex
                                word_ = word[startingIndex: edingIndex]
                                tempLetterHolder +=otherhualetters[word_]
                                flag = True
                                break

            else:
                tempLetterHolder += " "
        wordHolder += " "+tempLetterHolder 
        tempLetterHolder = ""  
    return wordHolder

sentence = doubleLetterExtractor(sentences=sentence)     
tokenizedWord = word_toknizer(sentences=sentence)


final_converted = word_mapperFromDefinedVariables(tokenizedWord)
print(final_converted)

