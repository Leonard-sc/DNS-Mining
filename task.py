import my_lib.data as dt
import my_lib.apriori as ap
import numpy as np
import pylab as pl
from apyori import apriori
import time

data = dt.Data("C:\\Users\\ShaneSun\\Desktop\\DNS-mining\\data")
data.read_all()
#计算用户的访问次数在这个时间区间内的数量及百分比
# user_count={}
# for key,value in data.record.items():
#     if key not in user_count:
#         user_count.setdefault(key,{})
#     for record in value:
#         hour = record.time.split(':')[0]
#         if hour not in user_count[key]:
#             user_count[key].setdefault(hour,{})
#             user_count[key][hour].setdefault(record.source_ip,1)
#             user_count[key][hour].setdefault('all_user', 1)
#         else:
#             if record.source_ip not in user_count[key][hour]:
#                 user_count[key][hour].setdefault(record.source_ip,1)
#             else:
#                 user_count[key][hour][record.source_ip] += 1
#             user_count[key][hour]['all_user'] += 1


# print(user_count)

# user_percent={}
# for day,vd in user_count.items():
#     if day not in user_percent:
#         user_percent.setdefault(day,{})
#     for hour,vh in vd.items():
#         if hour not in user_percent[day]:
#             user_percent[day].setdefault(hour,{})
#         for user,vu in vh.items():
#             if ((user not in user_percent[day][hour]) and (user!='all_user')):
#                 percent=str(round(vu/user_count[day][hour]['all_user']*100,5))+'%'
#                 user_percent[day][hour].setdefault(user,percent)
#
# print(user_percent)




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