# This code runs on Processing3 in python mode.

import random
import math
import matplotlib.pyplot as plt
import numpy as np

N_list = [1000,8000,16000,64000,128000]
Avg = [32,64,128]
T = ['Square','Disk']

    
def setup():
    size(1400,1400)
    T1 = T[0]
    N = N_list[4]
    
    Location = []
    Degree = [0]*N
    RGG_L = [[] for i in range (N)]
    #for square#
    r = (Avg[2]/(N*PI))**0.5
    R = (1400* r)
    R2 = R**2
    # #for disk#
    # r = (Avg[2]/float(N))**0.5
    # R = (700* r)
    # R2 = R**2
    Min_index = []
    Max_index = []
    
    if T1 == 'Square':
        for i in range(N):
            x = random.uniform(0, 1400)
            y = random.uniform(0, 1400)
            Location.append([x,y])
            #strokeWeight(1)
            #point(x ,y)
            
            Location = sorted(Location,key=lambda k:k[0])
      #sweep method#          
        for i in range(N):     
            for j in range(i+1,N):
                if Location[j][0] - Location[i][0] <= R:
                    if ((Location[i][0] - Location[j][0])**2 +(Location[i][1] - Location[j][1])**2  ) <= R2:
                        #line(Location[i][0],Location[i][1],Location[j][0],Location[j][1])
                        RGG_L[i].append(j)
                        RGG_L[j].append(i)
                        Degree[i] +=1
                        Degree[j] +=1
                else: break
            
    if T1 == 'Disk':
        ellipse(700,700,1400,1400)
        for i in range(N):
            theata = random.uniform(0,2*PI)
            r2 = random.uniform(0, 490000)
            r1 = r2**0.5
            Location.append([700+(r1*cos(theata)),(700+r1*sin(theata))])
            # strokeWeight(3)
            # point(700+r1*cos(theata) ,700+r1*sin(theata))
            Location = sorted(Location,key=lambda k:k[0])
        
        #sweep method#     
        for i in range(N):     
            for j in range(i+1,N):
                if Location[j][0] - Location[i][0] <= R:
                    if ((Location[i][0] - Location[j][0])**2 +(Location[i][1] - Location[j][1])**2  ) <= R2:
                        #line(Location[i][0],Location[i][1],Location[j][0],Location[j][1])
                        RGG_L[i].append(j)
                        RGG_L[j].append(i)
                        Degree[i] +=1
                        Degree[j] +=1
                else: break
                    
    #find the vertices which has the max and min Degree#    
    
    Min_Degree = min(Degree)
    Max_Degree = max(Degree)
    
    # for i in range(N):
    #     if Degree[i] == Min_Degree:
    #         Min_index.append(i)
                
    # for i in Min_index:
    #     strokeWeight(20)
    #     stroke(255,0,0)
    #     point(Location[i][0],Location[i][1])
                
    # for i in range(N):
    #     if Degree[i] == Max_Degree:
    #         Max_index.append(i)
                
    # for i in Max_index:
    #     strokeWeight(20)
    #     stroke(0,0,255)
    #     point(Location[i][0],Location[i][1])
    
    
    RGG = [row[:] for row in RGG_L]

    #part 2  coloring
    Degree_List = [[] for i in range(Max_Degree+1)]
    for i in range(N):
        Degree_List[Degree[i]].append(i)
        
    #smallest - last - ordering
    SLO = []
    #create Degree_when_deleted List
    Degree_when_deleted = Degree[:]
    i = 0
    while i < len(Degree_List)-1:
        # try to find the vertex with min Degree
        if Degree_List[i]:
        #add the vertex into SLO List
            SLO.insert(0,[])
            SLO[0].append(Degree_List[i][0])
            #find vertices near the current vertex with min Degree
            for j in RGG_L[Degree_List[i][0]]:
            #for each vertex nearby,update related data
                SLO[0].append(j)
                Degree_List[Degree_when_deleted[j]-1].append(j)
                Degree_List[Degree_when_deleted[j]].remove(j)
                RGG_L[j].remove(Degree_List[i][0])
                Degree_when_deleted[j]-=1
            del Degree_List[i][0]
        #check the Degree in front of the current min Degree
        #since some vertices' Degree may drop 1 when deleting
            i = i-2

        i+=1
        if i < 0:
            i = 0

            
    #create color set,for example 1:[1,2,3] means vertex1,2,3 are color 1
    color_set = {1:[]}

    #for each list in SLO,we only need to color the first vertex,
    #make sure the color not the same with the other vertex in the list
    for i in SLO:
    #start from color 1
        current_color = 1

        #check set means the vertices we need to check(from secend to the end)
        check_set = set(i[1:])
        #for each current color,we need to check the color set,
        #if there is vertex both in check set and color set means this color is occupied,
        #so we need to try another color and check again.
        while set(color_set[current_color]) & check_set:
            current_color +=1 
        
            if current_color not in color_set:
                color_set[current_color] = []
    
        color_set[current_color].append(i[0])
    

        
    #part3
    
    new_RGG = {}
    SizeE = 0
    for i in color_set[1]:
        new_RGG[i] = []
        for j in RGG[i]:
            if j in color_set[2]:
                new_RGG[i].append(j)
                if j not in new_RGG.keys():
                    new_RGG[j] = []
                new_RGG[j].append(i)
                
                
    
    #deleting the tail
    check = 1
    while check:
        check = 0
        for k in new_RGG.keys():
            if len(new_RGG[k]) == 1:
                new_RGG[new_RGG[k][0]].remove(k)
                del new_RGG[k][0]     
                check = 1
            
        if check == 1:
            continue
     
    #dfs
    k = new_RGG.keys()[0]
    stack, path = [k], []
    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in new_RGG[vertex]:
            stack.append(neighbor)
    

                
    for i in new_RGG:
        if i in path:
            if new_RGG[i]:
                strokeWeight(5)
                stroke(0,0,255)
                point(Location[i][0] ,Location[i][1])
                for j in new_RGG[i]:
                    strokeWeight(5)
                    stroke(255,0,0)
                    point(Location[j][0] ,Location[j][1]) 
                    strokeWeight(1)
                    stroke(0,0,0)
                    line(Location[i][0],Location[i][1],Location[j][0],Location[j][1]) 
                
                    SizeE +=1
              
    
    #calculate dominations
    num = set()
    for i in path:
        num = num.union(set(RGG[i]))
    domination = len(num)/float(N)

  

    print(domination)
    print(SizeE)
    print(len(path))
