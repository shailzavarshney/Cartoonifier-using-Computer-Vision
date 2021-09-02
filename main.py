import numpy as np #to store image
import matplotlib.pyplot as plt # for visualisation
import imageio #to read image stored at particular path
# for creating GUI application
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import cv2 #for image processing
import easygui #to open the filebox
import uuid # for giving unique filename
import sys  
import os 
from tkinter import messagebox
# creating Main window
root=tk.Tk()
root.geometry('450x400')
root.title('Cartoonifier by Shailza')
root.configure(background='#F0D9FF')
root.iconbitmap("icon.ico")

label_main=Label(root,text="CARTOONIFY YOUR IMAGE ",font=("times new roman",20,"bold"),bd=10,relief=GROOVE,bg='#2A0944',fg="white").pack(side=TOP,fill=X)

load= Image.open("image3.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=50, y=75)

load_arr= Image.open("bg_change_1.jpg")
render_arr = ImageTk.PhotoImage(load_arr)
img_arr = Label(root, image=render_arr,bd=0)
img_arr.place(x=195, y=150)

load_1= Image.open("image4.jpg")
render_1 = ImageTk.PhotoImage(load_1)
img_1 = Label(root, image=render_1)
img_1.place(x=250, y=75)

def upload():
    imagepath=easygui.fileopenbox()
    cartoonify(imagepath)


def cartoonify(imagepath):
    #  to read the image
    image = cv2.imread(imagepath)
    original_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # to check if image is chosen or not 
    if original_image is None:
        print("Can not find any image !!! . Please choose appropriate file")
        sys.exit()

    # image to grayscale
    gray_image= cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    #applying median blur to smoothen the image
    smooth_image= cv2.medianBlur(gray_image, 5)

    # to get the edges
    edge_image = cv2.adaptiveThreshold(smooth_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
    cv2.THRESH_BINARY, 9,9)

    #  bilateral filter to remove noise
    filtered_image = cv2.bilateralFilter(original_image, 9, 400,400)

    #masking edged image with our "BEAUTIFY" image
    masked_image = cv2.bitwise_and(filtered_image,filtered_image, mask=edge_image)

    resized_image= cv2.resize(masked_image, (400,500))

    plt.imshow(resized_image)

    # save1=Button(root,text="Save",command=lambda: save(resized_image,imagepath),padx=10,pady=10)
    # save1.configure(background='#2A0944', foreground='white',font=('calibri',15,'bold'))
    # save1.pack(side=TOP,pady=60)
    
    plt.show()
    
def save(ReSized6, imagepath):
    #saving an image
    unique_filename = str(uuid.uuid4().hex)
    path1 = os.path.dirname(unique_filename)
    extension=os.path.splitext(imagepath)[1]
    path = os.path.join(path1,unique_filename+extension)
    cv2.imwrite(path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))
    I= "Image Saved !!!"
    # to show the message
    tk.messagebox.showinfo(title=None, message=I)

upload=Button(root,text="Cartoonify your Image",command=upload,padx=10,pady=5)
upload.configure(background='#2A0944', foreground='white',font=('calibri',12,'bold'))
upload.place(x=130,y=300)

root.mainloop()



