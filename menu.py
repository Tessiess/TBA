import tkinter as tk
from tkinter import ttk,scrolledtext,INSERT,END
from TBA_cht import *
from threading import Thread
import sys
import os
import time

home_page = tk.Tk()
home_page.title('TBA-v0.0.1')
width = 800
height = 600
screen_width = home_page.winfo_screenwidth()
screen_heigth = home_page.winfo_screenheight()
home_page.minsize(width, height)
home_page.geometry('%ix%i+%i+%i' %
                   (width, height, (screen_width-width)//2, (screen_heigth-height)//2))
home_page.iconbitmap('./by_CoconutCorn.ico')

class Thread_with_trace(Thread): 
    def __init__(self, *args, **keywords): 
        Thread.__init__(self, *args, **keywords) 
        self.killed = False

    def start(self): 
        self.__run_backup = self.run 
        self.run = self.__run	 
        Thread.start(self) 

    def __run(self): 
        sys.settrace(self.globaltrace) 
        self.__run_backup() 
        self.run = self.__run_backup 

    def globaltrace(self, frame, event, arg): 
        if event == 'call': 
            return self.localtrace  
        else: 
            return None

    def localtrace(self, frame, event, arg): 
        if self.killed: 
            if event == 'line': 
                raise SystemExit() 
        return self.localtrace 

    def kill(self): 
        self.killed = True


class Home:
    def __init__(self):
        # 主页面
        self.home = tk.Frame(home_page, width=800, height=600, bg='white')
        self.home.pack()

        # 左栏
        self.list = tk.Frame(home_page, width=200,
                             height=360, bg='white', highlightthickness=1, highlightbackground='black')
        self.list.place(relx=0.05, rely=0.12)

        # 左栏组件
        self.iv_start = tk.IntVar()
        self.iv_lesson = tk.IntVar()
        self.iv_club = tk.IntVar()
        self.iv_cafe = tk.IntVar()
        self.iv_crafting = tk.IntVar()
        self.iv_shop = tk.IntVar()
        self.iv_campaign = tk.IntVar()
        self.cb_start = tk.Checkbutton(
            self.list, bg='white', onvalue=1, offvalue=0, variable=self.iv_start)
        self.cb_lesson = tk.Checkbutton(
            self.list, bg='white', onvalue=1, offvalue=0, variable=self.iv_lesson)
        self.cb_club = tk.Checkbutton(
            self.list, bg='white', onvalue=1, offvalue=0, variable=self.iv_club)
        self.cb_cafe = tk.Checkbutton(
            self.list, bg='white', onvalue=1, offvalue=0, variable=self.iv_cafe)
        self.cb_crafting = tk.Checkbutton(
            self.list, bg='white', onvalue=1, offvalue=0, variable=self.iv_crafting)
        self.cb_shop = tk.Checkbutton(
            self.list, bg='white', onvalue=1, offvalue=0, variable=self.iv_shop)
        self.cb_campaign = tk.Checkbutton(
            self.list, bg='white', onvalue=1, offvalue=0, variable=self.iv_campaign)

        b_start = tk.Button(self.list, text='开始唤醒', width=17,
                            height=1, font=('黑体'), anchor='w', command=self.show_start, relief='groove', bd=0,  bg='white')
        b_lesson = tk.Button(self.list, text='课程表', width=17,
                             height=1, font=('黑体'), anchor='w', command=self.show_lesson, relief='groove', bd=0, bg='white')
        b_club = tk.Button(self.list, text='社团', width=17,
                           height=1, font=('黑体'), anchor='w', command=self.show_club, relief='groove', bd=0,  bg='white')
        b_cafe = tk.Button(self.list, text='咖啡厅', width=17,
                           height=1, font=('黑体'), anchor='w', command=self.show_cafe, relief='groove', bd=0,  bg='white')
        b_crafting = tk.Button(self.list, text='制造', width=17, height=1, font=(
            '黑体'), anchor='w', command=self.show_crafting, relief='groove', bd=0,  bg='white')
        b_shop = tk.Button(self.list, text='商店', width=17,
                           height=1, font=('黑体'), anchor='w', command=self.show_shop, relief='groove', bd=0,  bg='white')
        b_campaign = tk.Button(self.list, text='清体力', width=17, height=1, font=(
            '黑体'), anchor='w', command=self.show_campaign, relief='groove', bd=0,  bg='white')
        b_mission=tk.Button(self.list, text='自动开荒活动', width=17, height=1, font=(
            '黑体'), anchor='w', command=self.show_mission, relief='groove', bd=0,  bg='white')

        b_all = tk.Button(self.list, text='全选', width=7,
                          height=1, font=('黑体'), command=self.all, bg='white', bd=1)
        b_clear = tk.Button(self.list, text='清空', width=7,
                            height=1, font=('黑体'), command=self.clear, bg='white', bd=1)
        
        self.sc_text=scrolledtext.ScrolledText(home_page, width=26,
                             height=22,wrap=tk.WORD, bg='white',font=('微软雅黑'))
        self.sc_text['state'] ='disabled'
        self.sc_text.tag_config('red',foreground='red')
        self.sc_text.tag_config('black',foreground='black')
        self.sc_text.place(relx=0.65, rely=0.12)

        
        # 运行组件
        self.sv_run=tk.StringVar()
        self.sv_run.set('开始执行')
        self.b_run = tk.Button(self.home, textvariable=self.sv_run,
                          width=14, height=3, font=('黑体'), command=self.thread_run, bg='white', bd=1)
        
        self.loading()

        # 排版
        b_start.place(relx=0.18, rely=0.05)
        self.cb_start.place(relx=0.08, rely=0.05)
        b_cafe.place(relx=0.18, rely=0.13)
        self.cb_cafe.place(relx=0.08, rely=0.13)
        b_lesson.place(relx=0.18, rely=0.21)
        self.cb_lesson.place(relx=0.08, rely=0.21)
        b_club.place(relx=0.18, rely=0.29)
        self.cb_club.place(relx=0.08, rely=0.29)
        b_crafting.place(relx=0.18, rely=0.37)
        self.cb_crafting.place(relx=0.08, rely=0.37)
        b_campaign.place(relx=0.18, rely=0.45)
        self.cb_campaign.place(relx=0.08, rely=0.45)
        b_shop.place(relx=0.18, rely=0.53)
        self.cb_shop.place(relx=0.08, rely=0.53)
        b_mission.place(relx=0.18,rely=0.61)
        b_all.place(relx=0.1, rely=0.88)
        b_clear.place(relx=0.55, rely=0.88)
        self.b_run.place(relx=0.1, rely=0.82)

        # 计数元件
        self.cnt=0


    def insert_text(self,tt,tag='black'):
        self.sc_text['state'] ='normal' 
        self.sc_text.insert(tk.INSERT,time.strftime('%m-%d %H:%M:%S ', time.localtime())+tt+'\n',tag)
        self.sc_text.see(tk.END)
        self.sc_text['state'] ='disabled'


    def show_start(self):
        self.destory_menu()
        if self.iv_start.get():
            self.cb_start.deselect()
        else:
            self.cb_start.select()
        self.stm=Start_menu()

    def show_lesson(self):
        self.destory_menu()
        if self.iv_lesson.get():
            self.cb_lesson.deselect()
        else:
            self.cb_lesson.select()
        self.lem=Lesson_menu()

    def show_club(self):
        self.destory_menu()
        if self.iv_club.get():
            self.cb_club.deselect()
        else:
            self.cb_club.select()
        self.clm=Club_menu()

    def show_cafe(self):
        self.destory_menu()
        if self.iv_cafe.get():
            self.cb_cafe.deselect()
        else:
            self.cb_cafe.select()
        self.cam=Cafe_menu()

    def show_crafting(self):
        self.destory_menu()
        if self.iv_crafting.get():
            self.cb_crafting.deselect()
        else:
            self.cb_crafting.select()
        self.crm=Crafting_menu()

    def show_shop(self):
        self.destory_menu()
        if self.iv_shop.get():
            self.cb_shop.deselect()
        else:
            self.cb_shop.select()
        self.shm=Shop_menu()

    def show_campaign(self):
        self.destory_menu()
        if self.iv_campaign.get():
            self.cb_campaign.deselect()
        else:
            self.cb_campaign.select()
        self.camm=Campaign_menu()

    def show_mission(self):
        self.destory_menu()
        Mission_menu()
        

    def all(self):
        self.cb_start.select()
        self.cb_lesson.select()
        self.cb_club.select()
        self.cb_cafe.select()
        self.cb_crafting.select()
        self.cb_shop.select()
        self.cb_campaign.select()

    def clear(self):
        self.cb_start.deselect()
        self.cb_lesson.deselect()
        self.cb_club.deselect()
        self.cb_cafe.deselect()
        self.cb_crafting.deselect()
        self.cb_shop.deselect()
        self.cb_campaign.deselect()

    def thread_run(self):
        self.tr_run=Thread_with_trace(target=self.run)
        self.tr_run.start()

    def run(self):
        self.sc_text['state'] ='normal' 
        self.sc_text.delete('1.0',tk.END)
        self.sc_text['state'] ='disabled'

        self.insert_text('开始执行任务')
        self.save()
        self.sv_run.set('中止任务')
        self.b_run['command']=self.stop

        self.insert_text('开始连接模拟器')
        if not self.cnt:
            with open('database/start.txt', "rb") as f:
                me = f.readlines()
            os.system('adb kill-server')
            os.system("adb devices")
            # 模拟器类型
            os.system("adb connect %s" % str(me[3],encoding='utf-8').replace('\n',''))  # 7555/16384
            self.insert_text('连接完成')
            self.cnt+=1
        else:
            self.insert_text('模拟器已连接')

        if self.iv_start.get():
            self.insert_text('任务：开始唤醒')
            try:
                self.stm.run()
            except:
                self.destory_menu()
                self.stm=Start_menu()
                self.stm.run()
            self.insert_text('开始唤醒 完成')
        if self.iv_cafe.get():
            self.insert_text('任务：咖啡厅')
            try:
                self.cam.run()
            except:
                self.destory_menu()
                self.cam=Cafe_menu()
                self.cam.run()
            self.insert_text('咖啡厅 完成')
        if self.iv_lesson.get():
            self.insert_text('任务：课程表')
            try:
                self.lem.run()
            except:
                self.destory_menu()
                self.lem=Lesson_menu()
                self.lem.run()
            self.insert_text('课程表 完成')
        if self.iv_club.get():
            self.insert_text('任务：社团')
            try:
                self.clm.run()
            except:
                self.destory_menu()
                self.clm=Club_menu()
                self.clm.run()
            self.insert_text('社团 完成')
        if self.iv_crafting.get():
            self.insert_text('任务：制造')
            try:
                self.crm.run()
            except:
                self.destory_menu()
                self.crm=Crafting_menu()
                self.crm.run()
            self.insert_text('制造 完成')
        if self.iv_campaign.get():
            self.insert_text('任务：清体力')
            try:
                self.camm.run()
            except:
                self.destory_menu()
                self.camm=Campaign_menu()
                self.camm.run()
            self.insert_text('清体力 完成')
        if self.iv_shop.get():
            self.insert_text('任务：商店')
            try:
                self.shm.run()
            except:
                self.destory_menu()
                self.shm=Shop_menu()
                self.shm.run()
            self.insert_text('商店 完成')
        self.insert_text('所有任务完成')

        self.sv_run.set('开始执行')
        self.b_run['command']=self.thread_run

    def destory_menu(self):
        try:
            if self.stm.menu:
                self.stm.menu.destroy()
        except:
            pass
        try:
            if self.cam.menu:
                self.cam.menu.destroy()
        except:
            pass
        try:
            if self.lem.menu:
                self.lem.menu.destroy()
        except:
            pass
        try:
            if self.clm.menu:
                self.clm.menu.destroy()
        except:
            pass
        try:
            if self.crm.menu:
                self.crm.menu.destroy()
        except:
            pass
        try:
            if self.camm.menu:
                self.camm.menu.destroy()
        except:
            pass
        try:
            if self.shm.menu:
                self.shm.menu.destroy()
        except:
            pass


    def stop(self):
        self.sv_run.set('开始执行')
        self.b_run['command']=self.thread_run

        self.tr_run.kill()
        self.tr_run.join()
        if not self.tr_run.is_alive():
            self.insert_text('已成功中止运行')

    def save(self):
        try:
            message=''
            message+='%s\n' % self.iv_start.get()
            message+='%s\n' % self.iv_cafe.get()
            message+='%s\n' % self.iv_lesson.get()
            message+='%s\n' % self.iv_club.get()
            message+='%s\n' % self.iv_crafting.get()
            message+='%s\n' % self.iv_shop.get()
            message+='%s' % self.iv_campaign.get()
            with open('database/setting.txt', "bw") as f:
                f.write(message.encode(encoding='utf-8'))
            self.insert_text('已默认保存选择')
        except:
            pass

    def loading(self):
        try:
            with open('database/setting.txt', "rb") as f:
                me = f.readlines()
            if int(me[0]):
                self.cb_start.select()
            if int(me[1]):
                self.cb_cafe.select()
            if int(me[2]):
                self.cb_lesson.select()
            if int(me[3]):
                self.cb_club.select()
            if int(me[4]):
                self.cb_crafting.select()
            if int(me[5]):
                self.cb_shop.select()
            if int(me[6]):
                self.cb_campaign.select()
        except:
            pass    
        

class Start_menu:
    def __init__(self):
        self.menu = tk.Frame(home_page, width=220,
                             height=360, bg='white')
        self.menu.place(relx=0.35, rely=0.12)
        l_length=tk.Label(self.menu,text='模拟器长度：',font=('黑体'),bg='white')
        l_width=tk.Label(self.menu,text='模拟器宽度：',font=('黑体'),bg='white')
        self.e_length=tk.Entry(self.menu,width=8,bg='#FCFCFC')
        self.e_width=tk.Entry(self.menu,width=8,bg='#FCFCFC')
        # b_knowxy=tk.Button(self.menu,text='自动获取模拟器大小',font=('黑体'),bg='white',command=self.knowxy, bd=1,height=1)
        l_net=tk.Label(self.menu,text='谷歌商店连接状况：',font=('黑体'),bg='white')
        self.c_net=ttk.Combobox(self.menu,values=('连接良好，商店正常','连接不良，主页会弹窗'),font=('黑体'))
        l_address=tk.Label(self.menu,text='连接地址：',font=('黑体'),bg='white')
        self.e_address=tk.Entry(self.menu,width=26,bg='#FCFCFC')
        b_save=tk.Button(self.menu,text='保存设置',font=('黑体'),bg='white',command=self.save, bd=1,height=1)

        self.loading()
        
        l_length.place(relx=0,rely=0.05)
        self.e_length.place(relx=0.5,rely=0.05)
        l_width.place(relx=0,rely=0.12)
        self.e_width.place(relx=0.5,rely=0.12)
        # b_knowxy.place(rely=0.19)
        l_net.place(relx=0,rely=0.3)
        self.c_net.place(relx=0,rely=0.37)
        l_address.place(relx=0,rely=0.47)
        self.e_address.place(relx=0,rely=0.54)
        b_save.place(relx=0.65,rely=0.9)



    def knowxy(self):
        try:
            with open('database/start.txt', "rb") as f:
                me = f.readlines()
            os.system('adb kill-server')
            os.system("adb devices")
            os.system("adb connect 127.0.0.1:%i" % int(me[3]))
            (x,y)=know_xy()
            self.e_length.insert(0,x)
            self.e_width.insert(0,y)
        except:
            h.insert_text('连接模拟器失败，建议先选择mumu版本，保存后再自动识别','red')
            pass


    def save(self):
        try:
            if not self.e_length.get() or not self.e_width.get():
                h.insert_text('模拟器大小为空','red')
                raise Exception()
            message='%s\n%s\n' % (self.e_length.get(),self.e_width.get())
            if self.c_net.get()=='连接良好，商店正常':
                message+='good\n'
            elif self.c_net.get()=='连接不良，主页会弹窗':
                message+='bad\n'
            else:
                h.insert_text('未选择谷歌商店连接情况/删减了部分字','red')
                raise Exception()
            if self.e_address.get():
                message+='%s' % self.e_address.get()
            else:
                h.insert_text('未输入连接地址','red')
                raise Exception()
            with open('database/start.txt', "bw") as f:
                f.write(message.encode(encoding='utf-8'))
                h.insert_text('如果修改了模拟器大小，需要重启软件才生效','red')
        except:
            h.insert_text('保存有误','red')


    def loading(self):
        try:
            with open('database/start.txt', "rb") as f:
                me = f.readlines()
            self.e_length.insert(0,str(me[0],encoding='utf-8').replace('\n',''))
            self.e_width.insert(0,str(me[1],encoding='utf-8').replace('\n',''))
            if str(me[2],encoding='utf-8').replace('\n','')=='good':
                self.c_net.current(0)
            else:
                self.c_net.current(1)
            self.e_address.insert(0,str(me[3],encoding='utf-8').replace('\n',''))
        except:
            pass   

    def run(self):
        s=Sta()
        h.insert_text('开始打开ba')
        s.open()
        h.insert_text('唤醒并签到')
        s.touch()
        s.dlc()
        is_main()


class Lesson_menu:
    def __init__(self):
        self.menu=tk.Frame(home_page, width=230,
                             height=360, bg='white')
        self.menu.place(relx=0.35, rely=0.12)
        l_ticket=tk.Label(self.menu,text='课程表票券数量：',font=('黑体'),bg='white',height=1)
        self.e_ticket=tk.Entry(self.menu,width=8,bg='#FCFCFC')
        self.iv_1 = tk.IntVar()
        self.cb_1 = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_1,text='办公室',font=('黑体'),height=1)
        self.iv_2 = tk.IntVar()
        self.cb_2 = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_2,text='居住区',font=('黑体'),height=1)
        self.iv_3 = tk.IntVar()
        self.cb_3 = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_3,text='格黑娜',font=('黑体'),height=1)
        self.iv_4 = tk.IntVar()
        self.cb_4 = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_4,text='阿拜多斯',font=('黑体'),height=1)
        self.iv_5 = tk.IntVar()
        self.cb_5 = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_5,text='千年',font=('黑体'),height=1)
        self.iv_6 = tk.IntVar()
        self.cb_6 = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_6,text='三一',font=('黑体'),height=1)
        self.iv_7 = tk.IntVar()
        self.cb_7 = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_7,text='赤冬',font=('黑体'),height=1)
        self.iv_8 = tk.IntVar()
        self.cb_8 = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_8,text='百鬼',font=('黑体'),height=1)
        self.iv_9 = tk.IntVar()
        self.cb_9 = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_9,text='白鸟区',font=('黑体'),height=1)
        self.iv_1c=[tk.IntVar() for _ in range(7)]
        self.iv_2c=[tk.IntVar() for _ in range(7)]
        self.iv_3c=[tk.IntVar() for _ in range(8)]
        self.iv_4c=[tk.IntVar() for _ in range(8)]
        self.iv_5c=[tk.IntVar() for _ in range(8)]
        self.iv_6c=[tk.IntVar() for _ in range(8)]
        self.iv_7c=[tk.IntVar() for _ in range(8)]
        self.iv_8c=[tk.IntVar() for _ in range(8)]
        self.iv_9c=[tk.IntVar() for _ in range(8)]
        self.cb_1c = [tk.Checkbutton(self.menu,variable=self.iv_1c[i], onvalue=1, offvalue=0) for i in range(7)]
        self.cb_2c = [tk.Checkbutton(self.menu,variable=self.iv_2c[i], onvalue=1, offvalue=0) for i in range(7)]
        self.cb_3c = [tk.Checkbutton(self.menu,variable=self.iv_3c[i], onvalue=1, offvalue=0) for i in range(8)]
        self.cb_4c = [tk.Checkbutton(self.menu,variable=self.iv_4c[i], onvalue=1, offvalue=0) for i in range(8)]
        self.cb_5c = [tk.Checkbutton(self.menu,variable=self.iv_5c[i], onvalue=1, offvalue=0) for i in range(8)]
        self.cb_6c = [tk.Checkbutton(self.menu,variable=self.iv_6c[i], onvalue=1, offvalue=0) for i in range(8)]
        self.cb_7c = [tk.Checkbutton(self.menu,variable=self.iv_7c[i], onvalue=1, offvalue=0) for i in range(8)]
        self.cb_8c = [tk.Checkbutton(self.menu,variable=self.iv_8c[i], onvalue=1, offvalue=0) for i in range(8)]
        self.cb_9c = [tk.Checkbutton(self.menu,variable=self.iv_9c[i], onvalue=1, offvalue=0) for i in range(8)]
        self.col(self.cb_1c,7)
        self.col(self.cb_2c,7)
        self.col(self.cb_3c,8)
        self.col(self.cb_4c,8)
        self.col(self.cb_5c,8)
        self.col(self.cb_6c,8)
        self.col(self.cb_7c,8)
        self.col(self.cb_8c,8)
        self.col(self.cb_9c,8)
        l_tips=tk.Label(self.menu,text='(打钩表示刷取，颜色表示产物品质)',font=('黑体',10),bg='white',height=1)

        self.loading()

        l_ticket.place(relx=0,rely=0.05)
        self.e_ticket.place(relx=0.7,rely=0.05)
        self.cb_1.place(relx=-0.02,rely=0.15)
        self.pla(self.cb_1c,7,0.15)
        self.cb_2.place(relx=-0.02,rely=0.22)
        self.pla(self.cb_2c,7,0.22)
        self.cb_3.place(relx=-0.02,rely=0.29)
        self.pla(self.cb_3c,8,0.29)
        self.cb_4.place(relx=-0.02,rely=0.36)
        self.pla(self.cb_4c,8,0.36)
        self.cb_5.place(relx=-0.02,rely=0.43)
        self.pla(self.cb_5c,8,0.43)
        self.cb_6.place(relx=-0.02,rely=0.5)
        self.pla(self.cb_6c,8,0.5)
        self.cb_7.place(relx=-0.02,rely=0.57)
        self.pla(self.cb_7c,8,0.57)
        self.cb_8.place(relx=-0.02,rely=0.64)
        self.pla(self.cb_8c,8,0.64)
        self.cb_9.place(relx=-0.02,rely=0.71)
        self.pla(self.cb_9c,8,0.71)
        l_tips.place(relx=0,rely=0.8)

        b_save=tk.Button(self.menu,text='保存设置',font=('黑体'),bg='white',command=self.save, bd=1)
        
        b_save.place(relx=0.621739,rely=0.9)
        
    def pla(self,l,n,y):
        for i in range(n):
            l[i].place(relx=0.36+0.08*i,rely=y)

    def col(self,l,n):
        l[0]["bg"]='#FCFCFC'
        l[1]["bg"]='#FCFCFC'
        l[2]["bg"]='#3282F6'
        l[3]["bg"]='#3282F6'
        l[4]["bg"]='#FFFE91'
        l[5]["bg"]='#FFFE91'
        l[6]["bg"]='#7E84F7'
        if n==8:
            l[7]["bg"]='#7E84F7'

    def save(self):
        try:
            message=''
            if self.e_ticket.get():
               message+='%s\n' % self.e_ticket.get()
            else:
                h.insert_text('课程表票券未输入','red')
                raise Exception()
            message+='%s %s %s %s %s %s %s %s\n' % (self.iv_1.get(),self.iv_1c[0].get(),self.iv_1c[1].get(),self.iv_1c[2].get(),self.iv_1c[3].get(),self.iv_1c[4].get(),self.iv_1c[5].get(),self.iv_1c[6].get())
            message+='%s %s %s %s %s %s %s %s\n' % (self.iv_2.get(),self.iv_2c[0].get(),self.iv_2c[1].get(),self.iv_2c[2].get(),self.iv_2c[3].get(),self.iv_2c[4].get(),self.iv_2c[5].get(),self.iv_2c[6].get())
            message+='%s %s %s %s %s %s %s %s %s\n' % (self.iv_3.get(),self.iv_3c[0].get(),self.iv_3c[1].get(),self.iv_3c[2].get(),self.iv_3c[3].get(),self.iv_3c[4].get(),self.iv_3c[5].get(),self.iv_3c[6].get(),self.iv_3c[7].get())
            message+='%s %s %s %s %s %s %s %s %s\n' % (self.iv_4.get(),self.iv_4c[0].get(),self.iv_4c[1].get(),self.iv_4c[2].get(),self.iv_4c[3].get(),self.iv_4c[4].get(),self.iv_4c[5].get(),self.iv_4c[6].get(),self.iv_4c[7].get())
            message+='%s %s %s %s %s %s %s %s %s\n' % (self.iv_5.get(),self.iv_5c[0].get(),self.iv_5c[1].get(),self.iv_5c[2].get(),self.iv_5c[3].get(),self.iv_5c[4].get(),self.iv_5c[5].get(),self.iv_5c[6].get(),self.iv_5c[7].get())
            message+='%s %s %s %s %s %s %s %s %s\n' % (self.iv_6.get(),self.iv_6c[0].get(),self.iv_6c[1].get(),self.iv_6c[2].get(),self.iv_6c[3].get(),self.iv_6c[4].get(),self.iv_6c[5].get(),self.iv_6c[6].get(),self.iv_6c[7].get())
            message+='%s %s %s %s %s %s %s %s %s\n' % (self.iv_7.get(),self.iv_7c[0].get(),self.iv_7c[1].get(),self.iv_7c[2].get(),self.iv_7c[3].get(),self.iv_7c[4].get(),self.iv_7c[5].get(),self.iv_7c[6].get(),self.iv_7c[7].get())
            message+='%s %s %s %s %s %s %s %s %s\n' % (self.iv_8.get(),self.iv_8c[0].get(),self.iv_8c[1].get(),self.iv_8c[2].get(),self.iv_8c[3].get(),self.iv_8c[4].get(),self.iv_8c[5].get(),self.iv_8c[6].get(),self.iv_8c[7].get())
            message+='%s %s %s %s %s %s %s %s %s' % (self.iv_9.get(),self.iv_9c[0].get(),self.iv_9c[1].get(),self.iv_9c[2].get(),self.iv_9c[3].get(),self.iv_9c[4].get(),self.iv_9c[5].get(),self.iv_9c[6].get(),self.iv_9c[7].get())
            with open('database/lesson.txt', "bw") as f:
                f.write(message.encode(encoding='utf-8'))
        except:
             h.insert_text('保存有误','red')
        
    def loading(self):
        try:
            with open('database/lesson.txt', "rb") as f:
                me = f.readlines()
            self.e_ticket.insert(0,int(me[0]))
            l1=[self.cb_1,self.cb_2,self.cb_3,self.cb_4,self.cb_5,self.cb_6,self.cb_7,self.cb_8,self.cb_9]
            l2=[self.cb_1c,self.cb_2c,self.cb_3c,self.cb_4c,self.cb_5c,self.cb_6c,self.cb_7c,self.cb_8c,self.cb_9c]
            for i in range(9):
                tmp=list(map(int,str(me[i+1],encoding='utf-8').replace('\n','').split(' ')))
                for j in range(len(tmp)):
                    if j==0 and tmp[0]:
                        l1[i].select()
                    if j>0 and tmp[j]:
                        l2[i][j-1].select()
        except:
            pass   

    def run(self):
        with open('database/lesson.txt', "rb") as f:
            me = f.readlines()
        tickets=int(me[0])
        tables=[]
        for i in range(9):
            tmp=list(map(int,str(me[i+1],encoding='utf-8').replace('\n','').split(' ')))
            tables.append(tmp)
        l=Les(tables, tickets)
        l.run()


