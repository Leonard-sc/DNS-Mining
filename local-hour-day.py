import my_lib.data as dt
import pylab as pl

data = dt.Data("C:\\Users\\ShaneSun\\Desktop\\DNS-mining\\data")
data.read_all()
time_count={}
for key,value in data.record.items():
    for record in value:
        hour=record.time.split(':')[0]
        if('159.226.12.1' in record.dns_ip):
            if '159.226.12.1' not in time_count:
                time_count.setdefault('159.226.12.1',{})
                time_count['159.226.12.1'].setdefault(key, {})
                time_count['159.226.12.1'][key].setdefault(hour, 1)
            else:
                if(key not in time_count['159.226.12.1']):
                    time_count['159.226.12.1'].setdefault(key, {})
                    time_count['159.226.12.1'][key].setdefault(hour, 1)
                else:
                    if (hour not in time_count['159.226.12.1'][key]):
                        time_count['159.226.12.1'][key].setdefault(hour, 1)
                    else:
                        time_count['159.226.12.1'][key][hour]+=1
        if('159.226.12.2' in record.dns_ip):
            if '159.226.12.2' not in time_count:
                time_count.setdefault('159.226.12.2', {})
                time_count['159.226.12.2'].setdefault(key, {})
                time_count['159.226.12.2'][key].setdefault(hour, 1)
            else:
                if(key not in time_count['159.226.12.2']):
                    time_count['159.226.12.2'].setdefault(key, {})
                    time_count['159.226.12.2'][key].setdefault(hour, 1)
                else:
                    if (hour not in time_count['159.226.12.2'][key]):
                        time_count['159.226.12.2'][key].setdefault(hour, 1)
                    else:
                        time_count['159.226.12.2'][key][hour]+=1
# ```

# print(time_count)
# ```
plot_data=[]
i=0
for ip,ip_dict in time_count.items():
    for day,day_dict in ip_dict.items():
        plot_data.append([])
        plot_data.append([])
        for hour,num in sorted(day_dict.items(), key=lambda num:num[0]):
            plot_data[i].append(hour)
            plot_data[i+1].append(num)
        if(ip=='159.226.12.1'):
            plot_data.append('')
        else:
            plot_data.append('--')
        i+=3
# ```
print(plot_data[0:3])
print(len(plot_data))






label=['159.226.12.1_01','159.226.12.1_02','159.226.12.1_03','159.226.12.1_28','159.226.12.1_29','159.226.12.1_30','159.226.12.1_31','159.226.12.2_01','159.226.12.2_02','159.226.12.2_03','159.226.12.2_28','159.226.12.2_29','159.226.12.2_30','159.226.12.2_31']
i=0
for index,x in enumerate(plot_data):
    if(i%3==0):
        pl.plot(plot_data[index],plot_data[index+1],plot_data[index+2],label=label[int(i/3)])
    i+=1

pl.legend()
pl.show()

