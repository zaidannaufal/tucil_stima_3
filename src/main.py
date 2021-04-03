#!/usr/bin/env python3

import os

def makeInput(text):
    temp = text.split("\n")
    jumlahNode = int(temp[0])
    koordinat = temp[1:jumlahNode+1]
    matriks = temp[jumlahNode+1:]
    toDict(koordinat,matriks)

def toDict(koordinat, matriks):
    temp = {"koordinat":[],"edge":[]}
    newdict = {}
    for i in range(len(koordinat)):
        temp2 = koordinat[i]
        newdict[temp2[0]] = temp
        newdict[temp2[0]]["koordinat"] = ((temp2[1:].replace(":(","")).replace(")","")).split(",")
        newdict[temp2[0]]["edge"] = makeedge(matriks[i]) 
        break
    print(newdict)
        # newdict[i[0]]["koordinat"] = i[:]
        # newdict[i[0]]["edge"] = matriks[i]

def makeedge(row):
    temp = []
    row = (row.strip("[]")).replace(",","")
    for i in range(len(row)):
        if row[i] == "1":
            temp.append(i+1)
    return temp

PATH = os.path.abspath(os.getcwd())
filename = "test1.txt"
test = os.path.join(PATH,"test",filename)
with open(test,"r") as f:
    text = f.read()
    f.close()
# makeInput(text)
print(makeedge("0,1,1,1,0"))
