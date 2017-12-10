import my_lib.data as dt
import pylab as pl

data = dt.Data("C:\\Users\\ShaneSun\\Desktop\\DNS-mining\\data")
data.read_all()
dns_order_list = sorted(data.dns_item.items(), key=lambda num:num[1], reverse=True)
plot_x = [dns_order_list[0][0],dns_order_list[1][0]]
plot_y = [dns_order_list[0][1],dns_order_list[1][1]]
pl.bar(plot_x, plot_y)
pl.show()