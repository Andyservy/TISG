import wx
import wx.lib.intctrl as intctrl
import wx.adv
import wx.grid as grid

from Proyecto_TISG.Package import ShapedButton
from Proyecto_TISG.Variables import *


class Recapitulativa(object):
    def Box(self, parent):

        self.parent = parent
        parent.cursor = connection().cursor()

        self.Sizers = []
        self.FechasFacturas = []
        self.IdCliente = []

        box_Main = wx.BoxSizer(wx.HORIZONTAL)
        Seleccion = wx.BoxSizer(wx.VERTICAL)

        box_Main.Add(Seleccion, 1, wx.EXPAND)
        box_Main.Add(self.box_Factura(parent), 6, wx.EXPAND)

        Seleccion.Add(Facturas(self, parent), 5, wx.EXPAND)

        self.list_Fechas = wx.CheckListBox(parent, wx.ID_ANY, choices=self.FechasFacturas, style=1)
        Seleccion.Add(self.list_Fechas, 3, wx.EXPAND)

        Aceptar = wx.Button(parent, -1, 'ACEPTAR')
        Seleccion.Add(Aceptar, 1, wx.EXPAND | wx.ALL, 5)

        Guardar = wx.Button(parent, -1, 'GUARDAR')
        Seleccion.Add(Guardar, 1, wx.EXPAND | wx.ALL, 5)

        btn_Regresar = ShapedButton(parent, wx.Bitmap(Icon_Home[0]), wx.Bitmap(Icon_Home[1]), wx.Bitmap(Icon_Home[0]))
        Seleccion.Add(btn_Regresar, 1, wx.EXPAND | wx.ALL, 20)

        self.Sizers.append(box_Main)

        parent.GrandParent.SetSize(1136, 730)

        btn_Regresar.Bind(wx.EVT_BUTTON, self.OnClickRegresar)
        Aceptar.Bind(wx.EVT_BUTTON, self.OnClickAceptar)
        Guardar.Bind(wx.EVT_BUTTON, self.OnClickGuardar)

        return box_Main

    def box_Factura(self, parent):
        self.ClienteInfo = []
        self.Producto = []
        self.Fecha = []
        self.Distribucion = []
        self.Resultados = []

        Box_Comprobante = wx.BoxSizer(wx.VERTICAL)
        Box_Main = wx.GridBagSizer(24, 13)
        # Top---------------------------------------------------------------------------------------------------------------

        label_ResumenEmpresa = wx.StaticText(parent, -1, str(Consult_DataEmpresa[4]))
        Box_Main.Add(label_ResumenEmpresa, pos=(0, 0), span=(0, 10),
                     flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        fontlabel_ResumenEmpresa = wx.Font(16, wx.ROMAN, wx.NORMAL, wx.NORMAL)

        label_Ubicacion = wx.StaticText(parent, -1,
                                        "{0} Telefono: {1}".format(str(Consult_DataEmpresa[2]), Consult_DataEmpresa[7]))
        Box_Main.Add(label_Ubicacion, pos=(1, 1), span=(0, 9),
                     flag=wx.ALIGN_CENTER | wx.ALIGN_TOP | wx.ALL)

        label_RazonSocial = wx.StaticText(parent, -1, str(Consult_DataEmpresa[1]))
        Box_Main.Add(label_RazonSocial, pos=(0, 10), span=(0, 4),
                     flag=wx.ALIGN_LEFT | wx.ALL, border=5)
        fontlabel_RazonSocial = wx.Font(30, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_ITALIC, wx.NORMAL)

        label_TipoEmpresa = wx.StaticText(parent, -1, str(Consult_DataEmpresa[6]))
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

        ctrl_Nombre = wx.TextCtrl(parent, -1, name='Nombre', style=wx.TE_READONLY)
        Box_Main.Add(ctrl_Nombre, pos=(3, 1), span=(0, 3), flag=wx.RIGHT | wx.EXPAND)

        label_DNI = wx.StaticText(parent, -1, 'DNI:')
        Box_Main.Add(label_DNI, pos=(4, 0), flag=wx.LEFT | wx.LEFT, border=5)

        ctrl_DNI = intctrl.IntCtrl(parent, -1, name='DNI', max=89999999, limited=True, style=wx.TE_READONLY)
        Box_Main.Add(ctrl_DNI, pos=(4, 1), span=(0, 3), flag=wx.RIGHT | wx.EXPAND)

        label_ClienteRUC = wx.StaticText(parent, -1, 'RUC:')
        Box_Main.Add(label_ClienteRUC, pos=(5, 0), flag=wx.ALIGN_LEFT | wx.LEFT, border=5)
        label_ClienteRUC.Show()

        ctrl_ClienteRUC = wx.TextCtrl(parent, -1, name='RUC', style=wx.TE_READONLY)
        Box_Main.Add(ctrl_ClienteRUC, pos=(5, 1), span=(0, 3), flag=wx.EXPAND)
        ctrl_ClienteRUC.Show()

        self.RadioBox_Responsable = wx.RadioBox(parent, label='Responsable', choices=ResponsableCompraVenta,
                                           majorDimension=1, style=wx.RA_SPECIFY_ROWS | wx.TE_READONLY)
        Box_Main.Add(self.RadioBox_Responsable, pos=(5, 4), span=(0, 2), flag=wx.EXPAND | wx.ALL, border=5)
        self.Distribucion.append(self.RadioBox_Responsable)
        self.RadioBox_Responsable.Disable()

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

        ctrl_Domicilio = wx.TextCtrl(parent, -1, style=wx.TE_MULTILINE | wx.TE_READONLY)
        Box_Main.Add(ctrl_Domicilio, pos=(4, 8), span=(2, 3), flag=wx.EXPAND | wx.ALL, border=5)

        label_Comprobante = wx.StaticText(parent, -1, Comprobante[1], style=wx.ALIGN_CENTER)
        label_Comprobante.SetBackgroundColour(parent.Color)
        fontlabel_Comprobante = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)

        Box_Comprobante.Add(label_Comprobante, 1, wx.EXPAND)

        # Apuntamos la serie con una consulta

        Box_Numeracion = wx.BoxSizer(wx.HORIZONTAL)

        label_Serie = wx.StaticText(parent, -1, 'R-', style=wx.ALIGN_RIGHT)
        label_Serie.SetBackgroundColour('#323754')
        Box_Numeracion.Add(label_Serie, 1, wx.EXPAND)

        label_Num = wx.StaticText(parent, -1, '{0}'.format(Conteo_FacturaOrdinaria + 1))
        label_Num.SetBackgroundColour('#323754')
        Box_Numeracion.Add(label_Num, 1, wx.EXPAND)

        Box_Comprobante.Add(Box_Numeracion, 1, wx.EXPAND)

        Box_Main.Add(Box_Comprobante, pos=(4, 11), span=(2, 4), flag=wx.EXPAND)

        self.ClienteInfo.append(label_ClienteRUC)  # 0
        self.ClienteInfo.append(ctrl_ClienteRUC)  # 1
        self.ClienteInfo.append(label_Comprobante)  # 2
        self.ClienteInfo.append(label_Serie)  # 3
        self.ClienteInfo.append(label_Num)  # 4
        self.ClienteInfo.append(ctrl_Nombre)  # 5
        self.ClienteInfo.append(ctrl_DNI)  # 6
        self.ClienteInfo.append(ctrl_Domicilio)  # 7

        # Numeracion regla aquí: https://www.sunat.gob.pe/legislacion/superin/2017/anexosI-II-III-IV-318-2017.pdf
        # Numeracion: https://okasesores.es/facturas-emitidas-orden-numeracion-fecha-correlativas/

        # Productos---------------------------------------------------------------------------------------------------------

        Tabla_Articulos = grid.Grid(parent, -1)
        Box_Main.Add(Tabla_Articulos, pos=(6, 0), span=(0, 12))
        Tabla_Articulos.CreateGrid(8, 6)
        Tabla_Articulos.SetRowLabelSize(0)

        Tabla_Articulos.SetColLabelValue(0, "Codigo")
        Tabla_Articulos.SetColLabelValue(1, "Serie")
        Tabla_Articulos.SetColLabelValue(2, "Fecha")
        Tabla_Articulos.SetColLabelValue(3, "Descripcion.")
        Tabla_Articulos.SetColLabelValue(4, "Concepto")
        Tabla_Articulos.SetColLabelValue(5, "Importe s/.")

        Tabla_Articulos.SetColSize(0, 50)
        Tabla_Articulos.SetColSize(1, 150)
        Tabla_Articulos.SetColSize(2, 100)
        Tabla_Articulos.SetColSize(3, 450)
        Tabla_Articulos.SetColSize(4, 100)
        Tabla_Articulos.SetColSize(5, 100)

        self.attr = grid.GridCellAttr()
        self.attr.SetReadOnly(True)
        Tabla_Articulos.SetColAttr(0, self.attr)
        Tabla_Articulos.SetColAttr(1, self.attr)
        Tabla_Articulos.SetColAttr(3, self.attr)
        Tabla_Articulos.SetColAttr(4, self.attr)

        Tabla_Articulos.DisableDragColSize()
        Tabla_Articulos.DisableDragRowSize()

        _ = Tabla_Articulos.GetNumberRows()
        while _ > 0:
            _ = _ - 1
            Tabla_Articulos.SetCellValue(_, 0, "{0}".format(_ + 1))

        self.Producto.append(Tabla_Articulos)
        Tabla_Articulos.ForceRefresh()

        label_IGV = wx.StaticText(parent, -1, 'IGV')
        label_Total = wx.StaticText(parent, -1, 'Total')
        Box_Main.Add(label_IGV, pos=(8, 10), span=(0, 2))
        Box_Main.Add(label_Total, pos=(9, 10), span=(0, 2))

        ctrl_IGV = wx.TextCtrl(parent, -1, style=wx.TE_READONLY)
        ctrl_Total = wx.TextCtrl(parent, -1, style=wx.TE_READONLY)
        Box_Main.Add(ctrl_IGV, pos=(8, 12), span=(0, 2), flag=wx.EXPAND)
        Box_Main.Add(ctrl_Total, pos=(9, 12), span=(0, 2), flag=wx.EXPAND | wx.ALIGN_TOP)

        self.Resultados.append(ctrl_IGV)
        self.Resultados.append(ctrl_Total)

        label_ResumenEmpresa.SetFont(fontlabel_ResumenEmpresa)
        label_RazonSocial.SetFont(fontlabel_RazonSocial)
        label_TipoEmpresa.SetFont(fontlabel_Empresa)
        label_Comprobante.SetFont(fontlabel_Comprobante)

        # EVENTOS

        Tabla_Articulos.SetMinSize((950, 184))

        return Box_Main

    def Responsable(self, event):
        if self.Distribucion[0].GetStringSelection() == ResponsableCompraVenta[1]:
            self.ClienteInfo[0].Hide()
            self.ClienteInfo[1].Hide()

            self.Fecha[0].Hide()
            self.Fecha[1].Hide()

            self.ClienteInfo[2].SetLabelText(Comprobante[0])

            self.ClienteInfo[4].SetLabelText(Serie[0])

        if self.Distribucion[0].GetStringSelection() == ResponsableCompraVenta[0]:
            self.ClienteInfo[0].Show()
            self.ClienteInfo[1].Show()

            self.Fecha[0].Show()
            self.Fecha[1].Show()

            self.ClienteInfo[2].SetLabelText(Comprobante[1])

        self.parent.Layout()

    def OnClickRegresar(self, event):
        self.Sizers[0].ShowItems(False)
        self.parent.GrandParent.TopUsuario.Show()
        self.parent.SetBackgroundColour("#212F3C")
        self.parent.SetSizerAndFit(self.parent.MenuFacturacion())
        self.parent.GrandParent.SetSize(1000, 730)

        self.parent.GrandParent.Layout()

    def OnClickAceptar(self, event):
        x = 0
        RUCs = self.list_Fechas.GetCheckedStrings()

        self.Producto[0].ClearGrid()

        try:
            self.Producto[0].DeleteRows(numRows=self.Producto[0].GetNumberRows())

        except wx._core.wxAssertionError:
            pass

        self.Producto[0].AppendRows(len(RUCs))

        _ = self.Producto[0].GetNumberRows()
        while _ > 0:
            _ = _ - 1
            self.Producto[0].SetCellValue(_, 0, "{0}".format(_ + 1))

        for RUC in RUCs:
            self.parent.cursor.execute("""SELECT RUC, Fecha_Factura, Fecha_Limite, Concepto, Total FROM factura 
            WHERE RUC = '{0}'""".format(RUC))
            DatosFactura = self.parent.cursor.fetchone()
            DatosFactura = [str(x) for x in DatosFactura]

            self.Producto[0].SetCellValue(x, 1, DatosFactura[0])
            self.Producto[0].SetCellValue(x, 2, DatosFactura[1])
            self.Producto[0].SetCellValue(x, 4, DatosFactura[3])
            self.Producto[0].SetCellValue(x, 5, DatosFactura[4])

            x = x + 1

    def OnClickGuardar(self, event):
        pass


