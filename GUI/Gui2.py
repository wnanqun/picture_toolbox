from GUI.Global_control import root,frame,img,clear,set_file_path,get_file_path,get_save_path,set_save_path
from tkinter import filedialog,messagebox,Menu
import tkinter as tk
from PIL import Image,ImageTk
import math
def gui2():
    clear()
    root.title('图片压缩')
    default_val = 100
    scale_var=tk.IntVar()
    scale_var.set(default_val)
    scale = tk.Scale(frame,orient=tk.HORIZONTAL,variable=scale_var)
    scale.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)
    label3=tk.Label(frame,text="宽度:",font=("黑体",15))
    label4=tk.Label(frame,text="高度:",font=("黑体",15))
    w1=tk.IntVar()
    h1=tk.IntVar()
    input3=tk.Entry(frame,textvariable=w1)
    input4=tk.Entry(frame,textvariable=h1)
    label3.place(relx=0.15,rely=0.85,relwidth=0.2,relheight=0.05)
    input3.place(relx=0.35,rely=0.85,relwidth=0.2,relheight=0.05)
    label4.place(relx=0.15,rely=0.9,relwidth=0.2,relheight=0.05)
    input4.place(relx=0.35,rely=0.9,relwidth=0.2,relheight=0.05)
    bt=tk.Button(frame,text="压缩并保存",font=("黑体",20))
    bt.place(relx=0.65,rely=0.85,relwidth=0.2,relheight=0.1)
    bt1=tk.Button(frame,text="请在此添加图片",font=("黑体",20))
    bt1.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.5)
    bt2=tk.Button(frame,text="重新导入图片",font=("黑体",15))
    def preview():
        file_path=get_file_path()
        if file_path != None:
            global img
            img = Image.open(file_path)
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
            bt2.place(relx=0.01,rely=0.6,relwidth=0.23,relheight=0.1) 
    
    def calc1():
        file_path=get_file_path()
        if file_path==None:
            messagebox.showinfo("Message_title", "请先导入图片！")
            return 
        global img
        w,h=img.size
        try :
            ww=w1.get()
            hh=h1.get()
        except:
            messagebox.showinfo("Message_title", "输入非法！")
            return
        if ww==0 and (not hh):
            messagebox.showinfo("Message_title", "请设定目标尺寸！")
            return
        else :
            if not hh:
                hh=ww*h//w
            if not w1:
                ww=hh*w//h
        
        try: 
            #print(ww,hh)
            img = Image.open(file_path)
            img=img.resize((ww,hh))
            save_path1 = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("jpg file", "*.jpg"),("png file","*.png")])
            img.save(save_path1)
            set_save_path(save_path1)
            messagebox.showinfo("Message_title", "成功保存！")
        except:
            messagebox.showinfo("Message_title", "保存失败！")
    def upload_file():
        
        file_path1 = filedialog.askopenfilename(filetypes=[("jpg file", "*.jpg"),("png file","*.png")])
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
        file_path=get_file_path()
        if file_path==None:
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
