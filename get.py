#!/bin/python3
from os import system, mkdir, listdir
from PIL import Image
from time import time

start=time()

RESOLUTION=120 #50
GRAYSCALE_CHARS=['#','.']

try:
    mkdir('ascii')
except FileExistsError:
    pass
try:
    mkdir('images')
except FileExistsError:
    pass

system('rm -rf ascii/*')
system('rm -rf images/*')
#system('rm "[HD] Touhou - Bad Apple!! [ＰＶ] (Shadow Art)-UkgK8eUdpAo.mkv"')
system('rm "[HD] Touhou - Bad Apple!! [ＰＶ] (Shadow Art)-UkgK8eUdpAo.mp3"')

system('youtube-dl https://www.youtube.com/watch?v=UkgK8eUdpAo')
system('ffmpeg -i "[HD] Touhou - Bad Apple!! [ＰＶ] (Shadow Art)-UkgK8eUdpAo.mkv" images/%d.png')
system('ffmpeg -i "[HD] Touhou - Bad Apple!! [ＰＶ] (Shadow Art)-UkgK8eUdpAo.mkv" -q:a 0 -map a "[HD] Touhou - Bad Apple!! [ＰＶ] (Shadow Art)-UkgK8eUdpAo.mp3"')

for i in listdir('images'):
    image = Image.open(f'images/{i}')

    width, height = image.size
    aspectRatio = height/width
    newWidth = RESOLUTION
    newHeight = aspectRatio * newWidth * 0.55
    image = image.resize((newWidth, int(newHeight)))

    image = image.convert('L')
    pixels = image.getdata()
     
    newPixels = ''.join([GRAYSCALE_CHARS[(pixel//130)-1] for pixel in pixels])
    asciiImage = '\n'.join([newPixels[index:index + newWidth] for index in range(0, len(newPixels), newWidth)])

    with open(f"ascii/{i.split('.')[0]}.txt", "w") as file:
        file.write(asciiImage)

print(f'Runtime of {time()-start} s')
