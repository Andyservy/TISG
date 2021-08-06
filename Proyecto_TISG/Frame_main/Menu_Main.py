import wx

from Proyecto_TISG.Variables import *
from Proyecto_TISG.Package import Btnbicolor, PhotoCtrl

# Scripts
from Proyecto_TISG.Frame_main.Facturación import DataFacturacion, ComercialBillings


class MenuTab(wx.Notebook):
    def __init__(self, parent):
        super(MenuTab, self).__init__(parent, style=wx.NB_LEFT | wx.BORDER_NONE)

        self.AddPage(Facturacion(self), "Facturación")
        self.SetBackgroundColour(Color)


class Facturacion(wx.Panel, MenuTab):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.SetBackgroundColour(Color)
        self.init_GUI()

    def init_GUI(self):
        Box_Main = wx.BoxSizer(wx.VERTICAL)
        Box_TopBar = wx.BoxSizer(wx.HORIZONTAL)
        Box_Billing = wx.BoxSizer(wx.VERTICAL)
        Box_Preview = wx.BoxSizer(wx.VERTICAL)
        Box_seek = wx.BoxSizer(wx.VERTICAL)

        # Widgets
        Btn_CommercialBilling = wx.Button(self, -1, "Facturación comercial")
        Box_Billing.Add(Btn_CommercialBilling, 1, wx.EXPAND | wx.ALL, 15)

        Btn_SumUpBilling = wx.Button(self, -1, "Factura recapitulativa")
        Box_Billing.Add(Btn_SumUpBilling, 1, wx.EXPAND | wx.ALL, 15)

        Btn_PromissoryNote = wx.Button(self, -1, "Pagaré")
        Box_Billing.Add(Btn_PromissoryNote, 1, wx.EXPAND | wx.ALL, 15)

        Setting_Belling = wx.StaticBox(self, wx.ID_ANY, "Avanzado")
        MiniBox = wx.StaticBoxSizer(Setting_Belling, wx.VERTICAL)

        Btn_Descripcion = wx.Button(self, -1, "Refactorizar")
        MiniBox.Add(Btn_Descripcion, 1, wx.EXPAND | wx.CENTER, 10)
        Box_Preview.Add(MiniBox, 1, wx.EXPAND | wx.ALL, 10)

        Image1 = wx.Image(Preview_Billing[3], wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.bmp_Focusless = wx.StaticBitmap(self, -1, Image1)
        Box_Preview.Add(self.bmp_Focusless, 3, wx.EXPAND | wx.ALL, 15)
        PhotoCtrl(self, Preview_Billing[3], self.bmp_Focusless)

        BTN = [Btn_CommercialBilling, Btn_SumUpBilling, Btn_PromissoryNote, Btn_Descripcion]
        Btnbicolor(BTN, '#2C4158', '#384A5F')

        # Contenedores
        Box_TopBar.Add(Box_Billing, 3, wx.EXPAND)
        Box_TopBar.Add(Box_Preview, 1, wx.EXPAND)

        Box_Main.Add(Box_TopBar, 1, wx.EXPAND)

        self.SetSizer(Box_Main)

        # Eventos
        Btn_CommercialBilling.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterCB)
        Btn_SumUpBilling.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterSUB)
        Btn_PromissoryNote.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterPN)
        Btn_CommercialBilling.Bind(wx.EVT_BUTTON, self.OnCliclkCB)

        Btn_Descripcion.Bind(wx.EVT_BUTTON, self.OnClickD)

    def OnEnterCB(self, event):
        Image0 = wx.Image(Preview_Billing[0], wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.bmp_Focusless.SetBitmap(wx.Bitmap(Image0))
        PhotoCtrl(self, Preview_Billing[0], self.bmp_Focusless)
        event.Skip()

    def OnEnterSUB(self, event):
        Image1 = wx.Image(Preview_Billing[1], wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.bmp_Focusless.SetBitmap(wx.Bitmap(Image1))
        PhotoCtrl(self, Preview_Billing[1], self.bmp_Focusless)
        event.Skip()

    def OnEnterPN(self, event):
        Image2 = wx.Image(Preview_Billing[2], wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.bmp_Focusless.SetBitmap(wx.Bitmap(Image2))
        PhotoCtrl(self, Preview_Billing[2], self.bmp_Focusless)
        event.Skip()

    def OnClickD(self, event):
        DataFacturacion(self).ShowModal()

    def OnCliclkCB(self, event):
        ComercialBillings(self)

# Referencia
# Factura ordinaria = https://www.finanzarel.com/blog/factura-ordinaria-caracteristicas-ejemplos-y-plantillas/
# Factura resumen = https://iciredimpagados.com/blog/factura-recapitulativa/
# Pagaré = https://novicap.com/guia-financiera/pagare-que-es/
# Focus less = https://www.pinterest.es/pin/729935052087828216/