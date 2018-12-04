
class TreeNode():
    def __init__(self):
            
        self.children = {}
        self.hitNum = 0
        self.repeat = 0
        self.keyCharacter = ''
        self.refToList = None


class Trie:
    def __init__(self):
        self.root = TreeNode()
        self.insertList = []
        
    def insertNode(self, content, ref):
        if len(content) == 0:
            return
        else:
            self.insertList.append(content)
            currentNode = self.root
            for c in content:
                if c in currentNode.children:
                    currentNode.repeat += 1
                    currentNode = currentNode.children[c]
                else:
                    newNode = TreeNode()
                    newNode.keyCharacter = c
                    currentNode.children[c] = newNode
                    currentNode = currentNode.children[c]
            if currentNode.refToList == None:
                currentNode.refToList = ref

##            currentNode = self.root
##            repeatIndex = 0
##            for index in range(len(content)):
##                if currentNode.children[content[index]].repeat > 0:
##                    currentNode = currentNode.children[content[index]]
##                    repeatIndex = index
##            childNode = currentNode.children[content[repeatIndex+1]]
##            s = ''
##            refN = ''
##            while currentNode.children[content[repeatIndex+1]]:
##                s += currentNode.children[content[repeatIndex+1]].keyCharacter
##                if currentNode.children[content[repeatIndex+1]].refToList:
##                    refN = currentNode.children[content[repeatIndex+1]].refToList
##                repeatIndex += 1
##                currentNode = currentNode.children[content[repeatIndex+1]]
##            childNode.keyCharacter = s
##            childNode.refToList = refN
##            childNode.repeat = 0
##            childNode.hitNum = 0
##            childNode.children = {}

            return
        
    def becomeCompressedTrie(self):
        if self.insertList == []:
            return
        else:
            currentNode = self.root
            subWord = ''
            refNew = None
            for word in self.insertList:
                for i,c in enumerate(word):
                    if c in currentNode.children and (currentNode.repeat > 0):
                        currentNode = currentNode.children[c]
                    elif c in currentNode.children and (currentNode.repeat == 0):
                        subWord = word[i:]
                        repeatNode = currentNode
                        while i < len(word):
                            repeatNode = repeatNode.children[word[i]]
                            if repeatNode.refToList != None:
                                refNew = repeatNode.refToList
                            i += 1
                        currentNode.keyCharacter = subWord
                        currentNode.refToList = refNew
                        currentNode.repeat = 0
                        currentNode.hitNum = 0
                        currentNode.children = {}
                    else:
                        continue
                            
    def getRefByKey(self, keyChar):
        if len(keyChar) == 0:
            return None
        else:
            currentNode = self.root
            count = 0
            for c in keyChar:
                if c in currentNode.children:
                    currentNode = currentNode.children[c]
                    count += 1
                    if count == len(keyChar):
                        currentNode.hitNum += 1
                        return currentNode.refToList
                else:
                    return None
              
        
    def dfsKeyList(self, root):
        if root.keyCharacter:
            current_letter = root.keyCharacter
        else: 
            current_letter = ''
        
        if root.children:
            #list
            keyList = []
            for cNode in root.children:              
                childKeyList = self.dfsKeyList(root.children[cNode])
                for keyC in childKeyList:
                    s = current_letter + keyC
                    keyList.append(s)
        else:
            return [current_letter]

        return keyList

    def getRecommendKeyList(self, string):
        currentNode = self.root
        matchIndex = 0
        for index in range(len(string)):
            if string[index] in currentNode.children:
                currentNode = currentNode.children[string[index]]
                matchIndex = index
            else:
                break
        childKeyList = self.dfsKeyList(currentNode)
##        print("111111111111")
##        print(childKeyList)
##        print(matchIndex)
##        print("111111111111")
        keylist = []
        if currentNode.refToList != None:
            keylist.append(string[:(matchIndex+1)])
            
        for keyC in childKeyList:
            s = string[:(matchIndex)] + keyC
            keylist.append(s)
        return keylist

##
##tries = Trie()
##tries.insertNode(content="abcd", ref="http://abcd.com")
##tries.insertNode(content="acde", ref="http://acde.com")
##tries.insertNode(content="bcde", ref="http://acde.com")
##tries.insertNode(content="acddecxec", ref="http://acde.com")
##tries.becomeCompressedTrie()
##print (tries.insertList)
##print (tries.getRefByKey('acd'))
##print (tries.dfsKeyList(root=tries.root))
##print (tries.getRecommendKeyList("acd"))
##print (tries.root.children['a'].children['b'].hitNum)
##print (list(tries.root.children))
##for eachKey in tries.getRecommendKeyList("acd"):
##    print(eachKey)
##    print(tries.getRefByKey(eachKey))
