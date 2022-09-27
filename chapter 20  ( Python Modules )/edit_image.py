import os
from PIL import Image,ImageEnhance,ImageFilter

#  change extension of image       require : Image Module

img=Image.open("B_img.jpg")
img.save("B_img.png")
# img.show("B_img.png")

#  resize the image                require : Image Module

# MAX_SIZE=(250,250)     # want 250 pixels
# img.thumbnail(MAX_SIZE)
# img.save("B_img_resize.jpg")

#  resize multiple images using for loop           require : Image Module and OS Module

for item in os.listdir() :
    if item.endswith(".jpg") :
        img2=Image.open(item)
        name,extension=os.path.splitext(item)
        img2.save(f"{name}_resize_multiple.png")

#  sharpness                       require : ImageEnhance Module

enhancer=ImageEnhance.Sharpness(img)
enhancer.enhance(5).save("B_img_sharpness.jpg")

#  color                         require : ImageEnhance Module

enhancer=ImageEnhance.Color(img)
enhancer.enhance(3).save("B_img_color.jpg")

#  brightness                       require : ImageEnhance Module

enhancer=ImageEnhance.Brightness(img)
enhancer.enhance(1.5).save("B_img_Brightness.jpg")

#  contrast                    require : ImageEnhance Module

enhancer=ImageEnhance.Contrast(img)
enhancer.enhance(0).save("B_img_contrast.jpg")

#  Gaussian Blur                require : ImageFilter Module

img.filter(ImageFilter.GaussianBlur(radius=4)).save("B_img_gaussian_blur.jpg")



