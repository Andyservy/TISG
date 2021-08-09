import wx
import wx.adv
import wx.grid as grid

from Proyecto_TISG.Variables import *
from Proyecto_TISG.data.SERVIRDOR.DATABASE import connection
from Proyecto_TISG.Package import JustInt


def ComercialBillings(self):

    self.cursor = connection().cursor()

    Box_Main = wx.BoxSizer(wx.VERTICAL)

    # Top---------------------------------------------------------------------------------------------------------------

    Box_Top = wx.BoxSizer(wx.HORIZONTAL)
    Box_Resumen = wx.BoxSizer(wx.VERTICAL)
    Box_TopNombre = wx.BoxSizer(wx.VERTICAL)
    Box_TopTipoEmpresa = wx.BoxSizer(wx.HORIZONTAL)

    self.cursor.execute(Consult_DataEmpresa)
    DataEmpresa = self.cursor.fetchone()

    label_ResumenEmpresa = wx.StaticText(self, -1, str(DataEmpresa[4]),
                                         style=wx.ALIGN_CENTER | wx.ALIGN_BOTTOM)
    Box_Resumen.Add(label_ResumenEmpresa, 1, wx.ALL, 2)
    fontlabel_ResumenEmpresa = wx.Font(15, wx.ROMAN, wx.NORMAL, wx.NORMAL)

    label_Ubicacion = wx.StaticText(self, -1, "{0} Telefono: {1}".format(str(DataEmpresa[2]), DataEmpresa[7]),
                                    style=wx.ALIGN_CENTER | wx.ALIGN_TOP)
    Box_Resumen.Add(label_Ubicacion, 1, wx.EXPAND | wx.ALL)

    label_RazonSocial = wx.StaticText(self, -1, str(DataEmpresa[1]))
    Box_TopNombre.Add(label_RazonSocial, 1, wx.EXPAND | wx.ALL)
    fontlabel_RazonSocial = wx.Font(30, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_ITALIC, wx.NORMAL)

    label_TipoEmpresa = wx.StaticText(self, -1, str(DataEmpresa[6]))
    Box_TopTipoEmpresa.Add(label_TipoEmpresa, 1, wx.EXPAND | wx.ALL, 5)
    fontlabel_Empresa = wx.Font(27, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_ITALIC, wx.NORMAL)

    image1 = wx.Image(Productos_Pres[0], wx.BITMAP_TYPE_PNG).ConvertToBitmap()
    TubosPVC = wx.StaticBitmap(self, -1, image1)
    Box_TopTipoEmpresa.Add(TubosPVC, 1, wx.EXPAND, wx.ALL)

    image2 = wx.Image(Productos_Pres[1], wx.BITMAP_TYPE_PNG).ConvertToBitmap()
    Pacasmayo = wx.StaticBitmap(self, -1, image2)
    Box_TopTipoEmpresa.Add(Pacasmayo, 1, wx.EXPAND, wx.ALL)

    image3 = wx.Image(Productos_Pres[2], wx.BITMAP_TYPE_PNG).ConvertToBitmap()
    Fierros = wx.StaticBitmap(self, -1, image3)
    Box_TopTipoEmpresa.Add(Fierros, 1, wx.EXPAND, wx.ALL)

    # Cliente-----------------------------------------------------------------------------------------------------------

    miniBox_Cliente = wx.StaticBox(self, wx.ID_ANY, 'Cliente')
    Box_Cliente = wx.StaticBoxSizer(miniBox_Cliente, wx.HORIZONTAL)
    Box_Cliente1 = wx.BoxSizer(wx.VERTICAL)
    Box_Cliente2 = wx.BoxSizer(wx.VERTICAL)
    Box_Nombre = wx.BoxSizer(wx.HORIZONTAL)
    Box_DNI = wx.BoxSizer(wx.HORIZONTAL)
    Box_ClienteRUC = wx.BoxSizer(wx.HORIZONTAL)

    label_Nombre = wx.StaticText(self, -1, 'Nombre:')
    Box_Nombre.Add(label_Nombre, 1, wx.EXPAND)

    ctrl_Nombre = wx.TextCtrl(self, -1)
    Box_Nombre.Add(ctrl_Nombre, 1, wx.EXPAND)

    Box_Cliente1.Add(Box_Nombre, 1, wx.EXPAND | wx.ALL, 5)

    label_DNI = wx.StaticText(self, -1, 'DNI:')
    Box_DNI.Add(label_DNI, 1, wx.EXPAND)

    ctrl_DNI = wx.TextCtrl(self, -1)
    Box_DNI.Add(ctrl_DNI, 1, wx.EXPAND)
    JustInt(ctrl_DNI)

    Box_Cliente1.Add(Box_DNI, 1, wx.EXPAND | wx.ALL, 5)

    RadioBox_Responsable = wx.RadioBox(self, label='Responsable', choices=ResponsableCompraVenta,
                                       majorDimension=1, style=wx.RA_SPECIFY_ROWS)
    Box_Cliente1.Add(RadioBox_Responsable, 1, wx.EXPAND | wx.ALL, 5)

    label_Domicilio = wx.StaticText(self, -1, 'Domicilio:')
    Box_Cliente2.Add(label_Domicilio, 1, wx.EXPAND)

    ctrl_Domicilio = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
    Box_Cliente2.Add(ctrl_Domicilio, 1, wx.EXPAND | wx.ALL, 5)

    label_ClienteRUC = wx.StaticText(self, -1, 'RUC:')
    Box_ClienteRUC.Add(label_ClienteRUC, 1, wx.EXPAND)

    ctrl_ClienteRUC = wx.TextCtrl(self, -1)
    Box_ClienteRUC.Add(ctrl_ClienteRUC, 1, wx.EXPAND)
    JustInt(ctrl_ClienteRUC)

    Box_Cliente2.Add(Box_ClienteRUC, 1, wx.EXPAND | wx.ALL, 5)

    Box_Cliente.Add(Box_Cliente1, 1, wx.EXPAND)
    Box_Cliente.Add(Box_Cliente2, 1, wx.EXPAND)

    # Concepto----------------------------------------------------------------------------------------------------------

    miniBox_Concepto = wx.StaticBox(self, wx.ID_ANY, 'Concepto')
    Box_Concepto = wx.StaticBoxSizer(miniBox_Concepto, wx.HORIZONTAL)
    Box_CompraVenta = wx.BoxSizer(wx.HORIZONTAL)
    Box_Compra = wx.BoxSizer(wx.VERTICAL)
    Box_TipoPago = wx.BoxSizer(wx.HORIZONTAL)
    mini_Box_Periodo = wx.StaticBox(self, wx.ID_ANY, 'Periodo')
    Box_Periodo = wx.StaticBoxSizer(mini_Box_Periodo, wx.HORIZONTAL)
    Box_Factura = wx.BoxSizer(wx.VERTICAL)

    Compra = wx.RadioButton(self, 11, label='Compra', style=wx.RB_GROUP)
    Box_CompraVenta.Add(Compra, 1, wx.EXPAND)

    Venta = wx.RadioButton(self, 22, label='Venta')
    Box_CompraVenta.Add(Venta, 1, wx.EXPAND)

    Box_Compra.Add(Box_CompraVenta, 1, wx.EXPAND)
    Box_Concepto.Add(Box_Compra, 1, wx.EXPAND)

    label_TipoPago = wx.StaticText(self, -1, 'Tipo de pago:')
    Box_TipoPago.Add(label_TipoPago, 1, wx.EXPAND)

    choc_Pago = wx.Choice(self, choices=TipoDePago)
    choc_Pago.SetSelection(4)
    Box_TipoPago.Add(choc_Pago, 1, wx.EXPAND)

    Box_Compra.Add(Box_TipoPago, 1, wx.EXPAND)

    label_From = wx.StaticText(self, -1, 'Desde:')
    Box_Periodo.Add(label_From, 1, wx.EXPAND)

    date_From = wx.adv.GenericDatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime)
    Box_Periodo.Add(date_From, 1, wx.EXPAND)

    label_Until = wx.StaticText(self, -1, 'Hasta:')
    Box_Periodo.Add(label_Until, 1, wx.EXPAND)

    date_Until = wx.adv.GenericDatePickerCtrl(self, wx.ID_ANY)
    Box_Periodo.Add(date_Until, 1, wx.EXPAND)

    label_Comprobante = wx.StaticText(self, -1, Comprobante[1])
    label_Comprobante.SetBackgroundColour(self.Color)
    Box_Factura.Add(label_Comprobante, 1, wx.EXPAND)

    label_Numeracion = wx.StaticText(self, -1, 'F')
    label_Numeracion.SetBackgroundColour('#323754')
    Box_Factura.Add(label_Numeracion, 1, wx.EXPAND)
    # Numeracion regla aquí: https://www.sunat.gob.pe/legislacion/superin/2017/anexosI-II-III-IV-318-2017.pdf
    # Numeracion: https://okasesores.es/facturas-emitidas-orden-numeracion-fecha-correlativas/

    Box_Concepto.Add(Box_Periodo, 1, wx.EXPAND | wx.ALL, 5)
    Box_Concepto.Add(Box_Factura, 1, wx.EXPAND | wx.ALL, 5)
    # Parametros de la Factura------------------------------------------------------------------------------------------

    # Productos---------------------------------------------------------------------------------------------------------

    Box_Productos = wx.BoxSizer(wx.VERTICAL)
    Box_Confirmar = wx.BoxSizer(wx.HORIZONTAL)
    Box_AgregarBorrar = wx.BoxSizer(wx.HORIZONTAL)
    BoxLabel_Total = wx.BoxSizer(wx.VERTICAL)
    BoxCtrl_Total = wx.BoxSizer(wx.VERTICAL)

    Tabla_Articulos = grid.Grid(self, -1)
    Box_Productos.Add(Tabla_Articulos, 1, wx.EXPAND)
    Tabla_Articulos.CreateGrid(4, 10)

    btn_Agregar = wx.Button(self, -1, 'Agregar')
    Box_AgregarBorrar.Add(btn_Agregar, 1, wx.EXPAND | wx.ALL, 10)

    btn_Quitar = wx.Button(self, -1, 'Quitar')
    Box_AgregarBorrar.Add(btn_Quitar, 1, wx.EXPAND | wx.ALL, 10)

    label_SubTotal = wx.StaticText(self, -1, 'Sub Total')
    label_IGV = wx.StaticText(self, -1, 'IGV')
    label_Total = wx.StaticText(self, -1, 'Total')
    BoxLabel_Total.Add(label_SubTotal, 1, wx.EXPAND | wx.ALL, 5)
    BoxLabel_Total.Add(label_IGV, 1, wx.EXPAND | wx.ALL, 5)
    BoxLabel_Total.Add(label_Total, 1, wx.EXPAND | wx.ALL, 5)

    ctrl_SubTotal = wx.TextCtrl(self, -1)
    ctrl_IGV = wx.TextCtrl(self, -1)
    ctrl_Total = wx.TextCtrl(self, -1)
    BoxCtrl_Total.Add(ctrl_SubTotal, 1, wx.EXPAND | wx.ALL, 5)
    BoxCtrl_Total.Add(ctrl_IGV, 1, wx.EXPAND | wx.ALL, 5)
    BoxCtrl_Total.Add(ctrl_Total, 1, wx.EXPAND | wx.ALL, 5)

    Box_Confirmar.Add(Box_AgregarBorrar, 5, wx.EXPAND)
    Box_Confirmar.Add(BoxLabel_Total, 1, wx.EXPAND)
    Box_Confirmar.Add(BoxCtrl_Total, 3, wx.EXPAND)

    Box_Productos.Add(Box_Confirmar, 1, wx.EXPAND)

    # Estilos

    label_ResumenEmpresa.SetFont(fontlabel_ResumenEmpresa)
    label_RazonSocial.SetFont(fontlabel_RazonSocial)
    label_TipoEmpresa.SetFont(fontlabel_Empresa)

    Box_TopNombre.Add(Box_TopTipoEmpresa, 1, wx.EXPAND | wx.ALL, 5)
    Box_Top.Add(Box_Resumen, 1, wx.EXPAND | wx.ALL, 2)
    Box_Top.Add(Box_TopNombre, 1, wx.EXPAND | wx.ALL, 5)

    Box_Main.Add(Box_Top, 1, wx.EXPAND | wx.ALL, 5)
    Box_Main.Add(Box_Cliente, 3, wx.EXPAND | wx.ALL, 5)
    Box_Main.Add(Box_Concepto, 2, wx.EXPAND | wx.ALL, 5)
    Box_Main.Add(Box_Productos, 3, wx.EXPAND | wx.ALL, 5)

    return Box_Main



