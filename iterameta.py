from Tkinter import *

# import routines or something else

MyWindow = Tk()
MyWindow.title('ITERAMETA')
MyWindow.geometry('300x100+400+400')

ButtonTOCSY = Button(MyWindow, text='TOCSY peak list',command='')
ButtonTOCSY.pack(side=LEFT,padx=5, pady=5)

ButtonQuit = Button(MyWindow,text='Quit',command='')
ButtonQuit.pack(side=LEFT,padx=5,pady=5)

Text = StringVar()

MyWindow.mainloop()
