from Trie import Trie

#location: loca(number) -- decided in insertion -- insert in refToList
#key: key -- string
#occurList store {key, value- keyInDictInOccurList - website: 1 num}
class InvertFile():

    t = Trie()
    occurList = []

    def getKeyAndValue(self, keyString):
        loca = self.t.getRefByKey(keyString)
        if loca > 0:
            return self.occurList[loca]
        else:
            return None

#every keyString has a dictonary to store all webs
    def insertNewKeyValue(self, keyString, keyInDictInOccurList):
        if (self.get(keyString) == None):
            self.occurList.append({'keyString':key, keyInDictInOccurList: 1})
            loca = self.occurList.index({'keyString':key, keyInDictInOccurList: 1})
            self.t.insert(key, loca)
        else:
            subOccurList = self.get(keyString)
            if keyInDictInOccurList in subOccurList.keys():
                subOccurList[keyInDictInOccurList] += 1
            else:
                subOccurList[keyInDictInOccurList] = 1
        return
    
    def getRecommendKeyList(self, keyString):
        return self.t.getRecommendKeyList(keyString)
        

    
            

    
