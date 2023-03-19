try:
    import PIL
except:
    import os
    os.system("pip install Pillow")
    
from sys import argv
import os
from PIL import Image


if len(argv)<2:
    img = input("Glissez l'image ici\n")
    
else:
    img = argv[1]
    
    
taille = input("Qu'elle taille vous voulez la mettre ? Exemple : 1280/720\n\n")

taille = taille.split("/")
t = tuple(taille)
taille = []
for a in t:
    taille.append(int(a))

taille = tuple(taille)

new = os.path.basename(img)

t = new.split(".")



print("Traitement en cours ...")
Image.open(img).resize(taille).save("Image-resize."+t[1])
print("Image terminé !!")

import time
time.sleep(5)
exit()
