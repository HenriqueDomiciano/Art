import cv2 
import numpy as np
import random as rd
import imageio
import os

def build(img,colors,positions,thickness,sizes,n_of_circles,k):
    if k != 0:
        for i in range(len(positions)):
            color_red = rd.randint(20,255)
            color_blue = rd.randint(20,255)
            color_green= rd.randint(20,255)
            colors.append([color_blue,color_green,color_red])
            cv2.circle(img,center =tuple(positions[i]) ,radius =sizes[i],color=colors[-1] ,thickness=thickness[i])
    else:
        for i in range(n_of_circles):
            color_red = rd.randint(20,255)
            color_blue = rd.randint(20,255)
            color_green= rd.randint(20,255)
            colors.append([color_blue,color_green,color_red])
            thickness.append(2)
            cv2.circle(img,center =tuple(positions[-1]) ,radius =sizes[-1],color=colors[-1] ,thickness=thickness[-1])
    return img,colors,positions,thickness,sizes

images,colors,positions,thickness,sizes = [],[],[[512,512]],[],[10]
n_of_circles = 1
phi = 0
img = np.zeros((512,512,3), np.uint8)
for i in range(300):
    
    k = 20
    img,colors,positions,thickness,sizes = build(img,colors,positions,thickness,sizes,n_of_circles,i)
    poisitions = np.array(positions)
    positions[0][0] = 512//2-((k)* int(( phi * np.cos(phi))))#coordenada x
    positions[0][1] = 512//2-((k) * int(( phi * np.sin(phi))))#coordenada y
    positions = list(positions)
    phi += 0.2
    cv2.imwrite(f'image1/{i**10}.png',img)

png_dir = r'C:\Users\Dell\Desktop\Art\image1'
for file_name in sorted(os.listdir(png_dir),key = len):
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
with imageio.get_writer('movie6.gif', mode='I',fps=60) as writer:
    for i in images :
        writer.append_data(i)
