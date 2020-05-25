"""
このファイルに解答コードを書いてください
"""
#!/usr/bin/env python
# coding: utf-8
f = open('./input.txt')
data = f.read()
dataList = data.split('\n')
m = int(dataList[len(dataList)-2])
dic= {}
output = []
for item in dataList[:-2]:
    splititem = item.split(':')
    dic[int(splititem[0])] = splititem[1]
dic = sorted(dic.items())
for system in dic:
    if m%system[0]==0:
        output.append(system[1])
if len(output)>0:
    print(''.join(output))
else:
    print(m)

