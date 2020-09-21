import cv2
import time
from PIL import Image
#!pip install PyAutoGUI
#!pip install pytesseract
import pytesseract 
#import pyautogui as pag
def binarize(image_to_transform, threshold):
    # now, lets convert that image to a single greyscale image using convert()
    output_image=image_to_transform.convert("L")
    # the threshold value is usually provided as a number between 0 and 255, which
    # is the number of bits in a byte.
    # the algorithm for the binarization is pretty simple, go through every pixel in the
    # image and, if it's greater than the threshold, turn it all the way up (255), and
    # if it's lower than the threshold, turn it all the way down (0).
    # so lets write this in code. First, we need to iterate over all of the pixels in the
    # image we want to work with
    for x in range(output_image.width):
        for y in range(output_image.height):
            # for the given pixel at w,h, lets check its value against the threshold
            if output_image.getpixel((x,y))< threshold: #note that the first parameter is actually a tuple object
                # lets set this to zero
                output_image.putpixel( (x,y), 0 )
            else:
                # otherwise lets set this to 255
                output_image.putpixel( (x,y), 255 )
    #now we just return the new image
    return output_image
cap=cv2.VideoCapture(0)
time.sleep(5)
for i in range(30):
    ret,frame=cap.read()
cv2.imwrite("output.jpg",frame)
cv2.imshow("img",frame)
cv2.waitKey(0) 
cap.release()
cv2.destroyAllWindows()
name=r'C:\Users\pavni\Desktop\Tinkerer_course\final_project--pillow+pyautogui+opencv\output.jpg'
img=Image.open(name)
print(img.size)
print(img.width,img.height)
Image._show(img)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

im=[img]
im.append(img.convert('L'))
im.append(img.convert('1'))
fimage=im[0]
sheet=Image.new(fimage.mode,(3*fimage.width,3*fimage.height))

x=0
y=0
img4=img.convert("P", palette=Image.ADAPTIVE, colors=25)
img5=binarize(img,150)
img6=binarize(img,200)
im.append(img4.convert('L'))
im.append(binarize(img,150))
im.append(binarize(img,200))
im.append(img.convert("P", palette=Image.ADAPTIVE, colors=25))
im.append(img.convert("P", palette=Image.ADAPTIVE, colors=15))
im.append(img.convert("P", palette=Image.ADAPTIVE, colors=5))


for q in range(0,9):    
    if (q==3 or q==6) :
        x=x+img.width
        y=0
    sheet.paste(im[q],(x,y))
    y=y+img.height
    
    
sheet=sheet.resize((1500,1000))
Image._show(sheet)

text=pytesseract.image_to_string(sheet)
print(text)
