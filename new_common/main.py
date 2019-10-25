import time
import os

import wx
import wx.grid
import tkinter
from tkinter import *
import tkinter.messagebox
import random
import datetime

# import insert
# import data_show_1
# import combine
# import data_show_2

class Show(wx.Frame):
    def __init__(self):

        if os.path.isfile('C:\\brain_storm\\data_test.txt'):
            pass
        else:
            os.makedirs('C:\\brain_storm')
            f = open('C:\\brain_storm\\data_test.txt', 'w+', encoding='UTF-8')
            f.close()

        if os.path.isfile('C:\\brain_storm\\data_test_2.txt'):
            pass
        else:
            f = open('C:\\brain_storm\\data_test_2.txt', 'w+', encoding='UTF-8')
            f.close()

        wx.Frame.__init__(self, None, wx.ID_ANY, 'Brain Storm')
        panel = wx.Panel(self, wx.ID_ANY)
        vertical_sizer = wx.BoxSizer(wx.VERTICAL)
        text1 = wx.StaticText(panel, -1, "Brain Storm", (100, 30), (150, -1), wx.ALIGN_CENTER)
        jump1 = wx.Button(panel, label='零星想法')
        jump1.Bind(wx.EVT_BUTTON, self.brain)
        jump2 = wx.Button(panel, label='巡视想法')
        jump2.Bind(wx.EVT_BUTTON, self.check1)
        jump3 = wx.Button(panel, label='组合')
        jump3.Bind(wx.EVT_BUTTON, self.storm)
        jump4 = wx.Button(panel, label='巡视结果')
        jump4.Bind(wx.EVT_BUTTON, self.check2)
        vertical_sizer.Add(text1)
        vertical_sizer.Add(jump1)
        vertical_sizer.Add(jump2)
        vertical_sizer.Add(jump3)
        vertical_sizer.Add(jump4)
        panel.SetSizer(vertical_sizer)

    def brain(self, event):
        import insert
        insert.run_insert()

    def check1(self, event):
        import data_show_1
        data_show_1.data_show_1_run()

    def storm(self, event):
        import combine
        combine.run_combine()

    def check2(self, event):
        import data_show_2
        data_show_2.data_show_2_run()

# 目前需要做的事：1 将这四个文件里的def全部移进class里去 done
#                2 修改箭头排序以及排序后的编辑删除功能 sql_1 done


if __name__ == '__main__':
    app = wx.App()
    frame = Show()
    frame.Show()
    app.MainLoop()
