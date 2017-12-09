import my_lib.data as dt
import my_lib.apriori as ap

data = dt.Data("C:\\Users\\ShaneSun\\Desktop\\DNS-mining\\data")
data.read_all()
apriori = ap.Apriori(data.dns_item,data.dns_trans)
# print(apriori.dns_trans)
apriori.fp_tree()
print(apriori.dns_trans)

print(data.dns_item)

print(data.dns_item['159.226.12.1'])
print(data.dns_item['60.28.11.236'])
print(data.dns_item['113.31.37.200'])
print(data.dns_item['221.204.186.9'])
