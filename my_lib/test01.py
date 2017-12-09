d={'a':1,'b':0,'c':1}
keys = list(d.keys())
for k in keys:
    if d[k] == 0:
        del(d[k])

print(d)