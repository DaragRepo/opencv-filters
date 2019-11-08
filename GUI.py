from tkinter import Tk, Label, Radiobutton, StringVar
from PIL import Image, ImageTk
from tkinter import filedialog
from Filter import Filter
from MeanBlur import MeanBlur
from MedianBlur import  MedianBlur
from GaussianBlur import GaussianBlur
from Translator import Translator
from Scaler import Scaler
from Rotator import Rotator
from Histogram import Histogram
from Canny import Canny


import cv2

class GUI:
    var = []
    path = ''
    img = ''
    filters = []
    myLabel = ''
    def __init__(self, master, title, resolution, filters):
        self.master = master
        self.var = StringVar(master)
        self.filters = filters
        master.title(title)
        master.geometry(resolution)
        self.path = self.getImagePath()
        self.addFilterButtons(filters)
        self.loadImage()

    def loadImage(self):
        img = ImageTk.PhotoImage(Image.open(self.path[0]).resize((500,500)))
        self.img = cv2.imread(self.path[0], cv2.IMREAD_UNCHANGED)
        label = Label(self.master, image = img)
        label.image = img
        label.place(x = 0, y= 40)
        self.myLabel = label

    def convertImage(self):
        if (cv2.split(self.img)):
            b,g,r = cv2.split(self.img)
            img = cv2.merge((r,g,b))
            print(img)
            im = Image.fromarray(img)
            im = im.resize((500,500))
            imgtk = ImageTk.PhotoImage(image=im)
            label = Label(self.master, image=imgtk)
            label.image = imgtk
            label.place(x = 0, y= 40)
            self.myLabel = label

    def selected(self):
        i = 0
        for filter in self.filters:
            if (str(i) == self.var.get()):
                # self.loadImage()
                self.img = filter.applyFilter(self.img)
            i = i+1
        self.convertImage()

    def getImagePath(self):
        return filedialog.askopenfilenames()

    def addFilterButtons(self, filters):
        i = 0
        xpos = 50
        for filter in filters:
            Radiobutton(self.master, text=filter.__class__.__name__, variable=self.var, value= i ,command= self.selected).place(x = xpos, y = 10 )
            i = i+1
            xpos = xpos+120


root = Tk()
filters = [MeanBlur(), MedianBlur(), GaussianBlur(), Translator(), Rotator(), Histogram(), Canny() ]

my_gui = GUI(root, "Window","900x900",filters)
root.mainloop()
