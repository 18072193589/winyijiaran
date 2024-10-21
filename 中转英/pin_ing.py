import pinyin
import os
import tkinter as tk
from tkinter import filedialog

def transfer_pin(dir):
    for roots, dirs, files in os.walk(dir):
        # print(dirs)
        for s in dirs:
            # print(s)
            new_name=pinyin.get(s,format='strip')
            # print(new_name)
            os.rename(roots+os.sep+s,roots+os.sep+new_name)
            print (s,"=====",new_name)


root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()
transfer_pin(path)
root.destroy()