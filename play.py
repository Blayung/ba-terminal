#!/bin/python3
from os import listdir, get_terminal_size
from time import time,sleep
from playsound import playsound
from threading import Thread

toAppend=get_terminal_size()[1]-max(len(open('ascii/1.txt','r').readlines()),0)

Thread(target=playsound,args=('[HD] Touhou - Bad Apple!! [ＰＶ] (Shadow Art)-UkgK8eUdpAo.mp3',),daemon=True).start()
i=1
while True:
    start=time()

    if i==len(listdir('ascii')):
        break

    for _ in range(toAppend):
        print('')
    with open(f'ascii/{i}.txt','r') as file:
        print(file.read())

    i+=1

    sleep(max(0.03333333333-(time()-start),0))
