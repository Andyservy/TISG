import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        #self.panel = wx.Panel(self)
        self.btn = wx.Button(self, label="Panel 1", size=(250,75))
        self.btn.Bind(wx.EVT_BUTTON, self.switch)

        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(self.btn)
        #self.panel.SetSizer(vbox1)
        self.SetSizer(vbox1)

        #vbox = wx.BoxSizer(wx.VERTICAL)
        #vbox.Add(self.panel)
        #self.SetSizer(vbox)

        self.Show()

    def switch(self, event):
        self.parent.Swap()

class MyOtherPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        #self.panel = wx.Panel(self)
        self.btn = wx.Button(self, label="Panel 2", size=(175,250))
        self.btn.Bind(wx.EVT_BUTTON, self.switch)

        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(self.btn)
        self.SetSizer(vbox1)

        #vbox = wx.BoxSizer(wx.VERTICAL)
        #vbox.Add(self.panel)
        #self.SetSizer(vbox)

        self.Show()
        self.Hide()

    def switch(self, event):
        self.parent.Swap()

class PanelSwitcher(wx.Frame):
    def __init__(self):
        super().__init__(None)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.panel1 = MyPanel(self)
        self.panel2 = MyOtherPanel(self)
        vbox.Add(self.panel1)
        vbox.Add(self.panel2)
        self.SetSizer(vbox)
        self.Show()

    def Swap(self):
        if self.panel1.IsShown():
            self.panel1.Hide()
            self.panel2.Show()
        else:
            self.panel2.Hide()
            self.panel1.Show()
        self.Layout()
        self.Refresh()


if __name__ == "__main__":
    app = wx.App()
    PanelSwitcher()
    app.MainLoop()