class Club_menu:
    def __init__(self):
        self.menu=tk.Frame(home_page, width=220,
                             height=360, bg='white')
        self.menu.place(relx=0.35, rely=0.12)
        l=tk.Label(self.menu,text='还没想好这样页面\n有什么可选功能qwq',font=('黑体'),bg='white')
        l.place(relx=0,rely=0.05)

    def run(self):
        c=Clu()
        c.enter()
        is_main()
        c.mailbox()
        is_main()


class Cafe_menu:
    def __init__(self):
        self.menu = tk.Frame(home_page, width=220,
                             height=360, bg='white')
        self.menu.place(relx=0.35, rely=0.12)
        self.iv_invite = tk.IntVar()
        self.cb_invite = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_invite,text='选择邀请策略：',font=('黑体'),height=1)
        self.c_invite=ttk.Combobox(self.menu,values=('好感度最低的','好感度最高的'),font=('黑体'))

        b_save=tk.Button(self.menu,text='保存设置',font=('黑体'),bg='white',command=self.save, bd=1,height=1)

        self.loading()
        

        self.cb_invite.place(relx=0,rely=0.05)
        self.c_invite.place(relx=0,rely=0.14)

        b_save.place(relx=0.65,rely=0.9)


    def run(self):
        with open('database/cafe.txt', "rb") as f:
            me = f.readlines()
        c=Caf(str(me[0],encoding='utf-8').replace('\n',''),str(me[1],encoding='utf-8').replace('\n',''))
        c.enter()
        if c.invite_:
            if c.invite():
                h.insert_text('邀请cd未好','red')
            else:
                if c.method=='min':
                    h.insert_text('邀请的策略为好感度最低的')
                else:
                    h.insert_text('邀请的策略为好感度最高的')
        # touch
        c.get_AP()
        c.leave()
        is_main()

    def loading(self):
        try:
            with open('database/cafe.txt', "rb") as f:
                me = f.readlines()
            if str(me[0],encoding='utf-8').replace('\n',''):
                self.cb_invite.select()
            if str(me[1],encoding='utf-8').replace('\n','')=='min':
                self.c_invite.current(0)
            else:
                self.c_invite.current(1)
        except:
            pass   

    def save(self):
        try:
            if not self.c_invite.get():
                h.insert_text('邀请选择策略为空','red')
                raise Exception()
            if self.c_invite.get() and not self.iv_invite.get():
                h.insert_text('未勾选邀请选项','red')
            message=''
            message+='%s\n' % self.iv_invite.get()
            if self.c_invite.get()=='好感度最低的':
                message+='min'
            elif self.c_invite.get()=='好感度最高的':
                message+='max'
            else:
                h.insert_text('未选择邀请方式/删减了部分字','red')
                raise Exception()
            with open('database/cafe.txt', "bw") as f:
                f.write(message.encode(encoding='utf-8'))
        except:
            h.insert_text('保存有误','red')


