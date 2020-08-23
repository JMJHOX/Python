name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di=dict()
wdds=list()
for line in handle:
    wds=line.split()
    if line.startswith("From "):
        day=wds[1]
        #print(day)
        if day in di:
            di[day]=di[day]+1
           # print("old")
        else:
            di[day]=1
           # print("New")
print(di)
tmp=list()
for k,v in di.items():
    print(k,v)
    newt=(v,k)
    tmp.append(newt)
    tmp=sorted(tmp,reverse=True)
print(tmp[:5])