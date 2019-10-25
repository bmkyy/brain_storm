# 试试直接写入str，以\n分行
# 还有缺陷，需要实现自增id以协助后续查看编辑功能实现 done
import time
import os

import tkinter
from tkinter import *
import tkinter.messagebox


class Insert(object):
    def __init__(self):
        self.tk = tkinter.Tk()
        self.tk.title('test')
        self.tk.geometry('400x200+750+400')
        self.label = tkinter.Label(master=self.tk, text='请输入：')
        self.label.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.entry = tkinter.Entry(master=self.tk)
        self.entry.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.button = tkinter.Button(master=self.tk, text='提交', command=self.get_input)
        self.button.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.tk.mainloop()

    def get_data(self):
        with open('C:\\brain_storm\\data_test.txt', 'r+', encoding='UTF-8') as f:
            data = f.read()
            return data

    def write_data(self, data):
        with open('C:\\brain_storm\\data_test.txt', 'w+', encoding='UTF-8') as f:
            f.write(data)

    def msg(self, msg):
        tkinter.messagebox.showinfo(message=msg)

    def num(self):
        check_data = self.get_data()
        if check_data:
            with open("C:\\brain_storm\\data_test.txt", 'r+', encoding='UTF-8') as f:
                cd = f.readlines()
                cd2 = cd[len(cd) - 1].split(",")
                # print(cd2)
                # cd3 = cd2[0].split("'")
                cd4 = cd2[2].split(")")
                cd5 = cd4[0].split(" ")
                # print(cd5[1])
                id_num = int(cd5[1]) + 1
                # id_num = 5
        else:
            id_num = 0
        return id_num

    def get_input(self):
        input_string = self.entry.get()
        input_string = (input_string, time.time(), self.num())
        check_data = self.get_data()
        # print(check_data)
        if check_data:
            with open("C:\\brain_storm\\data_test.txt", 'r+', encoding='UTF-8') as f:
                cd = f.readlines()
                # print(cd)
                j = 0
                for i in range(len(cd)):
                    cd2 = cd[i].split(",")
                    # print(cd2)
                    cd3 = cd2[0].split("'")
                    cd4 = cd2[2].split(")")
                    # cd5 = cd4[0].split(" ")
                    # print(cd5[1])
                    if cd3[1] == input_string[0]:
                        self.msg("Already exist")
                        break
            #       break跳出的是for循环
                    j += 1
                if j == len(cd):
                    data_for_write = check_data + str(input_string) + "\n"
                    self.write_data(data_for_write)
                    self.msg("Insert succeed")
        else:
            data_for_write = check_data + str(input_string) + "\n"
            self.write_data(data_for_write)
            self.msg("Insert succeed")


def run_insert():
    Insert()
