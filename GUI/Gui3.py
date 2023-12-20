from tkinter import filedialog,messagebox,Menu
import tkinter as tk
from PIL import Image,ImageTk
from GUI.Global_control import root,frame,img,clear,set_file_path,get_file_path,get_save_path,set_save_path
import math
from tools import Image_super_resolution
import cv2
def gui3():
    clear()
    root.title('图片超分辨率')
    default_val = 100
    scale_var=tk.IntVar()
    scale_var.set(default_val)
    scale = tk.Scale(frame,orient=tk.HORIZONTAL,variable=scale_var)
    scale.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)

    bt=tk.Button(frame,text="超分辨率并保存",font=("黑体",20))
    bt.place(relx=0.45,rely=0.85,relwidth=0.4,relheight=0.1)
    bt1=tk.Button(frame,text="请在此添加图片",font=("黑体",20))
    bt1.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.5)
    bt2=tk.Button(frame,text="重新导入图片",font=("黑体",20))
    def preview():
        file_path1=get_file_path()
        if file_path1 != None:
            global img
            img = Image.open(file_path1)
            w,h = img.size 
            max1=400
            if(w>max1 or h>max1):
                if(w>h):
                    new_w=max1
                    new_h=max1*h//w
                    img= img.resize((new_w,new_h))
                else:
                    new_h=max1
                    new_w=max1*w//h
                    img=img.resize((new_w,new_h))
            global img1,imgLabel
            img1 = ImageTk.PhotoImage(img)
            imgLabel = tk.Label(frame,image=img1)
            imgLabel.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.5)
            w,h = img.size 
            global scalew,scaleh
            scalew=math.ceil( w/default_val )
            scaleh=math.ceil( h/default_val )
            bt2.place(relx=0.1,rely=0.85,relwidth=0.25,relheight=0.1)  
    
    
    def calc1():
        file_path1=get_file_path()
        if file_path1==None:
            messagebox.showinfo("Message_title", "请先导入图片！")
            return 
        try: 
            #print(ww,hh)
            print(file_path1)
            result=Image_super_resolution.run(file_path1)
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("jpg file", "*.jpg"),("png file","*.png")])
            set_save_path(save_path)
            cv2.imwrite(save_path, result)
            messagebox.showinfo("Message_title", "成功保存！")
        except:
            messagebox.showinfo("Message_title", "保存失败！")
    def upload_file():
        file_path1= filedialog.askopenfilename(filetypes=[("jpg file", "*.jpg"),("png file","*.png")])
        set_file_path(file_path1)
        if file_path1:
            bt1.destroy()
            preview()
            messagebox.showinfo("Message_title", "成功导入图片！")
        else :
            messagebox.showinfo("Message_title", "未成功导入！")

    bt.config(command=calc1)
    bt1.config(command=upload_file)
    bt2.config(command=upload_file)
    preview()
    def scaleFn(val):
        file_path1=get_file_path()
        if file_path1==None:
            return 
        if int(val) <= 10:#限制
            return
        global scalew,scaleh
        targetw = int(val)*scalew
        targeth = int(val)*scaleh
        bg = img.resize((targetw, targeth)) 
        global img1,imgLabel
        img1= ImageTk.PhotoImage(bg)    
        imgLabel.config(image=img1)
        #imgLabel.image = bgg
    scale.config(command=lambda x:scaleFn(x))
