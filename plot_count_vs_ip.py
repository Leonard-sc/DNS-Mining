import my_lib.data as dt
import pylab as pl


data = dt.Data("C:\\Users\\ShaneSun\\Desktop\\DNS-mining\\data")
data.read_all()
each_count=list(data.dns_item.values())
each_count.sort(reverse=True)
each_count=each_count[2:]
pl.plot(range(int(len(each_count)*0.382)), each_count[0:int(len(each_count)*0.382)])
pl.title('Plot of count vs. each ip')
pl.xlabel('each ip')
pl.ylabel('count')
pl.show()
