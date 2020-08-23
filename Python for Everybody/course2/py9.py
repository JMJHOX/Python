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
bigcount=None
bigword=None
for word,count in di.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
    
