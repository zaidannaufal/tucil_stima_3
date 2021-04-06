#!/usr/bin/env python3
import os
import gmaps
def euclidean_distance(koordinat1,koordinat2):
    return ((float(koordinat1[0])-float(koordinat2[0]))**2 + (float(koordinat1[1])-float(koordinat2[1]))**2 )**0.5

def do_a_star(node,nodeakhir,graf,node_arrived):
    node_arrived.append(graf[node]['koordinat'])
    if node == nodeakhir:
        return node_arrived
    else:
        newnode, node_arrived = next_node(node,nodeakhir,graf,node_arrived)
        return do_a_star(newnode,nodeakhir,graf,node_arrived)
  

def next_node(node,nodeakhir,graf,nodeterlewati):
    listtetangga = graf[node]["tetangga"]
    minjarak = (euclidean_distance(graf[node]['koordinat'], graf[listtetangga[0]]['koordinat'])
                + euclidean_distance(graf[listtetangga[0]]['koordinat'],graf[nodeakhir]['koordinat'])) 
    mintetangga = listtetangga[0]
    if nodeakhir in listtetangga:
        return nodeakhir,nodeterlewati
    else :
        for tetangga in listtetangga:
            if(graf[tetangga]['koordinat'] not in node_arrived):
                newjarak = (euclidean_distance(graf[node]['koordinat'], graf[tetangga]['koordinat'])
                            + euclidean_distance(graf[tetangga]['koordinat'],graf[nodeakhir]['koordinat']))
                if (newjarak < minjarak):
                    minjarak = newjarak
                    mintetangga = tetangga
        
        return mintetangga , nodeterlewati
   
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
    matriks = {koordinat[i*2]:{'tetangga' : matriks[i]} for i in range(0, len(matriks), 1)}
    return dicti, listnode


def makeedge(row,listnode):
    temp = []
    row = (row.strip("[]")).replace(",","")
    for i in range(len(row)):
        if row[i] == "1":
            temp.append(listnode[i])
    return temp

def makemap(awal,akhir,graf):
    gmaps.configure(api_key='AIzaSyBlvE6HXrmuztPHa5sa6JIKXraPGrGlBcc')
    node_arrived = []
    path = (do_a_star(awal,akhir,Graf,node_arrived))
    path = [ [float(x[0]),float(x[1])] for x in path ]

    maps = gmaps.figure()
    for i in range(len(path)-1):
      input1 = (path[i][0], path[i][1])
      input2 = (path[i+1][0], path[i+1][1])
      temp = gmaps.directions_layer(input1, input2, show_markers=False, travel_mode="WALKING")
      maps.add_layer(temp)
    marker = []
    marker.append((path[0][0] , path[0][1]))
    marker.append((path[-1][0], path[-1][1]))
    mark = gmaps.marker_layer(marker)
    maps.add_layer(mark)
    return maps    


if __name__ == "__main__":
    PATH = os.path.abspath(os.getcwd())
    filename = "buahbatu.txt"
    test = os.path.join(PATH,"..","test",filename)
    with open(test,"r") as f:
        text = f.read()
        f.close()
    Graf, listnode = todict(text)
    i = 1
    print("Berikut merupakan list node:")
    for node in listnode:
        print ("{}.{}".format(i,node))
        i+=1
    awal = int(input("Masukkan nomor node awal: "))
    tujuan = int(input("Masukkan nomor node tujuan: "))
    maps = makemap(listnode[awal-1],listnode[tujuan-1],Graf)