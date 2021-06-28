# Packages Third-party
import wx
import wx.lib.agw.gradientbutton as gb

# Package Project

from Proyecto_TISG.Package.Formulary import Verificacion
from Proyecto_TISG.Frame_main.Configuración import Restablecimiento_de_datos
from Proyecto_TISG.Package import Btnbicolor, ShapedButton


class Menu_Main(wx.Panel):

    def __init__(self, parent):
        super(Menu_Main, self).__init__(parent, -1)

        self.Color = self.Parent.Color
        self.SetBackgroundColour(self.Color)
        # self.SetSize(500, 700)

        self.Verificacion = Verificacion(self)

        self.check()
        self.init_GUI()

        self.Show()

    def check(self):
        global User
        User = Verificacion(self).User

    def init_GUI(self):

        # CONTENEDORES

        box_main = wx.BoxSizer(wx.VERTICAL)
        Data_sesión = wx.BoxSizer(wx.HORIZONTAL)
        Items_colum1 = wx.BoxSizer(wx.VERTICAL)
        Items_colum2 = wx.BoxSizer(wx.VERTICAL)
        Items = wx.BoxSizer(wx.HORIZONTAL)

        # WIDGETS
        Greeting = wx.StaticText(self, -1, label=("Nombre_Entrada de Usuario: %s" % str(User)),
                                 style=wx.ALIGN_CENTER)
        Data_sesión.Add(Greeting, 2, wx.EXPAND | wx.ALL, 10)

        bmpBtn_Configuration = gb.GradientButton(self, wx.ID_ANY, label="Configuración")
        Data_sesión.Add(bmpBtn_Configuration, 1, wx.EXPAND | wx.ALL, 20)

        Facturación = wx.Button(self, -1, 'FACTURACIÓN')
        Inventario = wx.Button(self, -1, 'INVENTARIO')
        Utilería = wx.Button(self, -1, 'UTILERÍA')
        Estadísticas = wx.Button(self, -1, 'ESTADÍSTICAS')
        Agenda = wx.Button(self, -1, 'AGENDA')
        Nomina = wx.Button(self, -1, 'NOMINA')

        Items_List = [Facturación, Inventario, Utilería, Estadísticas, Agenda, Nomina]

        Items_STYLES_1 = [Facturación, Inventario, Utilería]
        Items_Styles_2 = [Estadísticas, Agenda, Nomina]

        for _ in Items_STYLES_1:
            Items_colum1.Add(_, 1, wx.EXPAND | wx.ALL, 10)

        for _ in Items_Styles_2:
            Items_colum2.Add(_, 1, wx.EXPAND | wx.ALL, 10)

        Items.Add(Items_colum1, 1, wx.EXPAND)
        Items.Add(Items_colum2, 1, wx.EXPAND)

        # AÑADIENDO LOS BOX AL BOX PRINCIPAL
        box_main.Add(Data_sesión, 1, wx.EXPAND)
        box_main.Add(Items, 3, wx.EXPAND)

        # CONFIGURANDO SIZER
        self.SetSizer(box_main)

        # COLOUR and SIZE
        Font_Greeting = wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL)
        Greeting.SetBackgroundColour(self.Color)
        Greeting.SetForegroundColour("#FFFFFF")
        Greeting.SetFont(Font_Greeting)

        Font_bmp_configuration = wx.Font(20, wx.SCRIPT, wx.NORMAL, wx.NORMAL)
        bmpBtn_Configuration.SetFont(Font_bmp_configuration)
        bmpBtn_Configuration.SetForegroundColour("#FFFFFF")

        for button_font in Items_List:
            Font_Items = wx.Font(20, wx.SWISS, wx.NORMAL, wx.LIGHT)
            button_font.SetFont(Font_Items)
            button_font.SetForegroundColour("#7D95B7")

        # ESTILOS DE BOTONES

        Btnbicolor(Items_List, '#2C4158', '#384A5F')

        # EVENTOS
        bmpBtn_Configuration.Bind(wx.EVT_BUTTON, self.OnClick_Configuracion)
        Facturación.Bind(wx.EVT_BUTTON, self.OnClick_Facturacion)

    def OnClick_Configuracion(self, event):

        # Verificar
        self.Verificacion.Centre()
        self.Verificacion.ShowModal()

    def OnClick_Facturacion(self, event):
        self.Hide()

        Pl_Facturacion = Facturacion(self.Parent)
        self.Parent.sizer.Add(Pl_Facturacion, wx.EXPAND)

    # VERIFICACIÓN_Configuración
    def OnClickOK(self):
        # Dar acceso
        Confi_sesion = Restablecimiento_de_datos(self)
        Confi_sesion.ShowModal()

    def OnClickCancel(self, event):
        self.Verificacion.Close()


class Facturacion(Menu_Main):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.SetBackgroundColour("#212F3C")

        self.__init_GUI()

        self.Layout()

    def __init_GUI(self):
        Box_Main = wx.BoxSizer(wx.VERTICAL)
        Box_TopBar = wx.BoxSizer(wx.HORIZONTAL)

        BTN_Home = ShapedButton(self,
                                wx.Bitmap(
                                    'C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home.png'),
                                wx.Bitmap(
                                    'C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home_click.png'),
                                wx.Bitmap(
                                    'C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home_click.png'))
        Box_TopBar.Add(BTN_Home, 1, wx.EXPAND | wx.ALL, 10)

        Box_Main.Add(Box_TopBar, 1, wx.EXPAND)
        self.SetSizer(Box_Main)
