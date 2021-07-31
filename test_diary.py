from main import *
import pytest
import tkinter
from tkinter import *

class Test_Diary():
    def test_file(self):
        window = tkinter.Tk()
        window.geometry('700x500')
        window.resizable(False, False)
        e = Diary(window)
        # window.mainloop()
        assert e.read_from_file('example.txt') != ''
