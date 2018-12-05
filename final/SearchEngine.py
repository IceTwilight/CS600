from Trie import Trie
from InvertFile import InvertFile
from bs4 import BeautifulSoup

import json

import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class SearchEngine():

    invertFile = InvertFile()

    #jsonFileName:websiteFile
    def createTrie(self):
        f = open('websiteFile.json', 'r')
        listIn = f.readlines()
        str = listIn[0]
        webDict = json.loads(str) #jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}' -- {u'a': 1, u'c': 3, u'b': 2, u'e': 5, u'd': 4}
##        print(webDict)
        f.close()
        stopKeys = list(set(stopwords.words('english')))
        #print(stopKeys)

        for website in webDict:
##            print(website)
            f = open(website, 'r', encoding='UTF-8')
            soup = BeautifulSoup(f.read(),features="html.parser")
            
            listWords  = word_tokenize(soup.get_text())
            for word in listWords:
                word = word.lower()
            filteredWords = [w for w in listWords if not w in stopKeys]
##            if 'you' in filteredWords:
##                print("yes")

            #print(filteredWords)

            for word in filteredWords:
                #len(word) to avoid useless key and to avoid a big result
                if len(word) >= 3:
                    #word = word.lower()
                    # print(word)
                    # print(webDict[website])
                    self.invertFile.insertNewKeyValue(word, webDict[website])

        f.close()

    def getRecommendKeyList(self, keyString):
        return self.invertFile.getRecommendKeyList(keyString)

    def getRecommendWebsite(self, keyString):
        recommendKeyList = self.getRecommendKeyList(keyString)
        #print(recommendKeyList)
        recommendWebsiteListDict = []
        for eachKey in recommendKeyList:
##            print(eachKey)
            if self.invertFile.getKeyAndValue(eachKey) != None:
##                print(self.invertFile.getKeyAndValue(keyString).loca)
                recommendWebsiteListDict.append(self.invertFile.getKeyAndValue(eachKey))

        return recommendWebsiteListDict
        
##se = SearchEngine()
##se.createTrie()
##print(se.getRecommendKeyList('value'))
##print(se.getRecommendWebsite('value'))
###print(list((se.invertFile.t)))

##circleI = 1
##se = SearchEngine()
##print("Initializing...")
##se.createTrie()
##print("Initialization complete!")
##while circleI:
##    keyString = input("Please enter your keyword to get recommendation! (The length of keyword should larger than 3)")
####    print(type(keyString))
##    if type(keyString) != str or len(keyString) < 3:
##        print("Please enter available keyword")
##        continue
##    print("The irrelevant key is in the follow list: \n")
##    print(se.getRecommendKeyList(keyString))
##    print('\n')
##    print("For every irrelevant key, the recommend websites are as follows: \n")
##    print(se.getRecommendWebsite(keyString))
##    print('\n')
##    print("The result will stored in \"output\" file in" + keyString + ".txt + \n")
##    outputAddress = "./output/" + keyString + ".txt"
##    writeResult = open(outputAddress, "w")
####    writeResult.writelines(se.getRecommendWebsite(keyString))
##    for recommendWebsite in se.getRecommendWebsite(keyString):
####        s = json.dumps(recommendWebsite)
##        s = str(recommendWebsite)
####        print(s)
##        writeResult.write( s + '\n')
##    writeResult.close()
##    circleI = int(input("Want to try another key? 1 for yes, 0 for no"))
##    if circleI != 1 and circleI !=0:
##        print("Wrong choice, the program will be ended")
##        circleI = 0
##    


















    
