import numpy
from PIL import Image
from pprint import pprint

im_old = Image.open('/home/goods/Desktop/bat.png')
im_old = im_old.convert("RGBA")
im_new = Image.open('/home/goods/Desktop/batnew.png')
im_new = im_new.convert("RGBA")
pixels_old = im_old.load() # this is not a list, nor is it list()'able
pixels_new = im_new.load()
pixelToPng = []
picChange = False
removedPixel = []
addedPixel = []
finalChangeIm = []
transparent = (255,255,255,0)
numPixelChange=0
width, height = im_old.size
width, height = im_new.size
all_pixelsOldLst = []

all_pixelsOld = []
all_pixelsNew = []


for x in range(width):
    for y in range(height):
        cpixel_old = pixels_old[x, y]
        pixAndLoc = cpixel_old + (x,) + (y,)
        all_pixelsOld.append(pixAndLoc)

for x in range(width):
    for y in range(height):
        cpixel_new = pixels_new[x, y]
        pixAndLocNew = cpixel_new + (x,) + (y,)
        all_pixelsNew.append(pixAndLocNew)

for i in range(len(all_pixelsOld)):
    if(all_pixelsOld[i]!=all_pixelsNew[i]):
        picChange=True
        removedPixel.append(all_pixelsOld[i])
        addedPixel.append(all_pixelsNew[i])

#print(removedPixel)
#print(addedPixel)

changedPixImage = Image.new(im_new.mode, im_new.size )

for x in range(width):
    for y in range(height):
        for i in addedPixel:
            if i[4]==x and i[5]==y:
                tmpPix = i[0],+i[1],+i[2],+i[3],
                finalChangeIm.append(tmpPix)
                addedPixel.remove(i)
                break
            else:
                finalChangeIm.append(transparent)
                break



#pprint(finalChangeIm)
changedPixImage.putdata(finalChangeIm)
changedPixImage.save('/home/goods/Desktop/changedPixImage.png')