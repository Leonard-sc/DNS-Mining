class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode
        self.children = {}

    def inc(self, numOccur):
        self.count += numOccur

    def disp(self, ind=1):
        print(' ' * ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind + 1)


def createTree(dataSet, minSup=1):  # 根据数据集创建FP-Tree
    headerTable = {}       # 用headerTable存储事务中的元素
    for trans in dataSet:  # 首先扫描数据库进行计数
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    keys = list(headerTable.keys())

    for k in keys:
        if headerTable[k] < minSup:
            del (headerTable[k])  # 将不满足最小支持度的元素删除

    freqItemSet = set(headerTable.keys())
    if len(freqItemSet) == 0: return None, None  # r若没有满足最小支持度的元素，返回none
    for k in headerTable:
        headerTable[k] = [headerTable[k], None]  # 格式化headerTable以便使用树节点
    retTree = treeNode('Null Set', 1, None)  # 建立树
    for tranSet, count in dataSet.items():  # 第二次遍历数据库
        localD = {}
        for item in tranSet:  # 对每个transaction进行排序
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)  # 通过插入元素来更新树
    return retTree, headerTable

def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:  # 检查元素是否已在某一分支上
        inTree.children[items[0]].inc(count)  # 计数加1
    else:  # 把元素添加到树上
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None:  # 更新headerTable
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:  # 对剩余的item调用updatetree()更新树
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)

def updateHeader (nodeToTest, targetNode):
    while (nodeToTest.nodeLink != None):
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode

def ascendTree(leafNode, prefixPath):  # 从叶子节点到根是递增顺序
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)

def findPrefixPath(basePat, treeNode):
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats

def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: p[0])]  # 对headerTable排序
    for basePat in bigL:
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet) # 追加到set
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])
        myCondTree, myHead = createTree(condPattBases, minSup)
        if myHead != None:  # 递归进行挖掘
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)
