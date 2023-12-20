from tkinter import filedialog,messagebox,Menu
import tkinter as tk
import time
from PIL import Image,ImageTk
from GUI.Global_control import root,frame,img,clear,set_file_path,get_file_path,get_save_path,set_save_path
from tools import Generate_image
def gui4():
    clear()
    root.title('图片生成')
    def edit_txt():
        clear()
        label1=tk.Label(frame,text="请输入文本描述（仅支持英文）:",font=("黑体",15))
        label1.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.1)
        input1=tk.Text(frame,bg='pink')
        input1.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.5)
        bt=tk.Button(frame,text="开始生成",font=("黑体",20))
        bt.place(relx=0.65,rely=0.85,relwidth=0.2,relheight=0.1)
        
        
        def calc2():
            global describe_text
            describe_text=input1.get(1.0,tk.END)
            if describe_text:
                clear()
                label2=tk.Label(frame,text="加载中，请耐心等待!",font=("黑体",20))
                label2.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.5)
                show_img()
            else:
                messagebox.showinfo("Message_title", "请输入描述文本！")
        bt.config(command=calc2)
    def show_img():
        global img
        global describe_text
        img=Generate_image.run(describe_text)
        clear()
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
        bt=tk.Button(frame,text="返回",font=("黑体",20))
        bt.place(relx=0.65,rely=0.85,relwidth=0.2,relheight=0.1)
        bt1=tk.Button(frame,text="保存",font=("黑体",20))
        bt1.place(relx=0.25,rely=0.85,relwidth=0.2,relheight=0.1)
        def calc3():
            edit_txt()
        def save_img():
            global img,save_path
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("jpg file", "*.jpg"),("png file","*.png")])
            set_save_path(save_path)
            if save_path :
                img.save(save_path)
                messagebox.showinfo("Message_title", "成功保存图片！")
            else :
                messagebox.showinfo("Message_title", "未成功保存！")
        bt.config(command=calc3)
        bt1.config(command=save_img)
    edit_txt()
