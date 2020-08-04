import re


fh = open('regex.txt')
for linea in fh:
    linea=linea.rstrip()
    if re.search('hola',linea):
        print(linea)