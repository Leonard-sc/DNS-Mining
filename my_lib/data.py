import os

class Data(object):
    """ Class for dns data
    Attributes:
        self.file_list: list of file name.
        self.file_path: list of file's path.
        self.record: dict like {file_name : dns record list[]}
    Author: sun
    """
    def __init__(self,dir_path):
        """Init class,generate path for every file."""
        self.file_list = os.listdir(dir_path)
        self.file_path = [os.path.join(dir_path,x) for x in self.file_list]  # file name and dir path join to fully path
        self.record = {}
        self.dns_item = {}  # dict like {ip:count} ready for construct fp-tree
        self.dns_trans = []
        self.record_num = 0  # count record number

    def read_all(self):
        """read all dns record from every file."""
        for index,file_path in enumerate(self.file_path):
            # if (index==1):
            #     break
            file_name=self.file_list[index]
            self.record[file_name] = []
            with open(file_path,'r') as file:
                for line in file.readlines():
                    time = ''
                    source_ip = ''
                    des_site = ''
                    dns_ip = []
                    for index,value in enumerate(line.split('|')):
                        if(index == 0):
                            time=value
                        elif(index==1):
                            source_ip=value
                        elif(index==2):
                            des_site=value
                        elif(value!='\n'):
                            dns_ip.append(value)
                            if(value in self.dns_item):
                                self.dns_item[value]+=1
                            else:
                                self.dns_item.setdefault(value,1)
                    self.record[file_name].append(DataRecord(time,source_ip,des_site,dns_ip))
                    self.dns_trans.append(dns_ip)
                    self.record_num=self.record_num+1



class DataRecord(object):
    """Class for each of dns record,save the dns info
    Attribute:
        self.time: dns log time
        self.source_ip: user's ip
        self.des_site: user's destination site
        self.dns_ip: list of every dns server's ip in the way of search
    Author: sun
    """
    def __init__(self,time,source_ip,des_site,dns_ip):
        self.time=time
        self.source_ip=source_ip
        self.des_site=des_site
        self.dns_ip=dns_ip


"""example
data = Data("C:\\Users\\ShaneSun\\Desktop\\DNS-mining\\data")
data.read_all()
print(data.record['CSession_01'][0].time)
print(data.record['CSession_01'][0].source_ip)
print(data.record['CSession_01'][0].des_site)
print(data.record['CSession_01'][0].dns_ip)
"""

