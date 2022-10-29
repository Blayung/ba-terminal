#!/bin/python3
from os import listdir
from time import time,sleep
from playsound import playsound
from threading import Thread

frames=[]
i=1
while True:
    if i==len(listdir('ascii')):
        break
    with open(f'ascii/{i}.txt','r') as file:
        frames.append(file.read())
    i+=1

Thread(target=playsound,args=('[HD] Touhou - Bad Apple!! [ＰＶ] (Shadow Art)-UkgK8eUdpAo.mp3',),daemon=True).start()
for frame in frames:
    start=time()
    print(frame)
    sleep(0.03333333333-(time()-start))
