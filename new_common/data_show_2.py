import datetime
import time

import wx
import wx.grid


class Test(wx.Frame):
    def get_txt_data(self):
        with open("C:\\brain_storm\\data_test_2.txt", 'r+', encoding='UTF-8') as f:
            data = f.readlines()
            return data

    data = get_txt_data(True)
    # print(len(data))

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'grid_test', size=(700, 600))
        self.Bind(wx.EVT_CLOSE, self.on_close)
        panel = wx.Panel(self, wx.ID_ANY)
        self.grid = wx.grid.Grid(panel)
        self.grid.CreateGrid(len(self.data), 5)
        self.grid.SetRowSize(0, 40)
        self.grid.SetColSize(1, 150)
        self.grid.SetColSize(2, 100)
        self.grid.SetColSize(3, 100)
        self.grid.SetColSize(4, 200)
        self.grid.SetColLabelValue(0, 'id')
        self.grid.SetColLabelValue(1, '文本')
        self.grid.SetColLabelValue(2, '组合公式')
        self.grid.SetColLabelValue(3, '备注')
        self.grid.SetColLabelValue(4, 'date')
        self.row = 0
        self.col = 0
        for i in range(len(self.data)):
            # print(self.data[i])
            cell_1 = self.data[i].split('"')
            # print(cell_1)
            cell_2 = cell_1[2].split("'")
            # for i in range(len(cell_2)):
            #     print(i, cell_2[i])
            cell_3 = cell_2[-1].split(",")
            cell_4 = cell_3[-1].split(')')
            cell_4 = cell_4[0].split(" ")
            cell_5 = cell_3[1].split(" ")
            # print(cell_3)
            self.grid.SetCellValue(i, 0, cell_4[1])
            self.grid.SetCellValue(i, 1, cell_1[1])
            self.grid.SetCellValue(i, 2, cell_2[1])
            self.grid.SetCellValue(i, 3, cell_2[3])
            time_2 = datetime.datetime.fromtimestamp(float(cell_5[1]))
            self.grid.SetCellValue(i, 4, datetime.datetime.strftime(time_2, "%Y-%m-%d %H:%M:%S"))
        self.grid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.show_pop_menu)
        self.grid.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.select_cell)
        sizer = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        spin = wx.StaticText(panel, -1, "按字母排序", pos=wx.DefaultPosition, size=wx.DefaultSize)
        font = wx.Font(18, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL)
        spin.SetFont(font)
        hbox.Add(spin)
        sc = wx.SpinButton(panel, -1, pos=wx.DefaultPosition, size=(30, 30))
        sc.Bind(wx.EVT_SPIN_UP, self.sort_by_up_spin)
        sc.Bind(wx.EVT_SPIN_DOWN, self.sort_by_down_spin)
        hbox.Add(sc)
        spin2 = wx.StaticText(panel, -1, "按时间排序", pos=wx.DefaultPosition, size=wx.DefaultSize)
        font = wx.Font(18, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL)
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
    #     之所以放在了这里是因为提示最好将它放在__init__里面

    def select_cell(self, event):
        self.row = event.GetRow()
        self.col = event.GetCol()
        # self.select_id = self.grid.GetCellValue(self.row, 0)
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

        def get_data(event):
            msg = self.msg("确定编辑？")
            if msg == wx.ID_OK:
                item = text1.GetValue()
                self.grid.SetCellValue(self.row, self.col, item)
                self.time = time.time()
                item2 = datetime.datetime.fromtimestamp(self.time)
                self.grid.SetCellValue(self.row, 4, datetime.datetime.strftime(item2, "%Y-%m-%d %H:%M:%S"))
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
            for j in range(5):
                if j == 0:
                    waiting_data.append(int(self.grid.GetCellValue(i, j)))
                elif j == 4:
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
        for i in range(row_num):
            if i == 0:
                waiting_data_2 = (update_data[1], update_data[2],
                                  update_data[3], update_data[4],
                                  int(update_data[0]))
            else:
                waiting_data_2 = (update_data[i*5+1], update_data[i*5+2],
                                  update_data[i*5+3], update_data[i*5+4],
                                  int(update_data[i*5]))
            rewrite_data += str(waiting_data_2) + "\n"
            # print(rewrite_data)
        # print(rewrite_data)
        with open("C:\\brain_storm\\data_test_2.txt", 'w+', encoding='UTF-8') as f:
            f.write(rewrite_data)

    def msg(self, data1):
        msg1 = wx.MessageDialog(None, data1, caption="info", style=wx.OK | wx.CANCEL)
        return msg1.ShowModal()

    def on_close(self, event):
        msg = self.msg("是否确认关闭？")
        if msg == wx.ID_OK:
            wx.Frame.Destroy(self)
        else:
            pass

    def sort_by_up_spin(self, event):
        sorted_data = self.data
        wait_for_sort = []
        data_for_index = []
        data_for_index_2 = []
        for i in range(len(sorted_data)):
            sd = sorted_data[i].split('"')
            data_for_index.append(sd)
            wait_for_sort.append(sd[1])
        data_s1 = sorted(wait_for_sort, key=lambda x: x.lower())
        for i in range(len(data_for_index)):
            data_for_index_2.append(data_for_index[i][1])
            dfi2 = data_for_index[i][2].split("'")
            data_for_index_2.append(dfi2[1])
            data_for_index_2.append(dfi2[3])
            dfi3 = dfi2[4].split(" ")
            dfi5 = dfi3[1].split(",")
            data_for_index_2.append(dfi5[0])
            dfi4 = dfi3[2].split(")")
            data_for_index_2.append(dfi4[0])
        # print(data_for_index_2)

        for i in range(len(data_s1)):
            id_num = data_for_index_2.index(data_s1[i])
            self.grid.SetCellValue(i, 0, data_for_index_2[id_num+4])
            self.grid.SetCellValue(i, 1, data_for_index_2[id_num])
            self.grid.SetCellValue(i, 2, data_for_index_2[id_num+1])
            self.grid.SetCellValue(i, 3, data_for_index_2[id_num+2])
            time_3 = datetime.datetime.fromtimestamp(float(data_for_index_2[id_num+3]))
            self.grid.SetCellValue(i, 4, datetime.datetime.strftime(time_3, "%Y-%m-%d %H:%M:%S"))

    def sort_by_down_spin(self, event):
        sorted_data = self.data
        wait_for_sort = []
        data_for_index = []
        data_for_index_2 = []
        for i in range(len(sorted_data)):
            sd = sorted_data[i].split('"')
            data_for_index.append(sd)
            wait_for_sort.append(sd[1])
        data_s1 = sorted(wait_for_sort, reverse=True, key=lambda x: x.lower())
        for i in range(len(data_for_index)):
            data_for_index_2.append(data_for_index[i][1])
            dfi2 = data_for_index[i][2].split("'")
            data_for_index_2.append(dfi2[1])
            data_for_index_2.append(dfi2[3])
            dfi3 = dfi2[4].split(" ")
            dfi5 = dfi3[1].split(",")
            data_for_index_2.append(dfi5[0])
            dfi4 = dfi3[2].split(")")
            data_for_index_2.append(dfi4[0])
        # print(data_for_index_2)

        for i in range(len(data_s1)):
            id_num = data_for_index_2.index(data_s1[i])
            self.grid.SetCellValue(i, 0, data_for_index_2[id_num + 4])
            self.grid.SetCellValue(i, 1, data_for_index_2[id_num])
            self.grid.SetCellValue(i, 2, data_for_index_2[id_num + 1])
            self.grid.SetCellValue(i, 3, data_for_index_2[id_num + 2])
            time_4 = datetime.datetime.fromtimestamp(float(data_for_index_2[id_num + 3]))
            self.grid.SetCellValue(i, 4, datetime.datetime.strftime(time_4, "%Y-%m-%d %H:%M:%S"))

    def sort_by_up_spin_time(self, event):
        sorted_data = self.data
        wait_for_sort = []
        data_for_index = []
        data_for_index_2 = []
        for i in range(len(sorted_data)):
            sd = sorted_data[i].split('"')
            data_for_index.append(sd)
        for i in range(len(data_for_index)):
            data_for_index_2.append(data_for_index[i][1])
            dfi2 = data_for_index[i][2].split("'")
            data_for_index_2.append(dfi2[1])
            data_for_index_2.append(dfi2[3])
            dfi3 = dfi2[4].split(" ")
            dfi5 = dfi3[1].split(",")
            data_for_index_2.append(dfi5[0])
            wait_for_sort.append(dfi5[0])
            dfi4 = dfi3[2].split(")")
            data_for_index_2.append(dfi4[0])
        data_s1 = sorted(wait_for_sort, key=lambda x: x.lower())
        # print(data_for_index_2)

        for i in range(len(data_s1)):
            id_num = data_for_index_2.index(data_s1[i])
            self.grid.SetCellValue(i, 0, data_for_index_2[id_num + 1])
            self.grid.SetCellValue(i, 1, data_for_index_2[id_num - 3])
            self.grid.SetCellValue(i, 2, data_for_index_2[id_num - 2])
            self.grid.SetCellValue(i, 3, data_for_index_2[id_num - 1])
            time_5 = datetime.datetime.fromtimestamp(float(data_for_index_2[id_num]))
            self.grid.SetCellValue(i, 4, datetime.datetime.strftime(time_5, "%Y-%m-%d %H:%M:%S"))

    def sort_by_down_spin_time(self, event):
        sorted_data = self.data
        wait_for_sort = []
        data_for_index = []
        data_for_index_2 = []
        for i in range(len(sorted_data)):
            sd = sorted_data[i].split('"')
            data_for_index.append(sd)
        for i in range(len(data_for_index)):
            data_for_index_2.append(data_for_index[i][1])
            dfi2 = data_for_index[i][2].split("'")
            data_for_index_2.append(dfi2[1])
            data_for_index_2.append(dfi2[3])
            dfi3 = dfi2[4].split(" ")
            dfi5 = dfi3[1].split(",")
            data_for_index_2.append(dfi5[0])
            wait_for_sort.append(dfi5[0])
            dfi4 = dfi3[2].split(")")
            data_for_index_2.append(dfi4[0])
        data_s1 = sorted(wait_for_sort, reverse=True, key=lambda x: x.lower())
        # print(data_for_index_2)

        for i in range(len(data_s1)):
            id_num = data_for_index_2.index(data_s1[i])
            self.grid.SetCellValue(i, 0, data_for_index_2[id_num + 1])
            self.grid.SetCellValue(i, 1, data_for_index_2[id_num - 3])
            self.grid.SetCellValue(i, 2, data_for_index_2[id_num - 2])
            self.grid.SetCellValue(i, 3, data_for_index_2[id_num - 1])
            time_6 = datetime.datetime.fromtimestamp(float(data_for_index_2[id_num]))
            self.grid.SetCellValue(i, 4, datetime.datetime.strftime(time_6, "%Y-%m-%d %H:%M:%S"))


def data_show_2_run():
    app = wx.App()
    frame = Test()
    frame.Show()
    app.MainLoop()
