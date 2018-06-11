# This code runs on Processing3 in python mode.

import random
import math
import matplotlib.pyplot as plt
import numpy as np

N_list = [32000,8000,16000,64000,128000]
Avg = [64,64,128]
T = ['Square','Disk']


T1 = T[0]
N = N_list[1]
    
Location = []
Degree = [0]*N
RGG_L = [[] for i in range (N)]
#for square#
r = (Avg[0]/(N*math.pi))**0.5
R = (1400* r)
R2 = R**2
#for disk#
#r = (Avg[2]/float(N))**0.5
#R = (700* r)
#R2 = R**2
Min_index = []
Max_index = []
    
if T1 == 'Square':
    for i in range(N):
        x = random.uniform(0, 1400)
        y = random.uniform(0, 1400)
        Location.append([x,y])
        #strokeWeight(3)
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
        theata = random.uniform(0,2*math.pi)
        r2 = random.uniform(0, 490000)
        r1 = r2**0.5
        Location.append([700+(r1*cos(theata)),(700+r1*sin(theata))])
        #strokeWeight(3)
        #point(700+r1*cos(theata) ,700+r1*sin(theata))
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
'''
    for i in range(N):
        if Degree[i] == Min_Degree:
            Min_index.append(i)
                
    for i in Min_index:
        strokeWeight(20)
        stroke(255,0,0)
        point(Location[i][0],Location[i][1])
                
    for i in range(N):
        if Degree[i] == Max_Degree:
            Max_index.append(i)
                
    for i in Max_index:
        strokeWeight(20)
        stroke(0,0,255)
        point(Location[i][0],Location[i][1])
    
'''   
            
print('r is %.3f' %r)
print('avg_Deg is %.3f' %(sum(Degree)/float(N)))
print('Max_Deg is %.f' %Max_Degree )
print('Min.Degis %.f' %Min_Degree)
print('E is %.f' %(sum(Degree)/2) )
