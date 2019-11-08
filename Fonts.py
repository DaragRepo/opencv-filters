from tkinter import  Tk, font, Label, W


root = Tk()
my_font = font.families()

print(my_font)
# print(my_font)
for i in range(80,100):
    fonts = font.Font(family=my_font[i],size=15,weight="bold")
    Label(root, text=my_font[i], bg="green", fg="yellow", font= fonts).grid(row=i, column=0, sticky=W)


root.mainloop()