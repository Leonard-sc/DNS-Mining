# from bs4 import BeautifulSoup
# import requests
import my_lib.data as dt
import fileinput

import numpy as np
import time
import matplotlib.pyplot as pl
import  matplotlib.font_manager
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
msyh = matplotlib.font_manager.FontProperties(fname='C:\\Windows\\Fonts\\msyh.ttc')


# def getHtmlText(url,code='UTF-8'):
#     r = requests.get(url,timeout=30)
#     r.raise_for_status()
#     r.encoding = code
#     return r.text
#
# def getUrl(lst,url):
#     html = getHtmlText(url)
#     soup = BeautifulSoup(html,'html.parser')
#     a = soup.find_all('a')
#     for i in a:
#         try:
#             href = i.attrs['href']
#             lst.append(href)
#         except:
#             continue
#
#
data = dt.Data("../data")
data.read_all()
# 用户浏览网站字典，key值为用户IP，value为其浏览的网站
user_log = {}
user_num = 0
for SessionId in data.record:
    for trans in data.record[SessionId]:
        simp = trans.des_site.split(' ')[1]
        if trans.source_ip not in user_log:
            user_log.setdefault(trans.source_ip, [simp])
            user_num+=1
        else:
            user_log[trans.source_ip].append(simp)


user_list = [([0]*18) for i in range(user_num)]

# 选择的若干用户的IP地址集合
# IP_List = [
#             '159.226.15.11',
#             '159.226.13.201',
#             '192.168.13.229',
#             '192.168.138.100',
# '159.226.13.182',
#             ]
IP_List = list(user_log.keys())
print(IP_List)
# 所有域名集合
domain_list = []
for i in IP_List:
     for site in user_log[i]:
         site = site.split('.')
         if len(site) >= 3:
             if (len(site) >= 4):
                 site = site[site.index(site[-4:][0]):]
             else:
                 site = site[site.index(site[-3:][0]):]
         else:
             continue
         site = ".".join(site)
         if site not in domain_list:
             domain_list.append(site)


# 标记域名类别
domain_label = {}
# 将域名文件保存到domain_label.txt文件中
# file = open('domain_label.txt', 'w')
# for item in domain_list:
#     print(item)
#     print('1:新闻')
#     print('2:交友')
#     print('3:游戏')
#     print('4:小说')
#     print('5:军事')
#     print('6:购物')
#     print('7:科技')
#     print('8:直播')
#     print('9:搜索')
#     print('10:经济')
#     print('11:教育')
#     print('12:其他')
#     print('13:解决方案')
#     print('14:视频')
#     print('15:音乐')
#     print('16:体育')
#     print('17:娱乐')
#     print('18:招聘')
#     type = input("选择域名类别？")  # 根据输入判断域名类别
#
#     domain_label[item] = type
#     file.write(item+':'+type+'\n')
#     file.flush()
# file.close()


# 将用户的浏览网站集合到domain_label.txt中进行匹配，属于哪一类网站则该类型计数加1
f={}
for line in fileinput.input('domain_label.txt'):
    if line.split(':')[0] not in f:
        f.setdefault(line.split(':')[0],int(line.split(':')[1].split('\n')[0]) - 1)

for index,i in enumerate(IP_List):
     for site in user_log[i]:
         site = site.split('.')
         if len(site) >= 3:
             if (len(site) >= 4):
                 site = site[site.index(site[-4:][0]):]
             else:
                 site = site[site.index(site[-3:][0]):]
         else:
             continue
         site = ".".join(site)
         for s,c in f.items():
            if site == s:
                user_list[index][c] += 1


for i in user_list:
    print(i)

user_list = np.matrix(user_list)

num_clusters = 6
clf = KMeans(n_clusters=num_clusters,  n_init=1, verbose=1)
clf.fit(user_list)
# print(clf.labels_)
# # print(len(clf.labels_))
print(clf.cluster_centers_)
final_table=[0,0,0,0,0,0]#四类的统计数据：该类用户数量，上面的各种特征
for user_class in clf.labels_:
    final_table[user_class]+=1
print(final_table)#统计数量

# # 我们计算K值从1到10对应的平均畸变程度：
# # 用scipy求解距离
# K = range(1, 10)
# meandistortions = []
# for k in K:
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit(user_list)
#     meandistortions.append(sum(np.min(
#         cdist(user_list, kmeans.cluster_centers_,
#                 'euclidean'), axis=1)) / user_list.shape[0])
# pl.plot(K, meandistortions, 'bx-')
# pl.xlabel('k')
# pl.ylabel(u"平均畸变程度", fontproperties=msyh)
# pl.title(u'确定最佳的K值', fontproperties=msyh)
# pl.show()

    # for site in user_log[IP_List[2]]:
#
#
#
#         print(site)
#         print('1:新闻')
#         print('2:交友')
#         print('3:游戏')
#         print('4:小说')
#         print('5:军事')
#         print('6:购物')
#         print('7:科技')
#         print('8:直播')
#         print('9:搜索')
#         print('10:经济生活')
#         print('11:教育')
#         print('12:其他')
#         print('13:直播')
#         print('9:搜索')
#         print('10:经济生活')
#         print('11:教育')
#         print('12:其他')
#         print('7:科技')
#         type = input("选择域名类别？")  # 根据输入判断域名类别
#         user_list[0][int(type)] += 1
#         f open()
#
#
#
# print(user_list[2])
#
#
# # 定义各类网站的字典，key为网站类型，value为其包含的网站
# websitelists = {}
# websitelists['news'] = []
# websitelists['social'] = []
# websitelists['game'] = []
# websitelists['novel'] = []
# websitelists['military'] = []
# websitelists['shopping'] = []
# websitelists['finance'] = []
# websitelists['tech'] = []
# websitelists['live'] = []
# websitelists['search'] = []
#
# newsurl = 'http://hao.360.cn/xinwenmeiti.html'
# socialurl = 'http://www.hao123.com/love'
# techurl = 'http://hao.360.cn/diannaowz.html'
# getUrl(websitelists['social'], socialurl)
# for i in websitelists['social']:
#     print(i)
#
# getUrl(websitelists['news'], newsurl)
# for i in websitelists['news']:
#     print(i)
#
# getUrl(websitelists['game'], gameurl)
# for i in websitelists['game']:
#     print(i)
#
# getUrl(websitelists['novel'], novelurl)
# for i in websitelists['novel']:
#     print(i)
#
# getUrl(websitelists['military'], militaryurl )
# for i in websitelists['military']:
#     print(i)
#
# getUrl(websitelists['shopping'], shopping)
# for i in websitelists['shopping']:
#     print(i)
#
# getUrl(websitelists['tech'], techurl)
# for i in websitelists['tech']:
#     print(i)
#
# getUrl(websitelists['live'], liveurl)
# for i in websitelists['live']:
#     print(i)
# # 测试
# websitelists['social'].append('cloud-q.duba.net.')
# cnt = 0
# for userid in user_log:
#     for websites in user_log[userid]:
#         for id in websitelists:
#             if websites in websitelists[id]:
#                 print(userid,id)
#                 cnt+=1
#
#
# print(cnt)

# site_dict={}
# for key,value in data.record.items():
#     for record in value:
#         site = record.des_site.split('.')
#         if(len(site)>3):
#             if site[-3] not in site_dict:
#                 site_dict.setdefault(site[-3],None)
#
# print(site_dict.keys())
