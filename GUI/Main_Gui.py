import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import simpledialog
from tkinter.ttk import Treeview
from tkinter import messagebox
import shutil
from tkinter import *
import math
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog


from GUI.Global_control import root,frame,file_path,img,clear
from GUI.Gui2 import gui2
from GUI.Gui3 import gui3
from GUI.Gui4 import gui4
from GUI.Gui5 import gui5
class Main_Gui():
    def __init__(self):
        self.buttons=[]
    def add_function(self,text,calc):
        new_bt=tk.Button(frame,text=text,font=("黑体",20),command=calc,bg='#FFFFFF')
        new_bt.place(relx=0.35,rely=0.2+len(self.buttons)*0.1,relwidth=0.3,relheight=0.1)
        self.buttons.append(new_bt)
    
    def show(self):
        clear()
        app=Main_Gui()
        function_num=4
        functions_name=['图片压缩','图片分类','图片生成','图片超分辨率']
        functions_master=[gui2,gui5,gui4,gui3]
        for i in range(function_num):
            app.add_function(functions_name[i],functions_master[i])