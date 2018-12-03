from Trie import Trie

#location: loca(number) -- decided in insertion -- insert in refToList
#key: key -- string
#occurList store {key, value- keyInDictInOccurList - website: 1 num}
class InvertFile():

    t = Trie()
    occurList = []

    def getKeyAndValue(self, keyString):
        loca = self.t.getRefByKey(keyString)
##        print (loca)
        if loca and loca > 0:
            return self.occurList[loca]
        else:
            return None

#every keyString has a dictonary to store all webs
    def insertNewKeyValue(self, keyString, keyInDictInOccurList):
        if (self.getKeyAndValue(keyString) == None):
            self.occurList.append({'keyString':keyString, keyInDictInOccurList: 1})
            loca = self.occurList.index({'keyString':keyString, keyInDictInOccurList: 1})
            self.t.insertNode(keyString, loca)
        else:
            subOccurList = self.getKeyAndValue(keyString)
            if keyInDictInOccurList in subOccurList.keys():
                subOccurList[keyInDictInOccurList] += 1
            else:
                subOccurList[keyInDictInOccurList] = 1
        return
    
    def getRecommendKeyList(self, keyString):
        return self.t.getRecommendKeyList(keyString)

    def getCompressedTrie(self):
        return self.t.becomeCompressedTrie()
    
##        
##I = InvertFile()
##I.insertNewKeyValue(keyString="abcd", keyInDictInOccurList="http://abcd.com")
##I.insertNewKeyValue(keyString="acde", keyInDictInOccurList="http://acde.com")
##I.insertNewKeyValue(keyString="bcde", keyInDictInOccurList="http://acde.com")
##I.insertNewKeyValue(keyString="acddecxec", keyInDictInOccurList="http://acde.com")
##I.getCompressedTrie()
##print (I.getKeyAndValue('acde'))
##print("111111111111")
##print (I.getRecommendKeyList("ab"))
##print("222222222222")
##print (I.occurList)
##print("333333333333")
##print (I.t)
##    
            

    
