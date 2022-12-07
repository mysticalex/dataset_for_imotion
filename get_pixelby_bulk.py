import numpy as np
import cv2
import csv
import os


def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file            
            

emotion_dictionary ={'angry':'0','disgust':'1','fear':'2','happy':'3','neutral':'4','sad':'5','surprise':'6'}

#chose the folder name
emotion="disgust"




for file in get_files(emotion):
    img = cv2.imread(emotion+'/'+file, 1)
    pixel_values=[]
    for p in img:
        for q in p:
            pixel=sum(q)/3
            pixel_values.append(pixel)
    data=[emotion_dictionary[emotion],pixel_values,"training"]
            
    with open('fer.csv',"a",encoding="UTF8") as f:
    
        writer=csv.writer(f)
        writer.writerow(data)
            
    

            