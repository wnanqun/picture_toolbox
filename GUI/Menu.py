#设置菜单栏
from GUI.Global_control import root,frame,img,clear,set_file_path,get_file_path,get_save_path,set_save_path
from GUI.Main_Gui import Main_Gui
from tkinter import filedialog,messagebox,Menu
def set_menu():
    def menuCommand_open():
        file_path1 = filedialog.askopenfilename(filetypes=[("jpg file", "*.jpg"),("png file","*.png")])
        set_file_path(file_path1)
        if file_path1:
            messagebox.showinfo("Message_title", "成功导入图片！")
        else :
            messagebox.showinfo("Message_title", "未成功导入！")
    def menuCommand_save():
        global save_path,save_file,img
        save_path1 = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("jpg file", "*.jpg"),("png file","*.png")])
        set_save_path(save_path1)
        if save_path1 and img:
            img.save(save_path1)
            messagebox.showinfo("Message_title", "成功保存图片！")
        else :
            messagebox.showinfo("Message_title", "未成功保存！")
    def menuCommand_return():
        Main_Gui().show()
    # 创建主目录菜单（顶级菜单）
    global root,frame,file_path,img
    mainmenu = Menu(root)
    # 在顶级菜单上新增"文件"菜单的子菜单，同时不添加分割线
    filemenu = Menu(mainmenu, tearoff=False)
    # 新增"文件"菜单的菜单项，并使用 accelerator 设置菜单项的快捷键
    filemenu.add_command(label="打开", command=menuCommand_open)
    filemenu.add_command(label="保存", command=menuCommand_save)
    filemenu.add_command(label="返回菜单栏", command=menuCommand_return)
    # 添加一条分割线
    filemenu.add_separator()
    mainmenu.add_cascade(label="文件", menu=filemenu)
    root.config(menu=mainmenu)