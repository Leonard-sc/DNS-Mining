import my_lib.data as dt
import numpy as np
import time
import matplotlib.pyplot as pl
import  matplotlib.font_manager
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
msyh = matplotlib.font_manager.FontProperties(fname='C:\\Windows\\Fonts\\msyh.ttc')
data = dt.Data("C:\\Users\\ShaneSun\\Desktop\\DNS-mining\\data")
data.read_all()

#ip行为特征 ip:[总请求次数，查询域名数量，重复针对同一个域名的请求个数（最大、最小、平均、方差），请求重复发送的间隔时间（最大、最小、平均、方差）]
ip_feature={} #key为用户ip，value为以上特征
ip_search_list={}
ip_time_list={}
for key,value in data.record.items():
    for record in value:
        site = record.des_site.split('.')
        if len(site)>=3:
            if(len(site)>=4):
                site = record.des_site[site.index(site[-4:][0]):]
            else:
                site = record.des_site[site.index(site[-3:][0]):]
            if record.source_ip not in ip_feature:
                ip_feature.setdefault(record.source_ip,[0,0,0,0,0,0,0,0,0,0])
            if record.source_ip not in ip_search_list:
                ip_search_list.setdefault(record.source_ip,{})
            if record.des_site not in ip_search_list[record.source_ip]:
                ip_search_list[record.source_ip].setdefault(site, 0)
            if record.source_ip not in ip_time_list:
                ip_time_list.setdefault(record.source_ip,[])
            ip_feature[record.source_ip][0]+=1 #总发送请求次数
            ip_search_list[record.source_ip][site]+=1 #记录对每个域名的请求次数
            new_time = time.strptime('2000:'+record.time.split('.')[:-1][0],'%Y:%H:%M:%S') #添加偏移2000将其变为可操作
            ip_time = time.mktime(new_time)+float('.'+record.time.split('.')[-1]) #将其转换为时间戳并加上原毫秒
            ip_time_list[record.source_ip].append(ip_time)#记录下该用户所有的请求时间





for ip in ip_feature: #用ip_search_list 中的数据刷新ipfeature
    # if(ip_feature[ip][1]==0):#特性2：查询域名数量
    ip_feature[ip][1]=len(list(ip_search_list[ip].keys()))
    # if(ip_feature[ip][2]==0):#特性3：对同一域名的请求个数
    site_list=[]#每个位置记录一个站点的请求数量
    for site in ip_search_list[ip]:
        site_list.append(ip_search_list[ip][site])
    ip_feature[ip][2]=max(site_list)#最大请求个数
    ip_feature[ip][3]=min(site_list)#最小请求个数
    ip_feature[ip][4]=np.mean(site_list)#均值
    ip_feature[ip][5]=np.var(site_list)#方差
    time_space_list=[]#记录请求时间间隔
    ip_time_list[ip].sort()
    for index,time in enumerate(ip_time_list[ip]):
        if(0==index):continue
        time_space_list.append(time - ip_time_list[ip][index-1])
    if len(time_space_list)!=0:
        ip_feature[ip][6] = max(time_space_list)
        ip_feature[ip][7] = min(time_space_list)
        ip_feature[ip][8] = np.mean(time_space_list)
        ip_feature[ip][9] = np.var(time_space_list)

# print(ip_feature)
# print(len(ip_feature.values()))
#
m=np.matrix(list(ip_feature.values()))
print(m.shape)

# #我们计算K值从1到10对应的平均畸变程度：
# #用scipy求解距离
# K=range(1,10)
# meandistortions=[]
# for k in K:
#     kmeans=KMeans(n_clusters=k)
#     kmeans.fit(m)
#     meandistortions.append(sum(np.min(
#             cdist(m,kmeans.cluster_centers_,
#                  'euclidean'),axis=1))/m.shape[0])
# pl.plot(K,meandistortions,'bx-')
# pl.xlabel('k')
# pl.ylabel(u"平均畸变程度",fontproperties=msyh)
# pl.title('确定最佳的K值',fontproperties=msyh)
# pl.show()

num_clusters = 4
clf = KMeans(n_clusters=num_clusters,  n_init=1, verbose=1)
clf.fit(m)
# print(clf.labels_)
# # print(len(clf.labels_))
print(clf.cluster_centers_)
final_table=[0,0,0,0]#四类的统计数据：该类用户数量，上面的各种特征
for user_class in clf.labels_:
    final_table[user_class]+=1
print(final_table)#统计数量




