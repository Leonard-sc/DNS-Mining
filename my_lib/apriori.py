from my_lib import tree


class Apriori(object):
    def __init__(self,dns_item,dns_trans,support=0):
        self.dns_trans = dns_trans  # 所有条目[[abc] [cda] [azf]]
        self.dns_item = dns_item  # {ip:count , ip:count}
        self.table = {}  # the fp table like {ip:link}
        self.dns_order_list = sorted(dns_item.items(), key=lambda num:num[1], reverse=True)  # {(ip,count),(ip,count)}
        for trans in dns_trans:  # 筛选各个transaction使其内只包含大于最小支持度的项
            trans = list(filter(lambda x: self.dns_item[x] >= support, trans))
            trans.sort(key = lambda item:self.dns_item[item],reverse=True)  # 对dns_trans排序，使其各transaction内有序
        dns_trans = list(filter(lambda x: len(x) != 0, dns_trans))
        for order_item in self.dns_order_list:
            if(order_item[1]>=support):  # 如果大于最小支持度才加到表中
                self.table[order_item[0]]={{order_item[0]:order_item[1]},None}  # 生成表

        self.root = tree.Node()

    def fp_tree(self):
        for trans in self.dns_trans:
            for item,index in trans:
                if(index==0):
                    self.update(item,self.root)

    def update(self,item,node):
        if item in node.child_list:
            node.child_dict[item].increase(1)
        else:
            if(self.table[item][1]==None):
                self.table[item][1]=node
            else:
                next_node_link = self.table[item][1].node_link
                while(next_node_link!=None):
                    next_node_link = next_node_link.node_link
                next_node_link = node
            node.child_dicttree.Node(item,1,node)

class AprioriList(object):
    def __init__(self):
        pass