class Crafting_menu:
    def __init__(self):
        self.menu = tk.Frame(home_page, width=220,
                             height=360, bg='white')
        self.menu.place(relx=0.35, rely=0.12)
        l_stone=tk.Label(self.menu,text='选择启动石类型：',font=('黑体'),bg='white')
        self.c_stone=ttk.Combobox(self.menu,values=('启动石','启动石碎片'),font=('黑体'))
        l_num=tk.Label(self.menu,text='一次制造追加几次：(制造直到格子满)',font=('黑体'),bg='white')
        self.c_num=ttk.Combobox(self.menu,values=('0次(消耗1个启动石)','1次(消耗3个启动石)'),font=('黑体'))
        l_method=tk.Label(self.menu,text='选择制造策略：',font=('黑体'),bg='white')
        self.c_method=ttk.Combobox(self.menu,values=('优先产出礼物','优先产出彩素材(包含金色家具)'),font=('黑体'))

        b_save=tk.Button(self.menu,text='保存设置',font=('黑体'),bg='white',command=self.save, bd=1,height=1)
        
        self.loading()

        l_stone.place(relx=0,rely=0.05)
        self.c_stone.place(relx=0,rely=0.12)
        l_num.place(relx=0,rely=0.22)
        self.c_num.place(relx=0,rely=0.29)
        l_method.place(relx=0,rely=0.39)
        self.c_method.place(relx=0,rely=0.46)

        b_save.place(relx=0.65,rely=0.9)


    def save(self):
        try:
            message=''
            if self.c_stone.get()=='启动石':
                message+='stone1\n'
            elif self.c_stone.get()=='启动石碎片':
                message+='stone2\n'
            else:
                h.insert_text('未选择启动石策略/删减了部分字','red')
                raise Exception()
            if self.c_num.get()=='0次(消耗1个启动石)':
                message+='1\n'
            elif self.c_num.get()=='1次(消耗3个启动石)':
                message+='2\n'
            else:
                h.insert_text('未选择制造次数/删减了部分字','red')
                raise Exception()
            if self.c_method.get()=='优先产出礼物':
                message+='flo,rad'
            elif self.c_method.get()=='优先产出彩素材(包含金色家具)':
                message+='rad,flo'
            else:
                h.insert_text('未选择制造策略/删减了部分字','red')
                raise Exception()
            with open('database/crafting.txt', "bw") as f:
                f.write(message.encode(encoding='utf-8'))
        except:
            h.insert_text('保存有误','red')

    def loading(self):
        try:
            with open('database/crafting.txt', "rb") as f:
                me = f.readlines()
            if str(me[0],encoding='utf-8').replace('\n','')=='stone1':
                self.c_stone.current(0)
            else:
                self.c_stone.current(1)
            if str(me[1],encoding='utf-8').replace('\n','')=='1':
                self.c_num.current(0)
            else:
                self.c_num.current(1)
            if str(me[2],encoding='utf-8').replace('\n','')=='flo,rad':
                self.c_method.current(0)
            else:
                self.c_method.current(1)
        except:
            pass   


    def run(self):
        with open('database/crafting.txt', "rb") as f:
            me = f.readlines()
        stone_type,num,method=str(me[0],encoding='utf-8').replace('\n',''),str(me[1],encoding='utf-8').replace('\n',''),str(me[2],encoding='utf-8').replace('\n','')
        c=Cra(stone_type, num, method)
        c.enter()
        c.speed_up()
        c.receive()
        h.insert_text('已经全部收取')
        c.create()
        h.insert_text('已经制造完成')
        c.leave()
        is_main()


