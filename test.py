from my_lib import fpGrowth
from my_lib import data as dt
# rootNode = fpGrowth.treeNode('py',9,None)
# rootNode.children['eye'] = fpGrowth.treeNode('eye',13,None)
# rootNode.disp()
def loadSimpDat():
    data = dt.Data("./data")
    data.read_all()
    simpDat=data.dns_trans
    # simpDat = [
    #     ['I1', 'I2', 'I5'],
    #     ['I2', 'I4'],
    #     ['I2', 'I3'],
    #     ['I1', 'I3'],
    #     ['I2', 'I3'],
    #     ['I1', 'I3'],
    #     ['I1', 'I2', 'I3'],
    #     ['I1', 'I2', 'I5'],
    #     ['I2', 'I4'],
    #     ['I2', 'I3'],
    #     ['I1', 'I2', 'I4'],
    #     ['I1', 'I3'],
    #     ['I2', 'I3'],
    #     ['I1', 'I3'],
    #     ['I1', 'I2', 'I3', 'I5'],
    # ]
    #print(simpDat)
    return simpDat

def createInitset(dataset):
    retDict = {}
    for trans in dataset:
        if(frozenset(trans) in retDict):
            retDict[frozenset(trans)] = retDict[frozenset(trans)] + 1
        else:
            retDict[frozenset(trans)] = 1
    return retDict

simpDat = loadSimpDat()
initset = createInitset(simpDat)


myFPtree,myHeaderTable = fpGrowth.createTree(initset, 10000)
#myFPtree.disp()

#定义频繁集进行接收
freqItems=[]

fpGrowth.mineTree(myFPtree,myHeaderTable, 10000, set([]),freqItems)
file = open('freqItems.txt','w')
for i in freqItems:
    file.write(str(i)+'\n')
    #print(str(i))
file.close()
# print(freqItems)