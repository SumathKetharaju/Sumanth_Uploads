# Python3 program to convert image to pfd
# using img2pdf library

# importing necessary libraries
import img2pdf
from PIL import Image
import os

# storing image path
img_path = r"C:\Users\SUMANTH\Desktop\Automation_Purposes\Automations\sample_image_2"

# storing pdf path
pdf_path = r"C:/Users/Admin/Desktop/Automation_Purposes/Automations/sample_file.pdf"

# opening image
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")
