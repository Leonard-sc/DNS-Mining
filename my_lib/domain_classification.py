import my_lib.data as dt
import fileinput

data = dt.Data("../data")
data.read_all()
# 用户浏览网站字典，key值为用户IP，value为其浏览的网站
user_log = {}
for SessionId in data.record:
    for trans in data.record[SessionId]:
        simp = trans.des_site.split(' ')[1]
        if trans.source_ip not in user_log:
            user_log.setdefault(trans.source_ip, [simp])
        else:
            user_log[trans.source_ip].append(simp)


user_list = [([0]*18) for i in range(5)]

# 选择的若干用户的IP地址集合
IP_List = [
            '159.226.15.11',
            '159.226.13.201',
            '192.168.13.229',
            '192.168.138.100',
            '159.226.13.182',
            ]

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
         for line in fileinput.input('domain_label.txt'):
            if site == line.split(':')[0]:
                user_list[index][int(line.split(':')[1].split('\n')[0])-1] += 1


for i in user_list:
    print(i)