class Facturas(wx.TreeCtrl):

    def __init__(self, cover, parent):
        wx.TreeCtrl.__init__(self, parent)

        self.parent = parent
        parent.cursor = connection().cursor()

        self.cover = cover

        parent.cursor.execute("""SELECT NombreCliente FROM clientes""")
        self.Clientes = sorted([x[0] for x in parent.cursor.fetchall()])

        root = self.AddRoot('Facturas')

        for x in self.Clientes:
            Cliente = self.AppendItem(root, x)

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnClickTree)

        self.ExpandAll()

    def OnClickTree(self, event):
        item = event.GetItem()

        if self.GetItemText(item) in self.Clientes:

            self.parent.cursor.execute("""SELECT idClientes, Responsable, RUC, Domicilio, DNI FROM clientes 
            WHERE NombreCliente = '{0}'""".
                                       format(self.GetItemText(item)))
            Cliente = self.parent.cursor.fetchone()
            Cliente = [str(x) for x in Cliente]

            if Cliente[1] is None:
                pass
            else:
                self.cover.ClienteInfo[5].SetLabelText(self.GetItemText(item))

                try:
                    self.cover.ClienteInfo[6].SetLabelText(Cliente[4])
                except ValueError:
                    pass

                self.cover.ClienteInfo[7].SetLabelText(Cliente[3])

                if Cliente[1] == 'Individuo':
                    self.cover.RadioBox_Responsable.SetSelection(1)

                    if self.cover.Distribucion[0].GetStringSelection() == ResponsableCompraVenta[1]:
                        self.cover.ClienteInfo[0].Hide()
                        self.cover.ClienteInfo[1].Hide()

                        self.cover.Fecha[0].Hide()
                        self.cover.Fecha[1].Hide()

                        self.cover.ClienteInfo[2].SetLabelText(Comprobante[0])

                    self.cover.parent.Layout()

                if Cliente[1] == 'Empresa':
                    self.cover.RadioBox_Responsable.SetSelection(0)

                    if self.cover.Distribucion[0].GetStringSelection() == ResponsableCompraVenta[0]:
                        self.cover.ClienteInfo[0].Show()
                        self.cover.ClienteInfo[1].Show()

                        self.cover.Fecha[0].Show()
                        self.cover.Fecha[1].Show()

                        self.cover.ClienteInfo[2].SetLabelText(Comprobante[1])

                        try:
                            self.cover.ClienteInfo[1].SetLabelText(Cliente[2])
                        except ValueError:
                            pass

                        self.cover.parent.Layout()

            self.parent.cursor.execute("""SELECT RUC FROM factura WHERE Clientes_idClientes = '{0}'""".
                                       format(Cliente[0]))
            RUC = self.parent.cursor.fetchall()

            RUC = [str(x[0]) for x in RUC]

            for x in range(len(RUC)):
                if RUC[x] is None:
                    RUC[x] = 'Sin Fecha'

            self.cover.list_Fechas.SetItems(RUC)

            self.cover.IdCliente.append(Cliente[0])

            if len(self.cover.IdCliente) > 1:
                self.cover.IdCliente.pop(0)
