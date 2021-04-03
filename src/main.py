#!/usr/bin/env python3

import os
def mergeDict(dict1, dict2):
   ''' Merge dictionaries and keep values of common keys in list'''
   dict3 = {**dict1, **dict2}
   for key, value in dict3.items():
       if key in dict1 and key in dict2:
               dict3[key] = [value , dict1[key]]
   return dict3
   
def toDict(text):
    temp = text.split("\n")
    koordinat =[]
    jumlahNode = int(temp[0])
    for i in range(jumlahNode):
        koordinat += (temp[i+1].split(':'))

    for i in range(len(koordinat)):
        if(i%2==1):
            koordinat[i]=koordinat[i].split(',')

    dicti = {koordinat[i]:{'koordinat' : koordinat[i + 1]} for i in range(0, len(koordinat), 2)}
    matriks = temp[jumlahNode+1:]

    for i in range(len(matriks)):
        matriks[i] = makeedge(matriks[i])

    matriks = {koordinat[i*2]:{'tetangga' : matriks[i]} for i in range(0, len(matriks), 1)}
    dicti = mergeDict(dicti,matriks)
    for x, y in dicti.items():
        print(x, y) 


def makeedge(row):
    temp = []
    row = (row.strip("[]")).replace(",","")
    for i in range(len(row)):
        if row[i] == "1":
            temp.append(i+1)
    return temp

# PATH = os.path.abspath(os.getcwd())
# filename = "test1.txt"
# test = os.path.join(PATH,"test",filename)
test = "..\\test\\test1.txt"
with open(test,"r") as f:
    text = f.read()
    f.close()
toDict(text)
