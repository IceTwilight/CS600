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
        print(webDict)
        f.close()
        stopKeys = list(set(stopwords.words('english')))

        for website in webDict:
            print(website)
            f = open(website, 'r', encoding='UTF-8')
            soup = BeautifulSoup(f.read())
            
            listWords  = word_tokenize(soup.get_text())
            filteredWords = [w for w in listWords if not w in stopKeys]

            for word in filteredWords:
                #print(word)
                if len(word) > 2:
                    word = word.lower()
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
            if self.invertFile.getKeyAndValue(keyString) != None:
                #print(self.invertFile.getKeyAndValue(keyString))
                recommendWebsiteListDict.append(self.invertFile.getKeyAndValue(keyString))

        return recommendWebsiteListDict
        
se = SearchEngine()
se.createTrie()
print(se.getRecommendKeyList('value'))
print(se.getRecommendWebsite('value'))
#print(list((se.invertFile.t)))
