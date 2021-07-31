import tkinter
from tkinter import filedialog as fd, Frame, StringVar, Menu
from tkinter import *
import os
import datetime
from datetime import *

class Diary(Frame):

    def __init__(self, window):
        Frame.__init__(self, window)
        self.dirlist = list()
        self.main_folder = str()
        self.filename = ''
        self.new_filename = ''
        self.my_string_var = StringVar()
        self.base_file_text = ''
        self._init_window(window)


    def _init_window(self, window):
        #new file name
        self.label_new_file_name = tkinter.Text(bg='white', width=12, height=1)
        self.label_new_file_name.place(x=50, y=20)
        # create menu
        self.mainmenu = Menu(window)
        window.config(menu=self.mainmenu)
        self.mainmenu.add_command(label='Open', command=self.open_file)
        self.mainmenu.add_command(label='Save', command=self.save)
        #create labels for brows and addit text
        # self.label_dir = tkinter.Label(text='', justify='left',  bg='grey', width=20, height=25)
        self.label_dir = tkinter.Text(bg='grey', width=20, height=25)
        self.label_dir.place(x=50, y=50)
        self.label_text = tkinter.Text(bg='grey', width=45, height=25)
        self.label_text.place(x=250, y = 50)



    def open_file(self):
        f_types = [("All Files","*.*"),("PDF File" , "*.pdf"), ('Python files', '*.py'), ("Text files", '*.txt')]
        dlg = fd.Open(self, filetypes = f_types)
        fl = dlg.show()
        self.label_text.delete('1.0', END)
        if fl != '':
            self.my_string_var.set(self.read_from_file(fl))
        # self.label_dir['text'] = self._get_list_dir()
        self.label_dir.delete('1.0', END)
        self.label_dir.insert(END, "Files in this dir:\n")
        for i in self._get_list_dir():
            self.label_dir.insert(END, str(f"  {str(i)}\n"))
        #disable input to block text
        self.label_dir.config(state=DISABLED)



    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            text = f.read()
            self.base_file_text = text
            self.filename = filename
        self.label_text.insert('1.0', text)
        return text

    def save(self):
        self.new_filename = self.label_new_file_name.get('1.0', 'end-1c')
        filename = self.new_filename
        if filename == '':
            filename = str(datetime.now()).split(' ')[0] + '.txt'
        else:
            with open(filename, 'w') as f:
                f.write(self.label_text.get('1.0', 'end-1c'))


    def _get_list_dir(self):
        for item in os.listdir():
            if item == '\n' or item == '\t' or item == ' ' or item == '':
                continue
            else:
                self.dirlist.append(item)
        return self.dirlist




if __name__ == "__main__":
    window = tkinter.Tk()
    window.geometry('700x500')
    window.resizable(False, False)
    e = Diary(window)
    window.mainloop()
