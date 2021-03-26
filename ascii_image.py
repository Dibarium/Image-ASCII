from PIL import Image
import os
from PIL import ImageDraw
import PIL
import text_to_image
def greyscale(image): 
    image_file = Image.open(image) # open colour image
    image_file = image_file.convert('L') # convert image to black and white
    image_file.save("resultat.png")
    ascii("resultat.png")
    os.remove("resultat.png")

def ascii(image):
    fichier = open("output.txt","w")
    caracter = ".'"'`^"'",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    
    dico = dict((str(i),caracter[i]) for i in range(len(caracter)))

    photo = Image.open(image) #your image
    for y in range(photo.size[1]):
        for x in range(photo.size[0]):
            x = str(round(photo.getpixel((x,y))/4))
            fichier.write(dico[x])
        fichier.write("\n")
    fichier.close()

greyscale("dogo.png")
encoded_image_path = text_to_image.encode_file("output.txt", "output_image.png")