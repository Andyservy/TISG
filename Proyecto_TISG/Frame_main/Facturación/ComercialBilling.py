import wx
import wx.adv
import wx.grid as grid

from Proyecto_TISG.Variables import *
from Proyecto_TISG.data.SERVIRDOR.DATABASE import connection
from Proyecto_TISG.Package import JustInt
from Proyecto_TISG.Package import ShapedButton


class ComercialBillings(object):

    def Box(self, parent, boton):
        parent.cursor = connection().cursor()
        Box_Comprobante = wx.BoxSizer(wx.VERTICAL)
        self.parent = parent

        self.Sizers = []
        self.Cliente = []
        self.Producto = []
        self.Fecha = []
        self.Distribucion = []

        Box_Main = wx.GridBagSizer(24, 13)
        # Top---------------------------------------------------------------------------------------------------------------

        parent.cursor.execute(Consult_DataEmpresa)
        DataEmpresa = parent.cursor.fetchone()

        label_ResumenEmpresa = wx.StaticText(parent, -1, str(DataEmpresa[4]))
        Box_Main.Add(label_ResumenEmpresa, pos=(0, 0), span=(0, 10),
                     flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        fontlabel_ResumenEmpresa = wx.Font(16, wx.ROMAN, wx.NORMAL, wx.NORMAL)

        label_Ubicacion = wx.StaticText(parent, -1, "{0} Telefono: {1}".format(str(DataEmpresa[2]), DataEmpresa[7]))
        Box_Main.Add(label_Ubicacion, pos=(1, 1), span=(0, 9),
                     flag=wx.ALIGN_CENTER | wx.ALIGN_TOP | wx.ALL)

        label_RazonSocial = wx.StaticText(parent, -1, str(DataEmpresa[1]))
        Box_Main.Add(label_RazonSocial, pos=(0, 10), span=(0, 4),
                     flag=wx.ALIGN_LEFT | wx.ALL, border=5)
        fontlabel_RazonSocial = wx.Font(30, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_ITALIC, wx.NORMAL)

        label_TipoEmpresa = wx.StaticText(parent, -1, str(DataEmpresa[6]))
        Box_Main.Add(label_TipoEmpresa, pos=(1, 10),
                     flag=wx.ALIGN_RIGHT | wx.ALL)
        fontlabel_Empresa = wx.Font(27, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_ITALIC, wx.NORMAL)

        image1 = wx.Image(Productos_Pres[0], wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        TubosPVC = wx.StaticBitmap(parent, -1, image1)
        Box_Main.Add(TubosPVC, pos=(1, 11))

        image3 = wx.Image(Productos_Pres[2], wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        Fierros = wx.StaticBitmap(parent, -1, image3)
        Box_Main.Add(Fierros, pos=(1, 12))

        image2 = wx.Image(Productos_Pres[1], wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        Pacasmayo = wx.StaticBitmap(parent, -1, image2)
        Box_Main.Add(Pacasmayo, pos=(1, 13))

        # Cliente-----------------------------------------------------------------------------------------------------------
        miniBox_Cliente = wx.StaticBox(parent, wx.ID_ANY, 'Cliente')
        Box_Cliente = wx.StaticBoxSizer(miniBox_Cliente, wx.HORIZONTAL)

        label_Cliente = wx.StaticText(parent, -1, label='Cliente')
        Box_Main.Add(label_Cliente, pos=(1, 0), flag=wx.ALIGN_BOTTOM | wx.LEFT)

        linea = wx.StaticLine(parent)
        linea.SetForegroundColour(parent.Color)
        Box_Main.Add(linea, pos=(2, 0), span=(0, 14), flag=wx.EXPAND | wx.ALIGN_TOP)

        label_Nombre = wx.StaticText(parent, -1, label='Nombre:')
        Box_Main.Add(label_Nombre, pos=(3, 0), flag=wx.LEFT | wx.LEFT, border=5)

        ctrl_Nombre = wx.TextCtrl(parent)
        Box_Main.Add(ctrl_Nombre, pos=(3, 1), span=(0, 3), flag=wx.RIGHT | wx.EXPAND)

        label_DNI = wx.StaticText(parent, -1, 'DNI:')
        Box_Main.Add(label_DNI, pos=(4, 0), flag=wx.LEFT | wx.LEFT, border=5)

        ctrl_DNI = wx.TextCtrl(parent, -1)
        JustInt(ctrl_DNI)
        Box_Main.Add(ctrl_DNI, pos=(4, 1), span=(0, 3), flag=wx.RIGHT | wx.EXPAND)

        label_ClienteRUC = wx.StaticText(parent, -1, 'RUC:')
        Box_Main.Add(label_ClienteRUC, pos=(5, 0), flag=wx.ALIGN_LEFT | wx.LEFT, border=5)
        label_ClienteRUC.Show()

        ctrl_ClienteRUC = wx.TextCtrl(parent, -1)
        Box_Main.Add(ctrl_ClienteRUC, pos=(5, 1), span=(0, 3), flag=wx.EXPAND)
        JustInt(ctrl_ClienteRUC)
        ctrl_ClienteRUC.Show()

        RadioBox_Responsable = wx.RadioBox(parent, label='Responsable', choices=ResponsableCompraVenta,
                                           majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        Box_Main.Add(RadioBox_Responsable, pos=(5, 4), span=(0, 2), flag=wx.EXPAND | wx.ALL, border=5)
        self.Distribucion.append(RadioBox_Responsable)

        RadioBox_Concepto = wx.RadioBox(parent, label='Concepto', choices=['Venta', 'Compra'],
                                        majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        Box_Main.Add(RadioBox_Concepto, pos=(5, 6), span=(0, 2), flag=wx.EXPAND | wx.ALL, border=5)
        self.Distribucion.append(RadioBox_Concepto)

        label_TipoPago = wx.StaticText(parent, -1, 'Tipo de pago:')
        Box_Main.Add(label_TipoPago, pos=(4, 4), border=5)

        choc_Pago = wx.Choice(parent, choices=TipoDePago)
        choc_Pago.SetSelection(2)
        Box_Main.Add(choc_Pago, pos=(4, 5), span=(0, 3), flag=wx.EXPAND)

        label_From = wx.StaticText(parent, -1, 'Desde:')
        self.Fecha.append(label_From)
        Box_Main.Add(label_From, pos=(3, 4))

        date_From = wx.adv.GenericDatePickerCtrl(parent, wx.ID_ANY, wx.DefaultDateTime)
        Box_Main.Add(date_From, pos=(3, 5))
        self.Fecha.append(date_From)

        label_Until = wx.StaticText(parent, -1, 'Hasta:')
        self.Fecha.append(label_Until)
        Box_Main.Add(label_Until, pos=(3, 6))

        date_Until = wx.adv.GenericDatePickerCtrl(parent, wx.ID_ANY)
        self.Fecha.append(date_Until)
        Box_Main.Add(date_Until, pos=(3, 7))

        label_Domicilio = wx.StaticText(parent, -1, 'Domicilio:')
        Box_Main.Add(label_Domicilio, pos=(3, 8), flag=wx.EXPAND | wx.ALL, border=5)

        ctrl_Domicilio = wx.TextCtrl(parent, -1, style=wx.TE_MULTILINE)
        Box_Main.Add(ctrl_Domicilio, pos=(4, 8), span=(2, 3), flag=wx.EXPAND | wx.ALL, border=5)

        Añadir_Inventario = wx.CheckBox(parent, -1, label='Añadir al inventario')
        Añadir_Inventario.Hide()
        Box_Main.Add(Añadir_Inventario, pos=(3, 11), span=(0, 2))

        label_Comprobante = wx.StaticText(parent, -1, Comprobante[1], style=wx.ALIGN_CENTER)
        label_Comprobante.SetBackgroundColour(parent.Color)
        fontlabel_Comprobante = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)

        Box_Comprobante.Add(label_Comprobante, 1, wx.EXPAND)

        # Apuntamos la serie con una consulta

        Box_Numeracion = wx.BoxSizer(wx.HORIZONTAL)

        parent.cursor.execute(Conteo_Factura)
        nFilas = parent.cursor.fetchone()

        label_Serie = wx.StaticText(parent, -1, 'F-', style=wx.ALIGN_RIGHT)
        label_Serie.SetBackgroundColour('#323754')
        Box_Numeracion.Add(label_Serie, 1, wx.EXPAND)

        label_Num = wx.StaticText(parent, -1, '{0}'.format(nFilas[0] + 1))
        label_Num.SetBackgroundColour('#323754')
        Box_Numeracion.Add(label_Num, 1, wx.EXPAND)

        Box_Comprobante.Add(Box_Numeracion, 1, wx.EXPAND)

        Box_Main.Add(Box_Comprobante, pos=(4, 11), span=(2, 4), flag=wx.EXPAND)

        self.Cliente.append(label_ClienteRUC)
        self.Cliente.append(ctrl_ClienteRUC)
        self.Cliente.append(label_Comprobante)
        self.Cliente.append(Añadir_Inventario)
        self.Cliente.append(label_Serie)

        # Numeracion regla aquí: https://www.sunat.gob.pe/legislacion/superin/2017/anexosI-II-III-IV-318-2017.pdf
        # Numeracion: https://okasesores.es/facturas-emitidas-orden-numeracion-fecha-correlativas/

        # Productos---------------------------------------------------------------------------------------------------------

        Tabla_Articulos = grid.Grid(parent, -1)
        Box_Main.Add(Tabla_Articulos, pos=(6, 0), span=(0, 12))
        Tabla_Articulos.CreateGrid(8, 7)
        Tabla_Articulos.SetRowLabelSize(0)

        Tabla_Articulos.SetColLabelValue(0, "Codigo")
        Tabla_Articulos.SetColLabelValue(1, "Cant.")
        Tabla_Articulos.SetColLabelValue(2, "Descripcion")
        Tabla_Articulos.SetColLabelValue(3, "Precio (s/.)")
        Tabla_Articulos.SetColLabelValue(4, "Precio de Venta (s/.)")
        Tabla_Articulos.SetColLabelValue(5, "IVA")
        Tabla_Articulos.SetColLabelValue(6, "SubTotal (s/.)")

        Tabla_Articulos.SetColSize(0, 50)
        Tabla_Articulos.SetColSize(1, 100)
        Tabla_Articulos.SetColSize(2, 350)
        Tabla_Articulos.SetColSize(3, 150)
        Tabla_Articulos.SetColSize(4, 150)
        Tabla_Articulos.SetColSize(5, 150)
        Tabla_Articulos.SetColSize(6, 150)

        Tabla_Articulos.HideCol(4)

        attr = grid.GridCellAttr()
        attr.SetReadOnly(True)
        Tabla_Articulos.SetColAttr(0, attr)

        for _ in range(5):
            Tabla_Articulos.DisableColResize(_)
            Tabla_Articulos.DisableRowResize(_)

        _ = Tabla_Articulos.GetNumberRows()
        while _ > 0:
            _ = _ - 1
            Tabla_Articulos.SetCellValue(_, 0, "{0}".format(_ + 1))

        Tabla_Articulos.DisableColResize(0)
        Tabla_Articulos.DisableColResize(1)
        Tabla_Articulos.DisableColResize(2)
        Tabla_Articulos.DisableColResize(3)
        Tabla_Articulos.DisableColResize(4)
        Tabla_Articulos.DisableColResize(5)
        Tabla_Articulos.DisableColResize(6)

        self.Producto.append(Tabla_Articulos)
        Tabla_Articulos.ForceRefresh()

        btn_Guardar = wx.Button(parent, -1, 'Guardar')
        Box_Main.Add(btn_Guardar, pos=(7, 1), span=(2, 3), flag=wx.EXPAND)

        btn_Agregar = wx.Button(parent, -1, 'Agregar')
        Box_Main.Add(btn_Agregar, pos=(7, 4), span=(0, 2), flag=wx.EXPAND)

        btn_Quitar = wx.Button(parent, -1, 'Quitar')
        Box_Main.Add(btn_Quitar, pos=(8, 4), span=(0, 2), flag=wx.EXPAND)

        label_SubTotal = wx.StaticText(parent, -1, 'Sub Total')
        label_IGV = wx.StaticText(parent, -1, 'IGV')
        label_Total = wx.StaticText(parent, -1, 'Total')
        Box_Main.Add(label_SubTotal, pos=(7, 10), span=(0, 2))
        Box_Main.Add(label_IGV, pos=(8, 10), span=(0, 2))
        Box_Main.Add(label_Total, pos=(9, 10), span=(0, 2))

        ctrl_SubTotal = wx.TextCtrl(parent, -1, style=wx.TE_READONLY)
        ctrl_IGV = wx.TextCtrl(parent, -1, style=wx.TE_READONLY)
        ctrl_Total = wx.TextCtrl(parent, -1, style=wx.TE_READONLY)
        Box_Main.Add(ctrl_SubTotal, pos=(7, 12), span=(0, 2), flag=wx.EXPAND)
        Box_Main.Add(ctrl_IGV, pos=(8, 12), span=(0, 2), flag=wx.EXPAND)
        Box_Main.Add(ctrl_Total, pos=(9, 12), span=(0, 2), flag=wx.EXPAND | wx.ALIGN_TOP)

        btn_Regresar = ShapedButton(parent, wx.Bitmap(Icon_Home[0]), wx.Bitmap(Icon_Home[1]), wx.Bitmap(Icon_Home[0]))
        Box_Main.Add(btn_Regresar, pos=(7, 0), span=(3, 0))

        label_ResumenEmpresa.SetFont(fontlabel_ResumenEmpresa)
        label_RazonSocial.SetFont(fontlabel_RazonSocial)
        label_TipoEmpresa.SetFont(fontlabel_Empresa)
        label_Comprobante.SetFont(fontlabel_Comprobante)

        # EVENTOS

        RadioBox_Responsable.Bind(wx.EVT_RADIOBOX, self.Responsable)
        RadioBox_Concepto.Bind(wx.EVT_RADIOBOX, self.CompraVenta)
        btn_Regresar.Bind(wx.EVT_BUTTON, self.OnClickRegresar)
        btn_Agregar.Bind(wx.EVT_BUTTON, self.OnClickAgregar)
        btn_Quitar.Bind(wx.EVT_BUTTON, self.OnClickQuitar)
        btn_Guardar.Bind(wx.EVT_BUTTON, self.OnClickGuardar)

        Tabla_Articulos.SetMinSize((950, 184))

        self.Sizers.append(Box_Main)

        return self.Sizers[0]

    def Responsable(self, event):
        if self.Distribucion[0].GetStringSelection() == ResponsableCompraVenta[1]:
            self.Cliente[0].Hide()
            self.Cliente[1].Hide()

            self.Fecha[0].Hide()
            self.Fecha[1].Hide()

            self.Cliente[2].SetLabelText(Comprobante[0])

            self.Cliente[4].SetLabelText(Serie[0])

        if self.Distribucion[0].GetStringSelection() == ResponsableCompraVenta[0]:
            self.Cliente[0].Show()
            self.Cliente[1].Show()

            self.Fecha[0].Show()
            self.Fecha[1].Show()

            self.Cliente[2].SetLabelText(Comprobante[1])

        self.parent.Layout()

    def CompraVenta(self, event):
        if self.Distribucion[1].GetStringSelection() == 'Venta':
            self.Cliente[3].Hide()
            self.Producto[0].HideCol(4)
            self.Cliente[4].SetLabelText(Serie[0])

        if self.Distribucion[1].GetStringSelection() == 'Compra':
            self.Cliente[3].Show()
            self.Producto[0].ShowCol(4)
            self.Cliente[4].SetLabelText(Serie[1])

        self.parent.Layout()

    def OnClickRegresar(self, event):
        self.Sizers[0].ShowItems(False)
        self.parent.GrandParent.TopUsuario.Show()
        self.parent.SetBackgroundColour("#212F3C")
        self.parent.SetSizerAndFit(self.parent.MenuFacturacion())

        self.parent.GrandParent.Layout()

    def OnClickAgregar(self, event):

        self.Producto[0].AppendRows(1)

        _ = self.Producto[0].GetNumberRows()

        self.Producto[0].SetCellValue(_ - 1, 0, "{0}".format(_))
        self.Producto[0].SetFocus()

    def OnClickQuitar(self, event):
        _ = self.Producto[0].GetNumberRows()

        if _ > 0:
            self.Producto[0].DeleteRows(_ - 1)

    def OnClickGuardar(self, event):