class Shop_menu:
    def __init__(self):
        self.menu = tk.Frame(home_page, width=220,
                             height=360, bg='white')
        self.menu.place(relx=0.35, rely=0.12)
        self.iv_normal = tk.IntVar()
        self.cb_normal = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_normal,text='信用货币商店：',font=('黑体'),height=1)
        self.iv_exp = tk.IntVar()
        self.cb_exp = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_exp,text='狗粮',font=('黑体'),height=1)
        self.iv_stone = tk.IntVar()
        self.cb_stone = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_stone,text='强化石',font=('黑体'),height=1)
        self.iv_opz = tk.IntVar()
        self.cb_opz = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_opz,text='材料',font=('黑体'),height=1)
        self.iv_ap = tk.IntVar()
        self.cb_ap = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_ap,text='购买体力次数：',font=('黑体'),height=1)
        self.c_ap=ttk.Combobox(self.menu,values=('0','1','2','3','4'),font=('黑体'))

        b_save=tk.Button(self.menu,text='保存设置',font=('黑体'),bg='white',command=self.save, bd=1,height=1)

        self.loading()
        
        self.cb_normal.place(relx=0,rely=0.05)
        self.cb_exp.place(relx=0.1,rely=0.12)
        self.cb_stone.place(relx=0.1,rely=0.19)
        self.cb_opz.place(relx=0.1,rely=0.26)
        self.cb_ap.place(relx=0,rely=0.36)
        self.c_ap.place(relx=0,rely=0.44)

        b_save.place(relx=0.65,rely=0.9)


    def save(self):
        try:
            message=''
            message+='%s\n' % self.iv_normal.get()
            message+='%s\n' % self.iv_exp.get()
            message+='%s\n' % self.iv_stone.get()
            message+='%s\n' % self.iv_opz.get()
            message+='%s\n' % self.iv_ap.get()
            if self.iv_ap.get() and self.c_ap.get() in ['0','1','2','3','4']:
                message+='%s' % self.c_ap.get()
            elif not self.iv_ap.get():
                message+='0'
            else:
                h.insert_text('未选择购买ap次数/删减了部分字','red')
                raise Exception()
            with open('database/shop.txt', "bw") as f:
                f.write(message.encode(encoding='utf-8'))
        except:
            h.insert_text('保存有误','red')

    def loading(self):
        try:
            with open('database/shop.txt', "rb") as f:
                me = f.readlines()
            if int(me[0]):
                self.cb_normal.select()
            if int(me[1]):
                self.cb_exp.select()
            if int(me[2]):
                self.cb_stone.select()
            if int(me[3]):
                self.cb_opz.select()
            if int(me[4]):
                self.cb_ap.select()
            self.c_ap.current(int(me[5]))
        except:
            pass   

    def run(self):
        with open('database/shop.txt', "rb") as f:
            me = f.readlines()
        normal,exp,stone,opz,ap,ap_num=int(me[0]),int(me[1]),int(me[2]),int(me[3]),int(me[4]),int(me[5])
        tasks_normal=[]
        ss=''
        if exp:
            ss+='狗粮'
            tasks_normal.append('報告')
        if stone:
            ss+='强化石'
            tasks_normal.append('強化石')
        if opz:
            ss+='材料'
            tasks_normal.extend(['碎', '曼陀羅',
                '書', '粉', '鐵', '破', '毀損'])
        if len(ss)>4:
            ss.insert(4,'\n                       ')
        s=Sho(tasks_normal, ap_num, normal, ap)
        s.enter()
        if s.normal_:
            s.normal()
            h.insert_text('已购买 %s' % ss)
        if s.ap_:
            s.ap()
            h.insert_text('已购买%i次体力' % s.num_ap)
        s.leave()
        is_main()
        

