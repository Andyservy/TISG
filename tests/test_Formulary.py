# import wx
# import wx.adv
#
#
# class MyFrame(wx.Frame):
#     def __init__(self, parent, title=""):
#         super(MyFrame, self).__init__(parent, title=title)
#
#         self.panel = MyPanel(self)
#
#
# class MyPanel(wx.Panel):
#     def __init__(self, parent):
#         super(MyPanel, self).__init__(parent)
#
#         self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD)
#
#         # Later on...
#         self.tip = wx.adv.RichToolTip("Caps Lock is on",
#                                  "You might have made an error in your password\n"
#                                  "entry because Caps Lock is turned on.\n"
#                                  "\n"
#                                  "Press Caps Lock key to turn it off.")
#         self.password.Bind(wx.EVT_TEXT, self.OnContraseñaFill)
#
#     def OnContraseñaFill(self, event):
#         self.tip.ShowFor(self.password)
#
#
#
# def Main():
#     App = wx.App()
#     frame = MyFrame(None, title="Event Propagation")
#     frame.Show()
#     App.MainLoop()
#
#
# if __name__ == '__main__':
#     Main()


