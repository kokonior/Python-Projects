import re

strs = open("file.txt", "r") # file list
com = []
net = []
org = []
other = []

for x in strs.readlines():
    rz = re.search('((\w+))$', x.strip()).group(1)
    if rz == "com":
        com.append(x.strip())
    elif rz == "net":
        net.append(x.strip())
    elif rz == "org":
        org.append(x.strip())
    else:
        other.append(x.strip())

print("# Total Domains : {} \n\t.COM : {} \n\t.NET : {} \n\t.ORG : {}\n\tOTHERS : {}".format(len(org) + len(net) + len(com) + len(other), len(com), len(net), len(org), len(other)))