class Campaign_menu:
    def __init__(self):
        self.menu = tk.Frame(home_page, width=220,
                             height=360, bg='white')
        self.menu.place(relx=0.35, rely=0.12)
        self.iv_jjc = tk.IntVar()
        self.cb_jjc= tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_jjc,text='竞技场',font=('黑体'),height=1)
        
        l_example=tk.Label(self.menu,text='关卡名：',font=('黑体'),bg='white')
        self.e_example=tk.Entry(self.menu,width=8,bg='#FCFCFC')
        self.e_example.insert(0,'扫荡次数')
        self.iv_example = tk.IntVar()
        cb_example = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_example,text='没有通关打√',height=1)

        self.iv_bou = tk.IntVar()
        self.cb_bou = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_bou,text='悬赏通缉：',font=('黑体'),height=1)
        l_overpass=tk.Label(self.menu,text='高架：',font=('黑体'),bg='white')
        self.e_overpass=tk.Entry(self.menu,width=8,bg='#FCFCFC')
        self.iv_overpass = tk.IntVar()
        self.cb_overpass = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_overpass)
        l_desert=tk.Label(self.menu,text='沙漠：',font=('黑体'),bg='white')
        self.e_desert=tk.Entry(self.menu,width=8,bg='#FCFCFC')
        self.iv_desert = tk.IntVar()
        self.cb_desert = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_desert)
        l_classroom=tk.Label(self.menu,text='教室：',font=('黑体'),bg='white')
        self.e_classroom=tk.Entry(self.menu,width=8,bg='#FCFCFC')
        self.iv_classroom = tk.IntVar()
        self.cb_classroom = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_classroom)
        
        self.iv_scr = tk.IntVar()
        self.cb_scr = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_scr,text='学院交流会：',font=('黑体'),height=1)
        l_31=tk.Label(self.menu,text='三一：',font=('黑体'),bg='white')
        self.e_31=tk.Entry(self.menu,width=8,bg='#FCFCFC')
        self.iv_31 = tk.IntVar()
        self.cb_31 = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_31)
        l_geh=tk.Label(self.menu,text='格黑娜：',font=('黑体'),bg='white')
        self.e_geh=tk.Entry(self.menu,width=8,bg='#FCFCFC')
        self.iv_geh = tk.IntVar()
        self.cb_geh = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_geh)
        l_1000s=tk.Label(self.menu,text='千年：',font=('黑体'),bg='white')
        self.e_1000s=tk.Entry(self.menu,width=8,bg='#FCFCFC')
        self.iv_1000s = tk.IntVar()
        self.cb_1000s = tk.Checkbutton(
            self.menu, bg='white', onvalue=1, offvalue=0, variable=self.iv_1000s)
        
        self.loading()
        

        self.cb_jjc.place(relx=0,rely=0.05)
        l_example.place(relx=0,rely=0.15)
        self.e_example.place(relx=0.3,rely=0.15)
        cb_example.place(relx=0.55,rely=0.14)
        self.cb_bou.place(relx=0,rely=0.24)
        l_overpass.place(relx=0,rely=0.32)
        self.e_overpass.place(relx=0.3,rely=0.32)
        self.cb_overpass.place(relx=0.55,rely=0.31)
        l_desert.place(relx=0,rely=0.39)
        self.e_desert.place(relx=0.3,rely=0.39)
        self.cb_desert.place(relx=0.55,rely=0.38)
        l_classroom.place(relx=0,rely=0.46)
        self.e_classroom.place(relx=0.3,rely=0.46)
        self.cb_classroom.place(relx=0.55,rely=0.45)
        self.cb_scr.place(relx=0,rely=0.55)
        l_31.place(relx=0,rely=0.63)
        self.e_31.place(relx=0.3,rely=0.63)
        self.cb_31.place(relx=0.55,rely=0.62)
        l_geh.place(relx=0,rely=0.7)
        self.e_geh.place(relx=0.3,rely=0.7)
        self.cb_geh.place(relx=0.55,rely=0.69)
        l_1000s.place(relx=0,rely=0.77)
        self.e_1000s.place(relx=0.3,rely=0.77)
        self.cb_1000s.place(relx=0.55,rely=0.76)

        b_save=tk.Button(self.menu,text='保存设置',font=('黑体'),bg='white',command=self.save, bd=1,height=1)
        
        b_save.place(relx=0.65,rely=0.9)


    def save(self):
        try:
            message=''
            message+='%s\n' % self.iv_jjc.get()
            if not self.e_overpass.get():
                self.e_overpass.insert(0,0)
            if not self.e_desert.get():
                self.e_desert.insert(0,0) 
            if not self.e_classroom.get():
                self.e_classroom.insert(0,0)
            if not self.e_31.get():
                self.e_31.insert(0,0)
            if not self.e_geh.get():
                self.e_geh.insert(0,0) 
            if not self.e_1000s.get():
                self.e_1000s.insert(0,0)
            message+='%s %s %s %s %s %s %s\n' % (self.iv_bou.get(),self.e_overpass.get(),self.e_desert.get(),self.e_classroom.get(),self.iv_overpass.get(),self.iv_desert.get(),self.iv_classroom.get())
            message+='%s %s %s %s %s %s %s' % (self.iv_scr.get(),self.e_31.get(),self.e_geh.get(),self.e_1000s.get(),self.iv_31.get(),self.iv_geh.get(),self.iv_1000s.get())
            with open('database/campaign.txt', "bw") as f:
                f.write(message.encode(encoding='utf-8'))
        except:
            h.insert_text('保存有误','red')


    def loading(self):
        try:
            with open('database/campaign.txt', "rb") as f:
                me = f.readlines()
            bou,scr=str(me[1],encoding='utf-8').replace('\n','').split(' '),str(me[2],encoding='utf-8').replace('\n','').split(' ')
            bounty=list(map(int,bou))
            scrimmage=list(map(int,scr))
            if int(me[0]):
                self.cb_jjc.select()
            self.e_overpass.insert(0,bounty[1])
            self.e_desert.insert(0,bounty[2])
            self.e_classroom.insert(0,bounty[3])
            self.e_31.insert(0,scrimmage[1])
            self.e_geh.insert(0,scrimmage[2])
            self.e_1000s.insert(0,scrimmage[3])
            if bounty[4]:
                self.cb_overpass.select()
            if bounty[5]:
                self.cb_desert.select()
            if bounty[6]:
                self.cb_classroom.select()
            if scrimmage[4]:
                self.cb_31.select()
            if scrimmage[5]:
                self.cb_geh.select()
            if scrimmage[6]:
                self.cb_1000s.select()
        except:
            pass  


    def run(self):
        with open('database/campaign.txt', "rb") as f:
            me = f.readlines()
        jjc,bou,scr=int(me[0]),str(me[1],encoding='utf-8').replace('\n','').split(' '),str(me[2],encoding='utf-8').replace('\n','').split(' ')
        bounty=list(map(int,bou))
        scrimmage=list(map(int,scr))
        c=Cam(jjc, bounty, scrimmage)
        c.enter()
        if c.jjc_:
            c.jjc()
            h.insert_text('已收取竞技场日\n                       常')
        if c.bounty[0]:
           c.bou()
           h.insert_text('高架:沙漠:教室\n                       =%i:%i:%i' % (c.bounty[1],c.bounty[2],c.bounty[3]))
        if c.scrimmage[0]:
            c.scr()
            h.insert_text('31:格黑娜:千年\n                       =%i:%i:%i' % (c.scrimmage[1],c.scrimmage[2],c.scrimmage[3]))
        c.leave()
        is_main()


