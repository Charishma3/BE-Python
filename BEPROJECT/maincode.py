import random
#import cv2 as cv
import pandas as df
from PIL import Image, ImageDraw,ImageFont
import numpy as np
class certificate:
    image_list=["ce{0}.png".format(i) for i in range(1,6)]
    cod_list=["cod{0}.txt".format(i) for i in range(1,6)]    
    def __init__(self,name,pmname,course,date,certid):
        self.i=random.randint(1,5)
        self.name=name
        self.pmname=pmname
        self.course=course
        self.date=date
        self.cid=certid
    def generate_certificate(self):
        img = Image.open("ce{}.png".format(self.i))
        d1 = ImageDraw.Draw(img)
        #fonts&font's size
        issuef = ImageFont.truetype('fonts/mate.regular.ttf',35)
        namef = ImageFont.truetype('fonts/too-freakin-cute-demo.regular.ttf',80)
        pmf = ImageFont.truetype('fonts/TrajanPro-Regular.ttf',45)
        sign1=ImageFont.truetype('fonts/andalusia.regular.otf',60)
        sign2=ImageFont.truetype('fonts/simplemind.regular.ttf',150)
        ceidf=ImageFont.truetype('fonts/typo-ring.demo.otf',30)
        coursef=ImageFont.truetype('fonts/playdates.handwriting.ttf',80)
        #location,text,color
        f=open("cod{}.txt".format(self.i),"r")
        coords=[int(j) for j in f.read().split("\n")]
        d1.text((coords[0],coords[1]), r"Issued on {}".format(self.date),font=issuef, fill="black")
        if self.i==3:
            d1.text((coords[2]+210, coords[3]), self.name.upper(),font=namef, fill="crimson")
        elif len(self.name)<15:
            d1.text((coords[2], coords[3]), self.name.upper().center(26),font=namef, fill="crimson")
        else:
            d1.text((coords[2], coords[3]), self.name.upper(),font=namef, fill="crimson")
        d1.text((coords[4], coords[5]), "Charishma",font=sign1, fill="lime")
        d1.text((coords[6], coords[7]), self.pmname,font=sign2, fill="deeppink")
        d1.text((coords[8], coords[9]), self.pmname,font=pmf, fill="maroon")
        d1.text((coords[10], coords[11]), "Certificate id:{}".format(self.cid),font=ceidf, fill="black")
        d1.text((coords[12], coords[13]), "{} Internship".format(self.course),font=coursef, fill="coral")
        #img.show()
        img.save("test/{0}.png".format(self.name))
        print("certificate generated for "+self.name,"using template no:",self.i)
#driverscode
if __name__ == "__main__": 
    # Reading the csv file .... u can use xlsx file .. i have some issues/errors so im using same data but in csv format
    df_new = df.read_csv('Myproject.csv') #use read_excel("filepath") instead when u go for xlxs file
    #getting names from df
    nameslist=df_new["Name"].tolist()
    #getting course from df
    courselist=df_new["Course"].tolist()
    ceridlist=df_new["certificate id"].tolist()
    issuedatelist=df_new["issue date"].tolist()
    pmlist=df_new["Project Manager"].tolist()
    for i in range(len(nameslist)):
        a=certificate(nameslist[i],pmlist[i],courselist[i],issuedatelist[i],ceridlist[i])
        a.generate_certificate()
print("Successfully generated required certificates..........!")