from tkinter import filedialog,messagebox
import tkinter as tk
from PIL import Image,ImageTk
from GUI.Global_control import root,frame,img,clear,set_file_path,get_file_path,get_save_path,set_save_path
from tools import Image_classification
def gui5():
    clear()
    root.title('图像分类')
    bt=tk.Button(frame,text="查看分类结果",font=("黑体",20))
    bt.place(relx=0.65,rely=0.85,relwidth=0.3,relheight=0.1)
    bt1=tk.Button(frame,text="请在此添加图片",font=("黑体",20))
    bt1.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.5)
    Label_result = tk.Label(frame,bg='pink')
    Label_result.config(text='未有分类结果',font=("黑体",20))
    Label_result.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.1)
    bt2=tk.Button(frame,text="重新导入图片",font=("黑体",20))
    def upload_file():
        file_path1 = filedialog.askopenfilename(filetypes=[("jpg file", "*.jpg"),("png file","*.png")])
        set_file_path(file_path1)
        if file_path1:
            show_img()
            bt1.destroy()
            messagebox.showinfo("Message_title", "成功导入图片！")
        else :
            messagebox.showinfo("Message_title", "未成功导入！")
    def show_img():
        global img
        file_path=get_file_path()
        if file_path!=None:
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
            bt2.place(relx=0.15,rely=0.85,relwidth=0.3,relheight=0.1)
    def calc3():
        file_path=get_file_path()
        if not file_path:
            messagebox.showinfo("Message_title", "请先导入图片！")
            return
        ans=Image_classification.run(file_path)
        Label_result.config(text=ans)
        bt2=tk.Button(frame,text="重新导入图片",font=("黑体",20),command=upload_file)
        bt2.place(relx=0.15,rely=0.85,relwidth=0.3,relheight=0.1)
        messagebox.showinfo("Message_title", "分类成功！")
    show_img()
    bt1.config(command=upload_file)
    bt2.config(command=upload_file)
    bt.config(command=calc3)    
    