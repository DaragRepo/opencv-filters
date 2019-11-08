# class Employee:
#     def computerSalary(self):
#         return "General"
#
#
#
# class Engineer(Employee):
#     def computerSalary(self):
#         return "Engineering salary"
#
#
#
# def get(Employee):
#         print(Employee.computerSalary())
#
#
# bob = Employee()
# engineer = Engineer()
# company = [bob, engineer]
# # print(bob.computerSalary())
# get(engineer)
# # for emp in company:
# #     print(emp.computerSalary())
#
#

from GUI import *
# from Video import *
# from Fonts import *
# from MeanBlur import MeanBlur


# b,g,r = cv2.split(image)
# img = cv2.merge((r,g,b))

# A root window for displaying objects
# root = Tk()

# Convert the Image object into a TkPhoto object
# im = Image.fromarray(img)
# imgtk = ImageTk.PhotoImage(image=im)

# Put it in the display window
# Label(root, image=imgtk).pack()



#
# Some widgets (like text entry widgets, radio buttons and so on) can be connected directly to application variables by using special options: variable, textvariable, onvalue, offvalue, and value. This connection works both ways: if the variable changes for any reason, the widget it's connected to will be updated to reflect the new value. These Tkinter control variables are used like regular Python variables to keep certain values. It's not possible to hand over a regular Python variable to a widget through a variable or textvariable option. The only kinds of variables for which this works are variables that are subclassed from a class called Variable, defined in the Tkinter module. They are declared like this:
# x = StringVar() # Holds a string; default value ""
# x = IntVar() # Holds an integer; default value 0
# x = DoubleVar() # Holds a float; default value 0.0
# x = BooleanVar() # Holds a boolean, returns 0 for False and 1 for True
# To read the current value of such a variable, call the method get(). The value of such a variable can be changed with the set() method