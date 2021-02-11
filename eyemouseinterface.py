import tkinter
from tkinter import messagebox
import eyetracking
top = tkinter.Tk()

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")
def Enterbuttonclicked():#this function is added manually too
        # camerainput=int(self.lineEdit.text())
        eyemouse=eyetracking.eye_mouse(1)
        eyemouse.eyetrack()
B = tkinter.Button(top,text="Enter",command=Enterbuttonclicked)

B.pack()
top.mainloop()