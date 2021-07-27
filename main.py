import tkinter
from tkinter import *
import os

class Diary(Frame):

    def __init__(self, window):
        Frame.__init__(self, window)
        self.dirlist = list()
        self.main_folder = str()
        self._init_window(window)


    def _init_window(self, window):

        # create menu
        self.mainmenu = Menu(window)
        window.config(menu=self.mainmenu)
        helpmenu = Menu(self.mainmenu, tearoff=0)
        helpmenu.add_command(label='File')
        helpmenu.add_command(label='Folder')
        self.mainmenu.add_cascade(label = 'Open', menu=helpmenu)
        self.mainmenu.add_command(label='Save')

        #create labels for brows and addit text
        self.label_dir = tkinter.Label(text='', bg='grey', width=20, height=25)
        self.label_dir.place(x=50, y=50)
        self.label_text = tkinter.Text(bg='grey', width=40, height=25)
        self.label_text.place(x=250, y = 50)

    def _get_list_dir(self):
        for item in os.listdir():
            self.dirlist.append(item)
        return self.dirlist


    def _open_dir(self):
        pass


    def _write_file(self):
        pass


if __name__ == "__main__":
    window = tkinter.Tk()
    window.geometry('700x500')
    e = Diary(window)
    window.mainloop()
