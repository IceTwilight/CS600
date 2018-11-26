from Trie import Trie
from InvertFile import InvertFile
from bs4 import BeautifulSoup

import json
from nltk.corpus import stop_words
from nltk.tokenize import word_tokenize

class SearchEngine():
    invertFile = InvertFile()

    #jsonFileName:websiteFile
    def createTrie(self):
        f = open('websiteFile.json', 'r')
        webDict = json.loads(f.readlines()) #jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}' -- {u'a': 1, u'c': 3, u'b': 2, u'e': 5, u'd': 4}
        f.close()
        stopKeys = list(set(stopwords.words('english')))

        for website in webDict:
            f = open(website)
            soup = BeautifulSoup(f.read())
            
            listWords  =word_tokenize(soup.get_text())
            filteredWords = [w for w in listWords if not w in stopKeys]

            for word in filteredWords:
                if len(word) > 3:
                    word = word.lower()
                    self.invertFile.insertNewKeyValue(word, webDict[website])

        f.close()

    def getRecommendKeyList(self, keyString):
        return self.invertFile.getRecommendKeyList(keyString)

    def getRecommendWebsite(self, keyString):
        recommendKeyList = self.getRecommendKeyList(keyString)
        recommendWebsiteListDict = []
        for eachKey in recommendKeyList:
            if self.invertFile.getKeyAndValue(keyString) != None:
                recommendWebsiteDict.append(self.invertFile.getKeyAndValue(keyString))

        return recommendWebsiteListDict
        
    
