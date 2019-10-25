import datetime
import time
import os

import wx
import wx.grid


class Test(wx.Frame):

    def get_txt_data(self):
        with open("C:\\brain_storm\\data_test.txt", 'r+', encoding='UTF-8') as f:
            data = f.readlines()
            return data

    data = get_txt_data(1)
    # print(len(data))

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'grid_test', size=(500, 400))
        panel = wx.Panel(self, wx.ID_ANY)
        self.grid = wx.grid.Grid(panel)
        self.grid.CreateGrid(len(self.data), 3)
        self.grid.SetRowSize(0, 60)
        self.grid.SetColSize(1, 100)
        self.grid.SetColSize(2, 220)
        self.grid.SetColLabelValue(0, 'id')
        self.grid.SetColLabelValue(1, '文本')
        self.grid.SetColLabelValue(2, 'date')
        i, j = 0, 0
        self.row = 0
        self.col = 0
        for i in range(len(self.data)):
            # print(self.data[i])
            cell_1 = self.data[i].split(",", 1)
            # print(cell_1)
            cell_2 = cell_1[0].split("'")
            # print(cell_2[1])
            cell_3 = cell_1[1].split(",")
            cell_3 = cell_3[0].split(" ")
            cell_3 = cell_3[1].split(")")
            # print(cell_3[0])
            cell_4 = cell_1[1].split(",")
            cell_4 = cell_4[1].split(" ")
            cell_4 = cell_4[1].split(")")
            # print(cell_4[0])
            self.grid.SetCellValue(i, 0, cell_4[0])
            self.grid.SetCellValue(i, 1, cell_2[1])
            time = datetime.datetime.fromtimestamp(float(cell_3[0]))
            self.grid.SetCellValue(i, 2, datetime.datetime.strftime(time, "%Y-%m-%d %H:%M:%S"))
        self.grid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.show_pop_menu)
        self.grid.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.select_cell)
        # self.grid.Bind(wx.EVT_CLOSE, self.rel_update)
        sizer = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        spin = wx.StaticText(panel, -1, "按字母排序", pos=wx.DefaultPosition, size=wx.DefaultSize)
        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        spin.SetFont(font)
        hbox.Add(spin)
        sc = wx.SpinButton(panel, -1, pos=wx.DefaultPosition, size=(30, 30))
        sc.Bind(wx.EVT_SPIN_UP, self.sort_by_up_spin)
        sc.Bind(wx.EVT_SPIN_DOWN, self.sort_by_down_spin)
        hbox.Add(sc)
        spin2 = wx.StaticText(panel, -1, "按时间排序", pos=wx.DefaultPosition, size=wx.DefaultSize)
        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        spin2.SetFont(font)
        hbox.Add(spin2)
        sc2 = wx.SpinButton(panel, -1, pos=wx.DefaultPosition, size=(30, 30))
        sc2.Bind(wx.EVT_SPIN_UP, self.sort_by_up_spin_time)
        sc2.Bind(wx.EVT_SPIN_DOWN, self.sort_by_down_spin_time)
        hbox.Add(sc2)
        sizer.Add(self.grid, -1, wx.EXPAND, 2)
        sizer.Add(hbox)
        panel.SetSizer(sizer)
        self.select_id = self.grid.GetCellValue(self.row, 0)

    def select_cell(self, event):
        self.row = event.GetRow()
        self.col = event.GetCol()
        # print(self.row+1)

    def show_pop_menu(self, event):
        menu = wx.Menu()
        item = wx.MenuItem(menu, -1, 'Edit')
        item2 = wx.MenuItem(menu, -1, 'Delete')
        menu.Append(item)
        menu.Append(item2)

        self.Bind(wx.EVT_MENU, self.edit, item)
        self.Bind(wx.EVT_MENU, self.delete, item2)

        # self.get_data()
        self.PopupMenu(menu)
        menu.Destroy()

    def edit(self, event):
        self.time = 0

        def get_data(event):
            msg = self.msg("确定编辑？")
            if msg == wx.ID_OK:
                item = text1.GetValue()
                self.grid.SetCellValue(self.row, self.col, item)
                self.time = time.time()
                item2 = datetime.datetime.fromtimestamp(self.time)
                self.grid.SetCellValue(self.row, 2, datetime.datetime.strftime(item2, "%Y-%m-%d %H:%M:%S"))
                self.rel_update()
            else:
                pass
        # print(self.time)
        app1 = wx.App()
        window = wx.Frame(None, title="test", size=(500, 200))
        panel = wx.Panel(window)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        line1 = wx.StaticText(panel, -1, "请输入：")
        hbox.Add(line1, 1, wx.EXPAND, 5)
        text1 = wx.TextCtrl(panel)
        hbox.Add(text1, 1, wx.EXPAND, 5)
        button = wx.Button(panel, label="确认")
        button.Bind(wx.EVT_BUTTON, get_data)
        hbox.Add(button, 1, wx.EXPAND, 5)
        vbox.Add(hbox)
        panel.SetSizer(vbox)
        window.Show()
        app1.MainLoop()

    # 为了实现数据的更新，应当每次编辑或删除后都进行一次数据的更新

    def delete(self, event):
        msg2 = self.msg("确定要删除吗？")
        if msg2 == wx.ID_OK:
            self.grid.DeleteRows(pos=self.row, numRows=1, updateLabels=True)
            self.rel_update()
        #     此处需要进行txt内的删除，或者不进行操作，统一写入txt
        else:
            pass

    def get_data(self):
        waiting_data = []
        row_num = self.grid.GetNumberRows()
        for i in range(row_num):
            for j in range(3):
                if j == 0:
                    waiting_data.append(int(self.grid.GetCellValue(i, j)))
                elif j == 2:
                    time_str = self.grid.GetCellValue(i, j)
                    timestamp = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").timestamp()
                    waiting_data.append(timestamp)
                else:
                    waiting_data.append(self.grid.GetCellValue(i, j))
        #         注意这里的id放在了前面
        # print(waiting_data)

        return waiting_data

    def rel_update(self):
        update_data = self.get_data()
        rewrite_data = str()
        row_num = self.grid.GetNumberRows()
        try:
            for i in range(row_num):
                if i == 0:
                    waiting_data_2 = (update_data[1], update_data[2], int(update_data[0]))
                else:
                    waiting_data_2 = (update_data[i*3+1], update_data[i*3+2], int(update_data[i*3]))
                rewrite_data += str(waiting_data_2) + "\n"
                # print(rewrite_data)
            # print(rewrite_data)
            with open("C:\\brain_storm\\data_test.txt", 'w', encoding='UTF-8') as f:
                f.write(rewrite_data)
        except ImportError:
            print("update_error")

    def msg(self, data1):
        msg1 = wx.MessageDialog(None, data1, caption="info", style=wx.OK | wx.CANCEL)
        return msg1.ShowModal()

    def sort_by_up_spin(self, event):
        sorted_data = self.data
        wait_for_sort = []
        wfs = []
        for i in range(len(sorted_data)):
            sd = sorted_data[i].split(",")
            wfs.append(sd)
            sd2 = sd[0].split("(")
            sd3 = sd2[1].split("'")
            wait_for_sort.append(sd3[1])
        data_s1 = sorted(wait_for_sort, key=lambda x: x.lower())
        # print(data_s1)
        wfs2 = str(wfs).split("'")

        for i in range(len(wfs2)-1, -1, -1):
            if wfs2[i] == '[["(' or wfs2[i] == '", ' or wfs2[i] == ', ' or wfs2[i] == '], ["(':
                wfs2.pop(i)
        # print(wfs2)

        for i in range(len(data_s1)):
            id_num = wfs2.index(data_s1[i])
            id_num = int(id_num/3)
            cell_1 = sorted_data[id_num].split(",", 1)
            # print(cell_1)
            cell_2 = cell_1[0].split("'")
            # print(cell_2[1])
            cell_3 = cell_1[1].split(",")
            cell_3 = cell_3[0].split(" ")
            cell_3 = cell_3[1].split(")")
            # print(cell_3[0])
            cell_4 = cell_1[1].split(",")
            cell_4 = cell_4[1].split(" ")
            cell_4 = cell_4[1].split(")")
            # print(cell_4[0])
            self.grid.SetCellValue(i, 0, cell_4[0])
            self.grid.SetCellValue(i, 1, cell_2[1])
            time = datetime.datetime.fromtimestamp(float(cell_3[0]))
            self.grid.SetCellValue(i, 2, datetime.datetime.strftime(time, "%Y-%m-%d %H:%M:%S"))

    def sort_by_down_spin(self, event):
        sorted_data = self.data
        wait_for_sort = []
        wfs = []
        for i in range(len(sorted_data)):
            sd = sorted_data[i].split(",")
            wfs.append(sd)
            sd2 = sd[0].split("(")
            sd3 = sd2[1].split("'")
            wait_for_sort.append(sd3[1])
        data_s1 = sorted(wait_for_sort, reverse=True, key=lambda x: x.lower())
        wfs2 = str(wfs).split("'")

        for i in range(len(wfs2) - 1, -1, -1):
            if wfs2[i] == '[["(' or wfs2[i] == '", ' or wfs2[i] == ', ' or wfs2[i] == '], ["(':
                wfs2.pop(i)

        for i in range(len(data_s1)):
            id_num = wfs2.index(data_s1[i])
            id_num = int(id_num / 3)
            cell_1 = sorted_data[id_num].split(",", 1)
            cell_2 = cell_1[0].split("'")
            cell_3 = cell_1[1].split(",")
            cell_3 = cell_3[0].split(" ")
            cell_3 = cell_3[1].split(")")
            cell_4 = cell_1[1].split(",")
            cell_4 = cell_4[1].split(" ")
            cell_4 = cell_4[1].split(")")
            self.grid.SetCellValue(i, 0, cell_4[0])
            self.grid.SetCellValue(i, 1, cell_2[1])
            time = datetime.datetime.fromtimestamp(float(cell_3[0]))
            self.grid.SetCellValue(i, 2, datetime.datetime.strftime(time, "%Y-%m-%d %H:%M:%S"))

    def sort_by_up_spin_time(self, event):
        sorted_data = self.data
        wait_for_sort = []
        wfs = []
        for i in range(len(sorted_data)):
            sd = sorted_data[i].split(",")
            wfs.append(sd)
            sd2 = sd[1].split("(")
            sd3 = sd2[0].split(" ")
            wait_for_sort.append(sd3[1])
            # print(wait_for_sort)
        data_s1 = sorted(wait_for_sort, key=lambda x: x.lower())
        # print(data_s1)
        wfs2 = str(wfs).split(" ")
        # print(wfs2)

        for i in range(len(wfs2)-1, -1, -1):
            # print(wfs2[i])
            if wfs2[i] == "'":
                wfs2.pop(i)
        for i in range(len(wfs2)):
            if i % 3 == 1:
                wfs3 = wfs2[i].split("'")
                wfs2.pop(i)
                wfs2.insert(i, wfs3[0])
                # print(wfs2[i])
        # print(wfs2)

        for i in range(len(data_s1)):
            id_num = wfs2.index(data_s1[i])
            id_num = int(id_num / 3)
            # print(sorted_data)
            # print(id_num)
            cell_1 = sorted_data[id_num].split(",", 1)
            # print(cell_1)
            cell_2 = cell_1[0].split("'")
            # print(cell_2[1])
            cell_3 = cell_1[1].split(",")
            cell_3 = cell_3[0].split(" ")
            cell_3 = cell_3[1].split(")")
            # print(cell_3[0])
            cell_4 = cell_1[1].split(",")
            cell_4 = cell_4[1].split(" ")
            cell_4 = cell_4[1].split(")")
            # print(cell_4[0])
            self.grid.SetCellValue(i, 0, cell_4[0])
            self.grid.SetCellValue(i, 1, cell_2[1])
            time = datetime.datetime.fromtimestamp(float(cell_3[0]))
            self.grid.SetCellValue(i, 2, datetime.datetime.strftime(time, "%Y-%m-%d %H:%M:%S"))

    def sort_by_down_spin_time(self, event):
        sorted_data = self.data
        wait_for_sort = []
        wfs = []
        for i in range(len(sorted_data)):
            sd = sorted_data[i].split(",")
            wfs.append(sd)
            sd2 = sd[1].split("(")
            sd3 = sd2[0].split(" ")
            wait_for_sort.append(sd3[1])
            # print(wait_for_sort)
        data_s1 = sorted(wait_for_sort, reverse=True, key=lambda x: x.lower())
        # print(data_s1)
        wfs2 = str(wfs).split(" ")
        # print(wfs2)

        for i in range(len(wfs2) - 1, -1, -1):
            # print(wfs2[i])
            if wfs2[i] == "'":
                wfs2.pop(i)
        for i in range(len(wfs2)):
            if i % 3 == 1:
                wfs3 = wfs2[i].split("'")
                wfs2.pop(i)
                wfs2.insert(i, wfs3[0])
                # print(wfs2[i])
        # print(wfs2)

        for i in range(len(data_s1)):
            id_num = wfs2.index(data_s1[i])
            id_num = int(id_num / 3)
            # print(sorted_data)
            # print(id_num)
            cell_1 = sorted_data[id_num].split(",", 1)
            # print(cell_1)
            cell_2 = cell_1[0].split("'")
            # print(cell_2[1])
            cell_3 = cell_1[1].split(",")
            cell_3 = cell_3[0].split(" ")
            cell_3 = cell_3[1].split(")")
            # print(cell_3[0])
            cell_4 = cell_1[1].split(",")
            cell_4 = cell_4[1].split(" ")
            cell_4 = cell_4[1].split(")")
            # print(cell_4[0])
            self.grid.SetCellValue(i, 0, cell_4[0])
            self.grid.SetCellValue(i, 1, cell_2[1])
            time = datetime.datetime.fromtimestamp(float(cell_3[0]))
            self.grid.SetCellValue(i, 2, datetime.datetime.strftime(time, "%Y-%m-%d %H:%M:%S"))


def data_show_1_run():
    app = wx.App()
    frame = Test()
    frame.Show()
    app.MainLoop()
