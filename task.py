import my_lib.data as dt
import my_lib.apriori as ap
import numpy as np
import pylab as pl
from apyori import apriori


data = dt.Data("C:\\Users\\ShaneSun\\Desktop\\DNS-mining\\data")
data.read_all()
results = list(apriori(data.dns_trans))
print(results)
# each_count=list(data.dns_item.values())
# each_count.sort(reverse=True)
# each_count=each_count[2:]
# print(each_count)
# # golden = each_count[0:int(len(each_count)*0.382)]
# pl.plot(range(int(len(each_count)*0.382)), each_count[0:int(len(each_count)*0.382)])
# pl.title('Plot of y vs. x')
# pl.xlabel('ip')
# pl.ylabel('count')
# pl.show()






# apriori = ap.Apriori(data.dns_item,data.dns_trans)
# print(apriori.dns_trans)
# apriori.fp_tree()
# print(apriori.dns_trans)
# print(data.record_num)
# print(len(apriori.root.child_dict))
# print(apriori.dns_order_list)
#
# print(apriori.root)
# print(len(apriori.root.child_dict))
# print("159.226.12.2:")
# print("159.226.12.2-mem:",apriori.root.child_dict['159.226.12.2'])
# print("159.226.12.2-count:",apriori.root.child_dict['159.226.12.2'].count)
# print("159.226.12.2-parent:",apriori.root.child_dict['159.226.12.2'].parent)
# print("159.226.12.2-dict:",apriori.root.child_dict['159.226.12.2'].child_dict)
# print(len(apriori.root.child_dict['159.226.12.2'].child_dict))