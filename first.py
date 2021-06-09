import cv2 
import numpy as np
import random as rd
import imageio
import os
def build(img,colors,positions,thickness,sizes,n_of_circles,k):
    if k != 0:
        for i in range(len(positions)):
            cv2.circle(img,center =tuple(positions[i]) ,radius =sizes[i],color=colors[i] ,thickness=thickness[i])
    else:
        for i in range(n_of_circles):
            color_red = rd.randint(20,255)
            color_blue = rd.randint(20,255)
            color_green= rd.randint(20,255)
            center_x,center_y = rd.randint(0,512),rd.randint(0,512)
            size = rd.randint(50,100)//3
            sizes.append(size)
            positions.append([center_x,center_y])
            colors.append([color_blue,color_green,color_red])
            thickness.append(rd.randint(-1,7))
            cv2.circle(img,center =tuple(positions[-1]) ,radius =sizes[-1],color=colors[-1] ,thickness=thickness[-1])
    return img,colors,positions,thickness,sizes

images,colors,positions,thickness,sizes = [],[],[],[],[]
n_of_circles = rd.randint(10,20)
img = np.zeros((512,512,3), np.uint8)
for i in range(90):
    img,colors,positions,thickness,sizes = build(img,colors,positions,thickness,sizes,n_of_circles,i)
    k,u= 1,1
    positions = np.array(positions)
    positions = positions + 5  
    positions = list(positions)
    cv2.imwrite(f'image1\{(i+10)}.png',img)
png_dir = r'C:\Users\Dell\Desktop\Art\image1'
for file_name in sorted(os.listdir(png_dir)):
    if file_name.endswith('.png'):
        print(file_name)
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
with imageio.get_writer('movie5.gif', mode='I',fps=10) as writer:
    for i in images :
        writer.append_data(i)
#writing the sha256 algorithm 
'''
import hashlib

filename = "movie.gif"
with open(filename,"rb") as f:
    bites = f.read() # read entire file as bytes
    readable_hash = hashlib.sha256(bites).hexdigest()
value = readable_hash
with open('movie.txt','w') as fw:
    fw.write(value)
'''