# d={'a':1,'b':0,'c':1}
# keys = list(d.keys())
# for k in keys:
#     if d[k] == 0:
#         del(d[k])
#
# print(d)

seq = ('1', '2', '3')
seq1 = [0,1,2]

dict = {'a': 'hello', 'b': 'world', 'c': 'hello'}
dict = dict.fromkeys(seq)
print(dict)