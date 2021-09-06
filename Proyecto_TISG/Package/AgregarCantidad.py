import  wx
from Proyecto_TISG.Package import JustInt, show_messange


class CantidadAdicional(wx.Dialog):
    def __init__(self, Parent):
        wx.Dialog.__init__(self, None, -1, 'Confirmar', size=(200,120))

        self.parent = Parent
        self.Result = None

        # Add components.
        self.text = wx.TextCtrl(self)
        JustInt(self.text)
        button = wx.Button(self, wx.ID_OK, "OK")
        button.SetDefault()

        # Set sizer.
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.text, 1, wx.EXPAND)
        sizer.Add(button, 0, wx.EXPAND)
        self.SetSizer(sizer)

        button.Bind(wx.EVT_BUTTON, self.OnClickOk)

    def OnClickOk(self, event):
        if self.text.GetValue() == '':
            show_messange(self.parent, 'No debe dejar vacio')

        else:
            self.Result = int(self.text.GetValue())


