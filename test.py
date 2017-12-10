from my_lib import fpGrowth
from my_lib import data as dt
# rootNode = fpGrowth.treeNode('py',9,None)
# rootNode.children['eye'] = fpGrowth.treeNode('eye',13,None)
# rootNode.disp()
data = dt.Data("./data")
data.read_all()
def loadSimpDat():
    # data = dt.Data("./data")
    # data.read_all()
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
print(freqItems)
freqItems_sup=[0]*len(freqItems)
for index,item in enumerate(freqItems):
    for file in data.record:
        for record in data.record[file]:
            l = len(item)
            flag=0
            for x in item:
                if x in record.dns_ip:
                    flag += 1
            if flag==l :
                freqItems_sup[index] += 1

file = open('freqItems.txt','w')
for index,i in enumerate(freqItems):
    file.write(str(i)+':'+str(round(freqItems_sup[index]/data.record_num*100,3))+'\n')
    #print(str(i))
file.close()
print(freqItems)