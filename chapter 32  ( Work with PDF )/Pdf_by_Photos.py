from PIL import Image

img1=Image.open("B_img.jpg")
img2=Image.open("download.jfif")


img1.save("Photos.pdf","PDF",resolution=100.0,save_all=True,append_images=[img2])