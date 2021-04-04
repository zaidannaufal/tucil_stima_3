#!/usr/bin/env python3

import os
def euclidean_distance(koordinat1,koordinat2):
    return ( (int(koordinat1[0])-int(koordinat2[0]))**2 + (int(koordinat1[1])-int(koordinat2[1]))**2 )**0.5

def do_a_star(node,nodeakhir,graf):
    if node == nodeakhir:
        return nodeakhir
    else:
        return "{} -> {}".format(node,do_a_star(next_node(node,nodeakhir,graf),nodeakhir,graf))

def next_node(node,nodeakhir,graf):
    listtetangga = graf[node]["tetangga"]
    minjarak = (euclidean_distance(graf[node]['koordinat'], graf[listtetangga[0]]['koordinat'])
                + euclidean_distance(graf[listtetangga[0]]['koordinat'],graf[nodeakhir]['koordinat'])) 
    mintetangga = listtetangga[0]
    for tetangga in listtetangga:
        newjarak = (euclidean_distance(graf[node]['koordinat'], graf[tetangga]['koordinat'])
                    + euclidean_distance(graf[tetangga]['koordinat'],graf[nodeakhir]['koordinat']))
        if (newjarak < minjarak):
            minjarak = newjarak
            mintetangga = tetangga
    return mintetangga

# jgn gini sorry 
# def mergeDict(dict1, dict2):
#    ''' Merge dictionaries and keep values of common keys in list'''
#    dict3 = {**dict1, **dict2}
#    for key, value in dict3.items():
#        if key in dict1 and key in dict2:
#                dict3[key] = [value , dict1[key]]
#    return dict3
   
def todict(text):
    temp = text.split("\n")
    koordinat =[]
    jumlahnode = int(temp[0])
    for i in range(jumlahnode):
        koordinat += (temp[i+1].split(':'))
    
    for i in range(len(koordinat)):
        if(i%2==1):
            koordinat[i]=koordinat[i].split(',')
    
    dicti = {koordinat[i]:{'koordinat' : koordinat[i + 1],'tetangga':[]} for i in range(0, len(koordinat), 2)}
    matriks = temp[jumlahnode+1:]
    listnode = koordinat[::2]
    
    for i in range(len(matriks)):
        dicti[listnode[i]]["tetangga"] = makeedge(matriks[i],listnode) 
    # matriks = {koordinat[i*2]:{'tetangga' : matriks[i]} for i in range(0, len(matriks), 1)}
    # dicti = mergeDict(dicti,matriks)
    return dicti, listnode


def makeedge(row,listnode):
    temp = []
    row = (row.strip("[]")).replace(",","")
    for i in range(len(row)):
        if row[i] == "1":
            temp.append(listnode[i])
    return temp


if __name__ == "__main__":
    PATH = os.path.abspath(os.getcwd())
    filename = "test1.txt"
    test = os.path.join(PATH,"test",filename)
    # test = "..\\test\\test1.txt"
    with open(test,"r") as f:
        text = f.read()
        f.close()
    Graf, listnode = todict(text)
    for key,value in Graf.items():
        print("{} {}".format(key,value))
    print(do_a_star("A","H",Graf))

