#!/usr/bin/env python

import wx
import os
import re
import glob

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self,parent, title=title, size=(750,300),                style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.panel = wx.Panel(self,-1)

        testlist = ["apples","dogs","cats","pears","blue"]

        self.listBox = wx.CheckListBox(self.panel, -1, (20, 6), (220, 195), testlist, wx.LB_SINGLE)

        self.filecount = self.listBox.GetCount()
        self.findchecked = self.listBox.GetChecked()


        self.filecountdisplay = str(len(self.findchecked)) + "/" + str(self.filecount) + " Files"
        self.inlistDisplay = wx.StaticText(self.panel, -1, self.filecountdisplay,(160,215))

        self.Centre()
        self.Show(True)

        self.listBox.Bind(wx.EVT_PAINT, self.on_list_update)

    def on_list_update(self, event):
        event.Skip()
        self.findchecked = self.listBox.GetChecked()
        self.filecount = self.listBox.GetCount()
        self.filecountdisplay = str(len(self.findchecked)) + "/" + str(self.filecount) + " Files"
        self.inlistDisplay = wx.StaticText(self.panel, -1, self.filecountdisplay, (160, 215))
        self.Refresh()



    def OnExit(self,e):
        self.Close(True)

app = wx.App(True)
frame = MyFrame(None,"Alexa Puller v1.1")
app.MainLoop()