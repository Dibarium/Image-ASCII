from PIL import Image
import os
from PIL import ImageDraw 
def greyscale(image):     
    image_file = Image.open(image) # open colour image
    image_file = image_file.convert('L') # convert image to black and white
    image_file.save("resultat.png")
    ascii("resultat.png")
    os.remove("resultat.png")

    
def ascii(image):
    lines = []
    average = []
    total = []
    final = []
    fichier = open("output.txt","w")
    caracter = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,'"'^`"'". "[::-1]
    dico = dict((str(i),caracter[i]) for i in range(len(caracter)))
    print(dico)
    photo = Image.open(image) #your image
    for y in range(photo.size[1]):
        for x in range(photo.size[0]):
            color = photo.getpixel((x,y))
            average.append(color)
            
            if len(average) % 2 == 0:
                lines.append((average[0]+average[1])/2)
                average = []
       
        total.append(lines)
        lines = []

    lines = []
    for y in range(0,len(total),2):
        for x in range(len(total[y])):
            try:
                color = str(round(((total[y][x]+total[y+1][x])/2)/4))
            except:
                color = str(round(total[y][x]/10))
            fichier.write(dico[color])
        fichier.write("\n")
    fichier.close()
        

greyscale("desmineurs.png")