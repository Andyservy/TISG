# Packages Third-party
import wx

# Package Project
from Proyecto_TISG.Frame_main.Menú_main import Menu_Main
from Proyecto_TISG.Package.Formulary import Verificacion
from Proyecto_TISG import connection


class frame_main(wx.Frame):
    def __init__(self, parent, title, size):
        super(frame_main, self).__init__(parent, title=title, size=size)

        self.Centre()
        self.Color = "#212F3C"

        self.Formulario = Verificacion(self)
        self.User_name = self.Formulario.User

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)

        self.GUI_init()

    def GUI_init(self):
        # Verificación

        self.Formulario.ShowModal()

        # EVENTOS
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # PANELES PRINCIPALES

    def OnClose(self, event):
        connection().close()

        event.Skip()  # Este evento ya es llamado al apretar x, asi que se debe poner skip para que siga buscando

    # VERIFICACIÓN

    def OnClickOK(self):
        Pl_MenuMain = Menu_Main(self)
        self.sizer.Add(Pl_MenuMain, 1, wx.EXPAND)

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
