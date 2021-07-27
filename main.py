import tkinter
from tkinter import *
import os

class Diary(Frame):

    def __init__(self, window):
        Frame.__init__(self, window)
        self.dirlist = list()
        self.main_folder = str()


    def _init_window(self):
        pass


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
