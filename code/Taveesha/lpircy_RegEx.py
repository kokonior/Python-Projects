#Open desired file and get list of all email id
#used in file, without repetition.
import re
y = list()
res = list()
ls = list()
fname= input('Enter Name of File:')
try:
    handle= open(fname)
except:
    print('Cant open file:', fname)
    quit()
for line in handle:
    y= re.findall('^From (\S+@\S+)', line)
    ls.append(y)
for i in ls:
    if i not in res:
        if not len(i)==0:
            res.append(i)
#print(ls)
print(res)