class Mission_menu:
    def __init__(self):
        self.menu = tk.Frame(home_page, width=220,
                             height=360, bg='white')
        self.menu.place(relx=0.35, rely=0.12)
        l_readme=tk.Label(self.menu,text='注意：请将游戏页面跳转到需\n要刷取的活动页面，即页面右\n列含有“入场”按钮的      ',font=('黑体'),bg='white')
        l_num=tk.Label(self.menu,text='开荒新关卡次数：',font=('黑体'),bg='white')
        self.e_num=tk.Entry(self.menu,width=8,bg='#FCFCFC')

        self.sv_run=tk.StringVar()
        self.sv_run.set('开始执行')
        self.b_run=tk.Button(self.menu,textvariable=self.sv_run,font=('黑体'),bg='white',command=self.thread_run, bd=1,height=1)

        l_readme.place(relx=0,rely=0.05)
        l_num.place(relx=0,rely=0.23)
        self.e_num.place(relx=0.7,rely=0.23)
        self.b_run.place(relx=0.15,rely=0.9)


    def run(self):
        if int(self.e_num.get()):
            h.insert_text('开始执行任务')
            self.sv_run.set('中止任务')
            self.b_run['command']=self.stop

            h.insert_text('开始连接模拟器')
            if not h.cnt:
                with open('database/start.txt', "rb") as f:
                    me = f.readlines()
                os.system('adb kill-server')
                os.system("adb devices")
                # 模拟器类型
                os.system("adb connect %s" % str(me[3],encoding='utf-8').replace('\n',''))  # 7555/16384
                h.insert_text('连接完成')
                h.cnt+=1
            else:
                h.insert_text('模拟器已连接')
            for ii in range(int(self.e_num.get())):
                mission()
                h.insert_text('第%i次任务完成' % int(ii+1))
            h.insert_text('任务已完成')

            self.sv_run.set('开始执行')
            self.b_run['command']=self.thread_run
        else:
            h.insert_text('未输入开荒次数','red')
        
        

    def stop(self):
        self.sv_run.set('开始执行')
        self.b_run['command']=self.thread_run

        self.tr_run.kill()
        self.tr_run.join()
        if not self.tr_run.is_alive():
            h.insert_text('已成功中止运行')

    def thread_run(self):
        self.tr_run=Thread_with_trace(target=self.run)
        self.tr_run.start()



h = Home()

home_page.mainloop()

