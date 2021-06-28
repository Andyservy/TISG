import wx


class Btnbicolor(object):

    def __init__(self, botones, color_0, color_1):

        """
        Solo se considerara dos valores en Color, ya que esos interaran
        """
        try:
            self.ON = color_1
        except IndexError:
            print('Se omitieron valores', Btnbicolor, ',se consideran solo dos valores')
            exit()

        self.Coletionbutton(botones, color_0)
        self.OFF = color_0

    def Coletionbutton(self, Botones_stylecmn, Colour):

        for Button in Botones_stylecmn:
            Button.SetBackgroundColour(Colour)
            Button.SetWindowStyleFlag(wx.BORDER_NONE)
            self.builtButtons(Button)

    def builtButtons(self, BTN):
        BTN.Bind(wx.EVT_ENTER_WINDOW, self.OnEnter)
        BTN.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeave)
        BTN.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        BTN.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)

    def OnLeftDown(self, event):
        BTN = event.GetEventObject()

        BTN.SetBackgroundColour(self.OFF)

        event.Skip()

    def OnLeftUp(self, event):
        BTN = event.GetEventObject()

        BTN.SetBackgroundColour(self.ON)

        event.Skip()

    def OnEnter(self, event):
        BTN = event.GetEventObject()

        BTN.SetBackgroundColour(self.ON)
        """
        No se si se nesecita un skip() en esta parte, ni en OnEnter
        Si ocurre algún error, revisarlo aquí
        """
        # event.Skip()

    def OnLeave(self, event):
        BTN = event.GetEventObject()

        BTN.SetBackgroundColour(self.OFF)
        # event.Skip()


def show_messange(self, message):
    dlg = wx.MessageDialog(None, message, "No valido", wx.OK | wx.ICON_QUESTION)
    if dlg.ShowModal() == wx.ID_YES:
        pass
    dlg.Destroy()
