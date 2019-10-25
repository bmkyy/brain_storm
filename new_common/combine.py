import random
import time
import os

import wx
import wx.grid


# 先把显示提取数量的界面弄出来


class Showing(wx.Frame):
    # 还是实现获取的数据是以元组形式的，可以直接调用的来比较好，不用有太多的修改
    def get_string(self):
        data_2 = list()
        data_3 = list()
        data_4 = list()
        data_5 = list()
        data_6 = list()
        data_7 = list()
        data_8 = list()
        with open("C:\\brain_storm\\data_test.txt", 'r+', encoding='UTF-8') as f:
            data = f.read()
            range_num = data.count("(")
            data2 = data.split(',')
            for i in range(range_num):
                data_2.append(data2[2*i])
            data_2 = str(data_2).split("'")
            # print(data)
            for i in range(range_num):
                data_3.append(data_2[2*i+1])
            # print(data_3)
            data_4_2 = str(data2).split(" ")
            # 丢失后面的数据，待修改
            # print(data_4_2)
            for i in range(range_num):
                # print(i, data_4_2[i])
                data_4.append(data_4_2[(i+1)*4])
                data_6.append(data_4_2[i*4+2])
                # print(i, data_4)
            for item in data_4:
                item_2 = item.split(")")
                data_5.append(int(item_2[0]))
            # print(data_5)
            for item in data_6:
                item_2 = item.split("'")
                data_7.append(float(item_2[0]))
            # print(data_7)
            for i in range(data_5[-1]+1):
                data_8.append(tuple([data_3[i], data_7[i], data_5[i]]))
            # print(data_8)

        return data_8

    def get_string2(self):
        with open("C:\\brain_storm\\data_test_2.txt", 'r+', encoding='UTF-8') as f:
            data = f.read()

        return data

    data = get_string(1)
    num = len(data)

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'info', pos=(800, 400), size=(500, 600))
        self.panel = wx.Panel(self, wx.ID_ANY)
        # 预设grid位置
        self.grid = wx.grid.Grid(self.panel, size=(500, 200))
        line = wx.StaticText(self.panel, -1, "请输入提取数量：")
        self.input_string = wx.TextCtrl(self.panel, -1, "")
        button = wx.Button(self.panel, -1, label="确认")
        button.Bind(wx.EVT_BUTTON, self.get_data)
        sizer = wx.FlexGridSizer(cols=3, hgap=30, vgap=10)
        sizer.AddMany([line, self.input_string, button])
        line2 = wx.StaticText(self.panel, -1, "输入结合公式：")
        self.input_string2 = wx.TextCtrl(self.panel, -1, "输入公式", size=(300, 30))
        button2 = wx.Button(self.panel, -1, label="确认")
        button2.Bind(wx.EVT_BUTTON, self.get_string_data)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(line2)
        hbox.Add(self.input_string2)
        hbox.Add(button2)
        line3 = wx.StaticText(self.panel, -1, "结果公式备注：")
        self.input_string3 = wx.TextCtrl(self.panel, -1, "输入备注", size=(300, 30))
        button3 = wx.Button(self.panel, -1, label="确认")
        button3.Bind(wx.EVT_BUTTON, self.get_string_data2)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(line3)
        hbox2.Add(self.input_string3)
        hbox2.Add(button3)
        button4 = wx.Button(self.panel, -1, label="确定录入")
        button4.Bind(wx.EVT_BUTTON, self.check_and_save)
        self.sizer2 = wx.BoxSizer(wx.VERTICAL)
        self.sizer2.Add(self.grid)
        self.sizer2.Add(sizer)
        self.sizer2.Add(hbox)
        self.sizer2.Add(hbox2)
        self.sizer2.Add(button4)
        self.panel.SetSizer(self.sizer2)

    def get_data(self, event):
        item = int(self.input_string.GetValue())
        self.a = []
        i = 0
        if item:
            while i < item:
                self.item2 = random.randint(0, self.num-1)
                if self.item2 not in self.a:
                    self.a.append(self.data[self.item2])
                    i += 1
                # print(self.a)
        else:
            self.msg("请输入正整数！")
        self.grid.Destroy()
        self.grid = wx.grid.Grid(self.panel, size=(500, 200))
        self.grid.CreateGrid(item, 1)
        self.grid.SetRowSize(0, 30)
        self.grid.SetColLabelValue(0, "提取文本")
        j = 0
        # print(self.a)
        for item3 in self.a:
            self.grid.SetCellValue(j, 0, item3[0])
            j += 1

    def msg(self, data1):
        msg1 = wx.MessageDialog(None, data1, caption="info", style=wx.OK | wx.CANCEL)
        return msg1.ShowModal()

    # 公式结果框、备注框保存
    formula = None
    remarks = None

    def get_string_data(self, event):
        item = self.input_string2.GetValue()
        if item:
            self.formula = item
            # print(self.formula)
        else:
            self.msg("请输入公式！")

    def get_string_data2(self, event):
        item = self.input_string3.GetValue()
        if item:
            self.remarks = item
            # print(self.remarks)
        else:
            self.msg("请输入备注！")

    def check_and_save(self, event):
        data_3 = list()
        data_4 = list()
        data_6 = list()
        data_7 = list()
        data_8 = list()
        data_10 = list()
        data_12 = list()
        if self.formula and self.formula:
            item1 = []
            # print(self.a)
            for item in self.a:
                item1.append(item[0])
            item1 = str(item1)
            # print(item1)
            item2 = self.formula
            item3 = self.remarks
            check_data = self.get_string2()
            range_num = check_data.count("(")
            # print(data.count("("))
            data_2 = check_data.split('"')
            # for i in range(len(data_2)):
            #     print(i, data_2[i])
            for i in range(range_num):
                data_3.append(data_2[i * 2 + 1])
                data_4.append(data_2[i * 2 + 2])
            # print(data_3)
            data_5 = str(data_4).split("'")
            # for i in range(len(data_5)):
            #     print(i, data_5[i])
            for i in range(range_num):
                data_6.append(data_5[i * 4 + 1])
                data_7.append(data_5[i * 4 + 3])
            # print(data_6)
            # print(data_7)
            data_9_2 = list()
            for i in range(range_num):
                data_9 = data_2[-(i*2+1)].split(" ")
                data_9_2.append(data_9)
            for item in data_9_2:
                # print(item[-1])
                data_10.append(item[-1])
            for i in range(range_num):
                data_11 = data_10[i].split(")")
                data_12.append(int(data_11[0]))
            data_12.sort()
            # print(data_12)

            for i in range(range_num):
                data_8.append(tuple([data_3[i], data_6[i], data_7[i]]))
            # for i in range(len(data_9)):
            #     print(i, data_9[i])
            # print(data_8)
            # id_num = int(check_data[-1][-1])
            # print(id_num)
            if check_data:
                id_num = int(data_12[-1]) + 1
                for item in data_8:
                    if item1 != item[0] or item2 != item[1] or item3 != item[2]:
                        input_data = tuple([item1, item2, item3, time.time(), id_num])
                        input_string = check_data + str(input_data) + "\n"
                        with open("C:\\brain_storm\\data_test_2.txt", 'w+', encoding='UTF-8') as f:
                            f.write(input_string)
                        # 应该在此处加上时间戳以及id，并将5项合为一项
                        # print(check_data[id_num][0]+1)
                        self.msg("已录入。")
                        break
            else:
                input_data = tuple([item1, item2, item3, time.time(), 0])
                with open("C:\\brain_storm\\data_test_2.txt", 'w+', encoding='UTF-8') as f:
                    f.write(str(input_data)+"\n")
                self.msg("已录入。")


def run_combine():
    app = wx.App()
    frame = Showing()
    frame.Show()
    app.MainLoop()
