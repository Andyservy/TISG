# Packages Third-party
import wx
import wx.lib.agw.gradientbutton as gb

# Package Project

from Proyecto_TISG.Package.Formulary import Verificacion
from Proyecto_TISG.Frame_main.Configuración import RestablecimientoDeDatos


class TopUsuario(wx.Panel):

    def __init__(self, parent):
        super(TopUsuario, self).__init__(parent, style=wx.BORDER_NONE)

        # self.SetSize(500, 700)
        self.User = Verificacion(self).User
        self.SetBackgroundColour(self.Parent.Color)
        self.init_GUI()

    def init_GUI(self):
        # CONTENEDORES

        box_main = wx.BoxSizer(wx.VERTICAL)
        Data_sesión = wx.BoxSizer(wx.HORIZONTAL)
        Data = wx.BoxSizer(wx.VERTICAL)

        # WIDGETS
        Greeting = wx.StaticText(self, -1, label='NEGOCIOS CULQUI',
                                 style=wx.ALIGN_CENTER)
        Acero = wx.StaticText(self, -1, label='ACEROS AREQUIPA', style=wx.ALIGN_CENTER)
        Data.Add(Greeting, 1, wx.EXPAND | wx.ALL, 10)
        Data.Add(Acero, 1, wx.EXPAND | wx.LEFT, 10)
        Data_sesión.Add(Data, 1, wx.EXPAND | wx.ALL, 10)

        bmpBtn_Configuration = gb.GradientButton(self, wx.ID_ANY, label="Configuración")
        Data_sesión.Add(bmpBtn_Configuration, 1, wx.EXPAND | wx.ALL, 20)

        # AÑADIENDO LOS BOX AL BOX PRINCIPAL
        box_main.Add(Data_sesión, 1, wx.EXPAND)

        # CONFIGURANDO SIZER
        self.SetSizer(box_main)

        # COLOUR and SIZE
        Font_Greeting = wx.Font(25, wx.MODERN, wx.NORMAL, wx.NORMAL)
        Greeting.SetBackgroundColour(self.Parent.Color)
        Greeting.SetForegroundColour("#FFFFFF")
        Greeting.SetFont(Font_Greeting)

        Font_Acero = wx.Font(35, wx.MODERN, wx.NORMAL, wx.NORMAL)
        Acero.SetForegroundColour('#FFFFFF ')
        Acero.SetFont(Font_Acero)

        Font_bmp_configuration = wx.Font(20, wx.SCRIPT, wx.NORMAL, wx.NORMAL)
        bmpBtn_Configuration.SetFont(Font_bmp_configuration)
        bmpBtn_Configuration.SetForegroundColour("#FFFFFF")

        # EVENTOS
        bmpBtn_Configuration.Bind(wx.EVT_BUTTON, self.OnClick_Configuracion)

    def OnClick_Configuracion(self, event):
        # Verificar
        Verificacion(self).ShowModal()

    # VERIFICACIÓN_Configuración
    def OnClickOK(self):
        # Dar acceso
        RestablecimientoDeDatos(self).ShowModal()

    def OnClickCancel(self, event):
        Verificacion(self).Close()


# from Proyecto_TISG.Frame_main import FrameMain
