import wx

from Proyecto_TISG.Variables import *
from Proyecto_TISG.data.SERVIRDOR.DATABASE import connection


class ComercialBillings(wx.Panel):

    def __init__(self, parent):
        super(ComercialBillings, self).__init__(parent)

        self.cursor = connection().cursor()

        Box_Main = wx.BoxSizer(wx.VERTICAL)
        Box_Empresa = wx.StaticBoxSizer(wx.HORIZONTAL, self, 'Culqui Import')
        Box_Resumen = wx.BoxSizer(wx.VERTICAL)
        Box_Cliente = wx.BoxSizer(wx.HORIZONTAL)
        Box_DataFactura = wx.BoxSizer(wx.HORIZONTAL)
        Box_Producto = wx.BoxSizer(wx.VERTICAL)

        # Empresa

        self.cursor.execute(Consult_DataEmpresa)
        DataEmpresa = self.cursor.fetchone()

        label_ResumenEmpresa = wx.StaticText(Box_Empresa.GetStaticBox(), -1, str(DataEmpresa[4]))

        Box_Resumen.Add(label_ResumenEmpresa, 1, wx.EXPAND | wx.ALL, 10)

        Box_Empresa.Add(Box_Resumen, 1, wx.EXPAND)
        Box_Main.Add(Box_Empresa, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(Box_Main)



