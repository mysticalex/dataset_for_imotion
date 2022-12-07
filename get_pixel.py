import numpy as np
import cv2
import csv



emotion_dictionary ={'angry':'0','disgust':'1','fear':'2','happy':'3','neutral':'4','sad':'5','surprise':'6'}




image_filename="img0.png"
emotion="angry"




img = cv2.imread(emotion+'/'+image_filename, 1)

pixel_values=[]
for p in img:
    for q in p:
        pixel=sum(q)/3
        pixel_values.append(pixel)
        
#print(pixel_values)    
   
header=['emotion_index','pixel_value','data_split']
data=[emotion_dictionary[emotion],pixel_values,"training"]



with open('fer.csv',"a",encoding="UTF8") as f:
    
            writer=csv.writer(f)
        
           
            writer.writerow(data)
            