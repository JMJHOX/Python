
fh = open('mbox-short.txt')
count=0
for line in fh:
    if line.startswith('From '):
        line=line.rstrip()
        wds=line.split()
        count+=1
        print(wds[1])
    if not line.startswith('From"'):continue

print("There were", count, "lines in the file with From as the first word")
