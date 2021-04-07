#!/usr/bin/env python3

import os
import gmaps
import math

def euclidean_distance(koordinat1,koordinat2):
    return ((float(koordinat1[0])-float(koordinat2[0]))**2 + (float(koordinat1[1])-float(koordinat2[1]))**2 )**0.5

def do_a_star(node,nodeakhir,graf,node_arrived):
    node_arrived.append(graf[node]['koordinat'])
    if node == nodeakhir:
        return node_arrived
    else:
        newnode, node_arrived = next_node(node,nodeakhir,graf,node_arrived)
        if newnode == "null":
            return "null"
        return do_a_star(newnode,nodeakhir,graf,node_arrived)
    
def next_node(node,nodeakhir,graf,nodeterlewati):
    listtetangga = graf[node]["tetangga"]
#     minjarak = (euclidean_distance(graf[node]['koordinat'], graf[listtetangga[0]]['koordinat'])
#                 + euclidean_distance(graf[listtetangga[0]]['koordinat'],graf[nodeakhir]['koordinat'])) 
    minjarak = 999999999999.9
    mintetangga = "null"
    #     mintetangga = listtetangga[0]
    if nodeakhir in listtetangga:
        return nodeakhir,nodeterlewati
    else :
        for tetangga in listtetangga:
            if(graf[tetangga]['koordinat'] not in nodeterlewati):
                fx = euclidean_distance(graf[node]['koordinat'], graf[tetangga]['koordinat'])
                hx = fx + euclidean_distance(graf[tetangga]['koordinat'],graf[nodeakhir]['koordinat'])
                if (hx < minjarak):
                    minjarak = hx
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

def measure(lat1, lon1, lat2, lon2):  
    R = 6378.137 
    dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180
    dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180
    a = (math.sin(dLat/2) * math.sin(dLat/2) +
    math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) *
    math.sin(dLon/2) * math.sin(dLon/2))
    c = 2 * math.atan2((a)**0.5, (1-a)**0.5)
    d = R * c
    return d * 1000

def makemap(awal,akhir,graf):
    gmaps.configure(api_key='AIzaSyBlvE6HXrmuztPHa5sa6JIKXraPGrGlBcc')
    node_arrived = []
    path = (do_a_star(awal,akhir,Graf,node_arrived))
    if path == "null":
        return "Tidak ditemukan jalan"
    else:
        path = [ [float(x[0]),float(x[1])] for x in path ]
        distance = 0
        maps = gmaps.figure()
        for i in range(len(path)-1):
          distance = measure(path[i][0],path[i][1],path[i+1][0],path[i+1][1])
          input1 = (path[i][0], path[i][1])
          input2 = (path[i+1][0], path[i+1][1])
          temp = gmaps.directions_layer(input1, input2, show_markers=False, travel_mode="WALKING")
          maps.add_layer(temp)
        marker = []
        marker.append((path[0][0] , path[0][1]))
        marker.append((path[-1][0], path[-1][1]))
        mark = gmaps.marker_layer(marker)
        maps.add_layer(mark)
        return maps,distance