import wx

def on0Focus(event):
    button0.Enable()
    button1.Disable()
    print ("text0 widget received focus!")

def on1Focus(event):
    button1.Enable()
    button0.Disable()
    print ("text1 widget received focus!")

app = wx.App()

frame = wx.Frame(None, -1, 'Set Focus Test', size=(500,100))

dummy = wx.TextCtrl(frame, wx.ID_ANY, size=(1,1), pos=(10,1))#Prevents text0 getting focus on Show()
text0 = wx.TextCtrl(frame, wx.ID_ANY, size=(345,25), pos=(10,10))
text0.SetValue("123456")
button0 = wx.Button(frame,-1, "Zero",pos=(400,10))

text1 = wx.TextCtrl(frame, wx.ID_ANY, size=(345,25), pos=(10,40))
text1.SetValue("abcdef")
button1 = wx.Button(frame,-1, "One", pos=(400,40))

text0.Bind(wx.EVT_SET_FOCUS, on0Focus)
text1.Bind(wx.EVT_SET_FOCUS, on1Focus)
button0.Disable()
button1.Disable()

frame.Show()

app.MainLoop()