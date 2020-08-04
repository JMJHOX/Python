name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di=dict()
wdds=list()
for line in handle:
    wds=line.split()
    #print(wds)
    if line.startswith("From "):
        #print(wds)
        day=wds[5]
        tmp=day.split(":")
        neww=tmp[0]
        #print(neww)
        if neww in di:
            di[neww]=di[neww]+1
           # print("old")
        else:
            di[neww]=1
           # print("New")
#print(di)
tmpp=list()
for k,v in di.items():
    #print(k,v)
    newt=(k,v)
    tmpp.append(newt)
    tmpp=sorted(tmpp)
#ntmp=tmp.split()
#print(ntmp)
for y,k in tmpp:
    print(y,k)
