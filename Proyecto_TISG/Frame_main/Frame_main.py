# Packages Third-party
import wx

# Package Project
from Proyecto_TISG.Frame_main.TOPTAB.Barra_Usuario import TopUsuario
from Proyecto_TISG.Frame_main.Menu_Main import MenuTab
from Proyecto_TISG.Package.Formulary import Verificacion
from Proyecto_TISG import connection


class FrameMain(wx.Frame):
    def __init__(self, parent, title):
        super(FrameMain, self).__init__(parent, title=title, size=(1000, 700))

        self.Centre()

        self.Color = "#212F3C"
        self.User_Name = Verificacion(self).User
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.GUI_init()

        self.Show()

    def GUI_init(self):

        self.SetSizer(self.sizer)

        # Verificación

        Verificacion(self).ShowModal()

        # EVENTOS
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # PANELES PRINCIPALES

    # EVENTOS

    def OnClose(self, event):
        connection().close()

        event.Skip()  # Este evento ya es llamado al apretar x, asi que se debe poner skip para que siga buscando

    # VERIFICACIÓN

    def OnClickOK(self):
        self.sizer.Add(TopUsuario(self), 1, wx.EXPAND)
        self.sizer.Add(MenuTab(self), 4, wx.EXPAND)

    def OnClickCancel(self, event):
        self.Close()


"""
Al usar show () fuera de la definición de los atributos, se debe establecer una variable que herede la clase que 
acumula al Frame, ya que con esto se está resolviendo el primer parámetro, que en este caso sería self (solo admite 
de tipo window, y la variable a la que asignamos el frame se vuelve de esa clase)
Example:
- Frame.Show(self:No esta llenado, Bool: True)
- Variable = Frame(Parámetros)
  Variable.Show(self:Variable, Bool:True)
"""