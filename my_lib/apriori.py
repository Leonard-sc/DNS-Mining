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
                self.table[order_item[0]]=[order_item[1],None]  # 生成表
        self.root = tree.Node()

    def fp_tree(self):
        for trans in self.dns_trans:
            self.update(trans,self.root)



    def update(self,trans,root):
        for index,item in enumerate(trans):
            # print(index)
            # print(item)
            node = root
            for i in range(index):
                node = node.child_dict[trans[i]]
                node.increase(1)
                # print("node-ip:",node.ip)
                # print("node-mem:",node)
            if item in node.child_dict:
                node.child_dict[trans[i]]
            else:
                add_node = tree.Node(item,1,node)
                # print(add_node.ip)
                node.child_dict.setdefault(item,add_node)
                # print(len(node.child_dict))
                print(node.ip)
                print(node)
                print(add_node.ip)
                print(add_node)
                if(self.table[item][1]==None):
                    self.table[item][1]=add_node
                else:
                    next_node_link = self.table[item][1].node_link
                    while(next_node_link!=None):
                        next_node_link = next_node_link.node_link
                    next_node_link = add_node

class AprioriList(object):
    def __init__(self):
        pass
