import io
import os
import threading
from PIL import  ImageTk
from PIL import Image as imim
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
from Weibo_Crawl_Engine import Weibo_Pic_Spider

class App:
    def __init__(self):
        self.root=Tk()
        self.root.title('weibo图片小爬虫')
        self.root.resizable(0,0)
        width=380
        height=310
        left=(self.root.winfo_screenwidth()-width)/2
        top=(self.root.winfo_screenheight()-height)/2
        self.root.geometry('%dx%d+%d+%d'%(width,height,left,top))
        self.s=Weibo_Pic_Spider()
        self.create_widgets()
        self.set_widgets()
        self.place_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.label1=ttk.Label(self.root,text='关键字：')
        self.entry_keyword_var=StringVar()
        self.entry_keyword=ttk.Entry(self.root,textvariable=self.entry_keyword_var,justify='center')
        self.btn_search=ttk.Button(self.root,text='搜索',command=self.do_search_users)

        self.label_disk=ttk.Label(self.root,text='保存位置：')
        self.entry_savelocation_var=StringVar()
        self.entry_savelocation=ttk.Entry(self.root,textvariable=self.entry_savelocation_var,justify='center')
        self.check_opendir_var=BooleanVar(value=False)

        self.label_userlist=ttk.Label(self.root,text='用户列表：')
        self.combobox_userlist=ttk.Combobox(self.root,value=[],state='readonly',justify='center')
        self.btn_set_save_dir=ttk.Button(self.root,text='选择',command=self.select_save_dir)

        self.btn_startcrawl=ttk.Button(self.root,text='开始爬取',command=lambda :self.thread_it(self.do_download_pic))

        self.label_state=ttk.Label(self.root,text='状态：')
        self.scrolltext_state=ScrolledText(self.root)

        self.label_show_userimg=ttk.Label(self.root,text='用户头像',justify="center",compound='bottom',background='lightblue',width=20)

        self.lableframe=ttk.Labelframe(self.root,text='')
        self.lable_tip=ttk.Label(self.lableframe,text='',foreground='red')

        self.m=Menu(self.root)
        self.root['menu'] = self.m
        self.s1=Menu(self.m,tearoff=False)
        self.s2=Menu(self.m,tearoff=False)
        self.s3=Menu(self.m,tearoff=False)

    def set_widgets(self):
        self.m.add_cascade(menu=self.s1,label='开始')
        self.m.add_cascade(menu=self.s2,label='操作')
        #self.m.add_cascade(menu=self.s3,label='关于')
        self.s1.add_command(label='打开文件夹',command=lambda:os.startfile(self.abs_path))
        self.s1.add_separator()
        self.s1.add_command(label='退出',command=self.quit_window)

        self.combobox_userlist.bind("<<ComboboxSelected>>",self.show_user_head)
        self.entry_keyword.bind('<Return>',self.do_search_users)
        self.root.protocol("WM_DELETE_WINDOW",self.quit_window)
        self.open_dir_var=IntVar()
        #这里只能使用checkbutton用于开关
        self.s2.add_command(label='搜索',command=self.do_search_users)
        self.s2.add_command(label='开始爬取',command=lambda :self.thread_it(self.do_download_pic))
        self.s2.add_separator()
        self.s2.add_checkbutton(label='下载完后打开文件夹',variable=self.open_dir_var,command=self.open_dir_after_crawl)
        self.btn_startcrawl.config(state=DISABLED)
        self.s2.entryconfig("开始爬取", state=DISABLED)
       # self.s3.add_command(label='关于作者',command=lambda :messagebox.showinfo('作者信息','作者：懷淰メ\nversion:1.5'))


    def place_widgets(self):
        self.label1.place(x=10,y=15)
        self.entry_keyword.place(x=80,y=15,width=190)
        self.btn_search.place(x=280,y=15)

        self.label_disk.place(x=10,y=55)
        self.entry_savelocation.place(x=80,y=55,width=190)
        self.btn_set_save_dir.place(x=280,y=55)

        self.label_userlist.place(x=10,y=95)
        self.combobox_userlist.place(x=80,y=95,width=190)
        self.btn_startcrawl.place(x=280,y=95)

        self.label_show_userimg.place(x=280,y=140,height=120)

        self.label_state.place(x=10,y=180)
        self.scrolltext_state.place(x=80,y=140,width=200,height=120)


        self.lableframe.place(x=80,y=260)
        self.lable_tip.pack(anchor="w",fill=X)

    def show_user_head(self,*args):
        current_index=self.combobox_userlist.current()
        paned_img=PanedWindow(self.label_show_userimg)
        head_img=self.search_result[current_index]['user_head_img'].split('?')[0]
        image_bytes=self.s.get_img_bytes(head_img)
        data_stream = io.BytesIO(image_bytes)
        pil_image = imim.open(data_stream)
        photo = pil_image.resize((95, 90))
        paned_img.image=ImageTk.PhotoImage(photo)
        self.label_show_userimg.config(image=paned_img.image,compound='bottom')

    def do_search_users(self,*args):
        self.combobox_userlist.config(value=[])
        try:
            self.search_result.clear()
        except AttributeError:
            pass
        key_word=self.entry_keyword_var.get().strip()
        if key_word !='':
            self.search_result=self.s.get_users(key_word)
            if self.search_result:
                user_names=[user_['user_name'] for user_ in self.search_result]
                self.combobox_userlist.config(value=user_names)
                self.btn_startcrawl.config(state=NORMAL)
                self.s2.entryconfig("开始爬取", state=NORMAL)
                self.combobox_userlist.current(0)
                self.show_user_head()
            else:
                messagebox.showinfo('提示',f'很抱歉，没有检索到关于[{key_word}]的用户！')
        else:
            messagebox.showwarning('警告','关键字不能为空！')

    def do_download_pic(self):
        try:
            if self.entry_savelocation_var.get()!='':
                current_item=self.search_result[self.combobox_userlist.current()]
                user_id=current_item['user_id']
                user_name=current_item['user_name']
                self.s.set_start_url(user_id)
                abs_path=self.entry_savelocation_var.get()+f'/{user_name}'
                self.abs_path=abs_path
                self.s.do_make_dirs(abs_path)
                for pic in self.s.get_pics_url():
                    file_name = pic.split('/')[-1]
                    self.s.do_download_pic(pic,file_name,abs_path)
                    self.insert_into_scrolltext(f"{file_name}下载完成...")
                else:
                    self.btn_startcrawl.config(state=NORMAL)
                    self.s2.entryconfig("开始爬取", state=NORMAL)
                    if self.open_dir_flag:
                        os.startfile(self.abs_path)
            else:
                messagebox.showwarning('警告', '请选择图片保存路径！')
                self.select_save_dir()
        except AttributeError :
            messagebox.showwarning('警告','请先搜索！')

    def select_save_dir(self):
        while True:
            save_dir=askdirectory(title = "选择一个图片保存目录", initialdir='./', mustexist = True)
            if save_dir:
                self.entry_savelocation_var.set(save_dir)
                break
            else:
                messagebox.showwarning('警告','请选择图片保存的文件夹！')


    def open_dir_after_crawl(self):
        #图片爬取结束后，打开文件夹
        if self.open_dir_var.get()==1:
            self.open_dir_flag=True
        else:
            pass

    def insert_into_scrolltext(self,line):
        self.scrolltext_state.insert(END,line+'\n')
        self.scrolltext_state.yview_moveto(1)

    def quit_window(self,*args):
        ret=messagebox.askyesno('退出','确定要退出？')
        if ret :
            self.root.destroy()
        else:
            pass

    def thread_it(self,func,*args):
        t=threading.Thread(target=func,args=args)
        t.setDaemon(True)
        t.start()

if __name__ == '__main__':
    a=App()



