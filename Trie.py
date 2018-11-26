
class TreeNode():
    def __init__(self):
            
        self.children = {}
        self.hitNum = 0
        self.repeat = 0
        self.keyCharacter = ''
        self.refToList = None


class Trie
    def __init__(self):
        self.root = TreeNode()

    def insertNode(self, content, ref):
        if len(content) == 0:
            return
        else:
            currentNode = self.root
            for c in content:
                if c in currentNode.children:
                    currentNode.repeat++
                    currentNode = currentNode.children[c]
                else:
                    newNode = TreeNode()
                    newNode.keyCharacter = c
                    currentNode.children[c] = newNode
                    currentNode = currentNode.children[c]
            if currentNode.refToList = None:
                currentNode.refToList = ref

            currentNode = self.root
            repeatIndex = 0
            for index in range(len(content)):
                if currentNode.children[content[index]].repeat > 0:
                    currentNode = currentNode.children[content[index]]
                    repeatIndex = index
            childNode = currentNode.children[content[repeatIndex+1]]
            s = ''
            refN = ''
            while currentNode.children[content[repeatIndex+1]]:
                s += currentNode.children[content[repeatIndex+1]].keyCharacter
                if currentNode.children[content[repeatIndex+1]].refToList:
                    refN = currentNode.children[content[repeatIndex+1]].refToList
                repeatIndex++
                currentNode = currentNode.children[content[repeatIndex+1]]
            childNode.keyCharacter = s
            childNode.refToList = refN
            childNode.repeat = 0
            childNode.hitNum = 0
            childNode.children = {}

            return

    def getRefByKey(self, keyChar):
        if len(keyChar) == 0:
            return None
        else:
            currentNode = self.root
            count = 0
            for c in keyChar:
                if c in currentNode.children:
                    currentNode = currentNode.children[c]
                    count++
                    if count = len(keyChar):
                        currentNode.hitNum++
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
                childKeyList = self.dfs(root.children[cNode])
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
            if currentNode.children.has_key(string[index]):
                currentNode = currentNode.children[string[index]]
                matchIndex = index
            else:
                break
        childKeyList = self.dfsKeyList(currentNode)
        keylist = []
            
        for keyC in sub_keylist:
            s = string[:matchIndex] + keyC
            keylist.append(s)
        return keylist


# tries = Tries()
# tries.insert(word="abcd", ref="http://abcd.com")
# tries.insert(word="acde", ref="http://acde.com")
# tries.insert(word="bcde", ref="http://acde.com")
# tries.insert(word="acddecxec", ref="http://acde.com")
# print tries.dfs(root=tries.root)
# print tries.getRecommendKey("")
# print Tries.root.children['a'].children['b'].hit_num
# print Tries.root.children
        
        
