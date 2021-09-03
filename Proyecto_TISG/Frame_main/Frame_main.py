# Packages Third-party
import wx
import wx.lib.agw.gradientbutton as gb
# Package Project
from Proyecto_TISG.Frame_main.Configuración import RestablecimientoDeDatos
from Proyecto_TISG.Package.Formulary import Verificacion
from Proyecto_TISG import connection


class FrameMain(wx.Frame):
    def __init__(self, parent, title):
        super(FrameMain, self).__init__(parent, title=title, size=(1000, 730))
        self.Attribute()

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.TopUsuario = FrameMain.__subclasses__()[1](self)
        self.MenuTab = FrameMain.__subclasses__()[0](self)

        self.GUI_init()

        self.Show()
        self.SetMinSize(self.GetSize())
        self.Centre()

    def Attribute(self):
        self.Color = "#212F3C"
        self.User_Name = Verificacion(self).User

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
        self.sizer.Add(self.TopUsuario, 1, wx.EXPAND)
        self.sizer.Add(self.MenuTab, 4, wx.EXPAND)

    def OnClickCancel(self, event):
        self.Close()


class MenuTab(wx.Notebook, FrameMain):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, style=wx.NB_LEFT | wx.BORDER_NONE)
        self.Attribute()

        Facturacion = MenuTab.__subclasses__()[0]
        self.AddPage(Facturacion(self), "Facturación")
        self.SetBackgroundColour(self.Color)


class TopUsuario(wx.Panel, FrameMain):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, style=wx.BORDER_NONE)
        self.Attribute()
        # self.SetSize(500, 700)
        self.User = Verificacion(self).User
        self.SetBackgroundColour(self.Color)
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
        Data.Add(Greeting, 1, wx.EXPAND | wx.ALL, 5)
        Data.Add(Acero, 1, wx.EXPAND | wx.LEFT, 5)
        Data_sesión.Add(Data, 1, wx.EXPAND | wx.ALL, 10)

        bmpBtn_Configuration = gb.GradientButton(self, wx.ID_ANY, label="Configuración")
        Data_sesión.Add(bmpBtn_Configuration, 1, wx.EXPAND | wx.ALL, 20)

        # AÑADIENDO LOS BOX AL BOX PRINCIPAL
        box_main.Add(Data_sesión, 1, wx.EXPAND)

        # CONFIGURANDO SIZER
        self.SetSizer(box_main)

        # COLOUR and SIZE
        Font_Greeting = wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL)
        Greeting.SetBackgroundColour(self.Color)
        Greeting.SetForegroundColour("#FFFFFF")
        Greeting.SetFont(Font_Greeting)

        Font_Acero = wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL)
        Acero.SetForegroundColour('#FFFFFF ')
        Acero.SetFont(Font_Acero)

        Font_bmp_configuration = wx.Font(15, wx.SCRIPT, wx.NORMAL, wx.NORMAL)
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


"""
Al usar show () fuera de la definición de los atributos, se debe establecer una variable que herede la clase que 
acumula al Frame, ya que con esto se está resolviendo el primer parámetro, que en este caso sería self (solo admite 
de tipo window, y la variable a la que asignamos el frame se vuelve de esa clase)
Example:
- Frame.Show(self:No esta llenado, Bool: True)
- Variable = Frame(Parámetros)
  Variable.Show(self:Variable, Bool:True)
"""
