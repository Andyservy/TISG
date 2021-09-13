import wx
import wx.adv
import wx.grid as grid
import wx.lib.intctrl as intctrl

from Proyecto_TISG.Variables import *
from Proyecto_TISG import connection
from Proyecto_TISG.Package import JustInt, show_messange, ShapedButton, AutoComplete, CantidadAdicional


class ComercialBillings(object):

    def Box(self, parent, home=True, editable=True):

        parent.cursor = connection().cursor()
        Box_Comprobante = wx.BoxSizer(wx.VERTICAL)
        self.parent = parent

        self.Sizers = []
        self.ClienteInfo = []
        self.Producto = []
        self.Fecha = []
        self.Distribucion = []
        self.Resultados = []

        Box_Main = wx.GridBagSizer(24, 13)
        # Top---------------------------------------------------------------------------------------------------------------

        parent.cursor.execute("""SELECT * FROM clientes""")
        self.Cliente = parent.cursor.fetchall()

        self.parent.cursor.execute("""SELECT Nombre_Producto FROM productos_compra""")
        Nombres_Producto = sorted([x[0] for x in self.parent.cursor.fetchall()])

        self.NombreClientes = [x[1] for x in self.Cliente if not None in x[0:3] + x[4:5]]

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

        ctrl_Nombre = wx.TextCtrl(parent, -1, name='Nombre')
        Box_Main.Add(ctrl_Nombre, pos=(3, 1), span=(0, 3), flag=wx.RIGHT | wx.EXPAND)
        ctrl_Nombre.AutoComplete(AutoComplete(self.NombreClientes))

        label_DNI = wx.StaticText(parent, -1, 'DNI:')
        Box_Main.Add(label_DNI, pos=(4, 0), flag=wx.LEFT | wx.LEFT, border=5)

        ctrl_DNI = intctrl.IntCtrl(parent, -1, name='DNI', max=89999999, limited=True)
        JustInt(ctrl_DNI)
        Box_Main.Add(ctrl_DNI, pos=(4, 1), span=(0, 3), flag=wx.RIGHT | wx.EXPAND)

        label_ClienteRUC = wx.StaticText(parent, -1, 'RUC:')
        Box_Main.Add(label_ClienteRUC, pos=(5, 0), flag=wx.ALIGN_LEFT | wx.LEFT, border=5)
        label_ClienteRUC.Show()

        ctrl_ClienteRUC = wx.TextCtrl(parent, -1, name='RUC')
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

        label_Comprobante = wx.StaticText(parent, -1, Comprobante[1], style=wx.ALIGN_CENTER)
        label_Comprobante.SetBackgroundColour(parent.Color)
        fontlabel_Comprobante = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)

        Box_Comprobante.Add(label_Comprobante, 1, wx.EXPAND)

        # Apuntamos la serie con una consulta

        Box_Numeracion = wx.BoxSizer(wx.HORIZONTAL)

        label_Serie = wx.StaticText(parent, -1, 'F-', style=wx.ALIGN_RIGHT)
        label_Serie.SetBackgroundColour('#323754')
        Box_Numeracion.Add(label_Serie, 1, wx.EXPAND)

        label_Num = wx.StaticText(parent, -1, '{0}'.format(Conteo_FacturaVenta + 1))
        label_Num.SetBackgroundColour('#323754')
        Box_Numeracion.Add(label_Num, 1, wx.EXPAND)

        Box_Comprobante.Add(Box_Numeracion, 1, wx.EXPAND)

        Box_Main.Add(Box_Comprobante, pos=(4, 11), span=(2, 4), flag=wx.EXPAND)

        self.ClienteInfo.append(label_ClienteRUC)  # 0
        self.ClienteInfo.append(ctrl_ClienteRUC)  # 1
        self.ClienteInfo.append(label_Comprobante)  # 2
        self.ClienteInfo.append('Añadir_Inventario')  # 3
        self.ClienteInfo.append(label_Serie)  # 4
        self.ClienteInfo.append(label_Num)  # 5
        self.ClienteInfo.append(ctrl_Nombre)  # 6
        self.ClienteInfo.append(ctrl_DNI)  # 7
        self.ClienteInfo.append(ctrl_Domicilio)  # 8
        self.ClienteInfo.append(choc_Pago)  # 9

        # Numeracion regla aquí: https://www.sunat.gob.pe/legislacion/superin/2017/anexosI-II-III-IV-318-2017.pdf
        # Numeracion: https://okasesores.es/facturas-emitidas-orden-numeracion-fecha-correlativas/

        # Productos---------------------------------------------------------------------------------------------------------

        Tabla_Articulos = grid.Grid(parent, -1)
        Box_Main.Add(Tabla_Articulos, pos=(6, 0), span=(0, 12))
        Tabla_Articulos.CreateGrid(8, 8)
        Tabla_Articulos.SetRowLabelSize(0)

        Tabla_Articulos.SetColLabelValue(0, "Codigo")
        Tabla_Articulos.SetColLabelValue(1, "Producto")
        Tabla_Articulos.SetColLabelValue(2, "Cant.")
        Tabla_Articulos.SetColLabelValue(3, "Descripcion")
        Tabla_Articulos.SetColLabelValue(4, "Precio (s/.)")
        Tabla_Articulos.SetColLabelValue(5, "Precio de Venta (s/.)")
        Tabla_Articulos.SetColLabelValue(6, "IVA")
        Tabla_Articulos.SetColLabelValue(7, "SubTotal (s/.)")

        Tabla_Articulos.SetColSize(0, 50)
        Tabla_Articulos.SetColSize(1, 100)
        Tabla_Articulos.SetColSize(2, 100)
        Tabla_Articulos.SetColSize(3, 350)
        Tabla_Articulos.SetColSize(4, 100)
        Tabla_Articulos.SetColSize(5, 150)
        Tabla_Articulos.SetColSize(6, 100)
        Tabla_Articulos.SetColSize(7, 150)

        Tabla_Articulos.HideCol(5)

        self.attr = grid.GridCellAttr()
        self.attr.SetReadOnly(True)
        Tabla_Articulos.SetColAttr(0, self.attr)
        Tabla_Articulos.SetColAttr(4, self.attr)
        Tabla_Articulos.SetColAttr(5, self.attr)
        Tabla_Articulos.SetColAttr(6, self.attr)
        Tabla_Articulos.SetColAttr(7, self.attr)

        ChoiceProducto = grid.GridCellChoiceEditor(Nombres_Producto, True)

        for x in range(Tabla_Articulos.GetNumberRows() - 1):
            Tabla_Articulos.SetCellEditor(x, 1, ChoiceProducto)

        Tabla_Articulos.DisableDragColSize()
        Tabla_Articulos.DisableDragRowSize()
        Tabla_Articulos.SetColFormatNumber(2)

        _ = Tabla_Articulos.GetNumberRows()
        while _ > 0:
            _ = _ - 1
            Tabla_Articulos.SetCellValue(_, 0, "{0}".format(_ + 1))
            Tabla_Articulos.SetCellValue(_, 6, "{0}%".format(str(IGV)))

        self.Producto.append(Tabla_Articulos)
        Tabla_Articulos.ForceRefresh()

        btn_Guardar = wx.Button(parent, -1, 'Guardar')
        Box_Main.Add(btn_Guardar, pos=(7, 1), span=(2, 3), flag=wx.EXPAND)

        btn_Agregar = wx.Button(parent, -1, 'Agregar')
        Box_Main.Add(btn_Agregar, pos=(7, 4), span=(0, 2), flag=wx.EXPAND)

        btn_Quitar = wx.Button(parent, -1, 'Quitar')
        Box_Main.Add(btn_Quitar, pos=(8, 4), span=(0, 2), flag=wx.EXPAND)

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

        if home is True:
            btn_Regresar = ShapedButton(parent, wx.Bitmap(Icon_Home[0]), wx.Bitmap(Icon_Home[1]),
                                        wx.Bitmap(Icon_Home[0]))
            Box_Main.Add(btn_Regresar, pos=(7, 0), span=(3, 0))
            btn_Regresar.Bind(wx.EVT_BUTTON, self.OnClickRegresar)

        label_ResumenEmpresa.SetFont(fontlabel_ResumenEmpresa)
        label_RazonSocial.SetFont(fontlabel_RazonSocial)
        label_TipoEmpresa.SetFont(fontlabel_Empresa)
        label_Comprobante.SetFont(fontlabel_Comprobante)

        # EVENTOS

        RadioBox_Responsable.Bind(wx.EVT_RADIOBOX, self.Responsable)
        RadioBox_Concepto.Bind(wx.EVT_RADIOBOX, self.CompraVenta)
        btn_Agregar.Bind(wx.EVT_BUTTON, self.OnClickAgregar)
        btn_Quitar.Bind(wx.EVT_BUTTON, self.OnClickQuitar)
        btn_Guardar.Bind(wx.EVT_BUTTON, self.OnClickGuardar)
        ctrl_Nombre.Bind(wx.EVT_TEXT, self.OnFillNombre)
        Tabla_Articulos.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.OnEditCell)

        Tabla_Articulos.SetMinSize((950, 184))

        self.Sizers.append(Box_Main)

        return self.Sizers[0]

    def Responsable(self, event):
        if self.Distribucion[0].GetStringSelection() == ResponsableCompraVenta[1]:
            self.ClienteInfo[0].Hide()
            self.ClienteInfo[1].Hide()
            self.ClienteInfo[1].Clear()

            self.Fecha[0].Hide()
            self.Fecha[1].Hide()

            self.ClienteInfo[2].SetLabelText(Comprobante[0])

            self.ClienteInfo[4].SetLabelText(Serie[0])

        if self.Distribucion[0].GetStringSelection() == ResponsableCompraVenta[0]:
            self.ClienteInfo[0].Show()
            self.ClienteInfo[1].Show()
            self.ClienteInfo[1].Clear()

            self.Fecha[0].Show()
            self.Fecha[1].Show()

            self.ClienteInfo[2].SetLabelText(Comprobante[1])

        self.parent.Layout()

    def CompraVenta(self, event):
        if self.Distribucion[1].GetStringSelection() == 'Venta':
            self.Producto[0].HideCol(5)
            self.ClienteInfo[4].SetLabelText(Serie[0])
            self.ClienteInfo[5].SetLabelText(str(Conteo_FacturaVenta+1))

            self.attr.SetReadOnly(True)

        if self.Distribucion[1].GetStringSelection() == 'Compra':
            self.Producto[0].ShowCol(5)
            self.ClienteInfo[4].SetLabelText(Serie[1])
            self.ClienteInfo[5].SetLabelText(str(Conteo_FacturaCompra + 1))

            self.attr.SetReadOnly(False)

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
        self.Producto[0].SetCellValue(_ - 1, 6, "{0}%".format(str(IGV[0])))
        self.Producto[0].SetFocus()

    def OnClickQuitar(self, event):
        _ = self.Producto[0].GetNumberRows()

        if _ > 0:
            self.Producto[0].DeleteRows(_ - 1)

    def OnClickGuardar(self, event):

        Filas = []
        total = 0
        llenas = 0
        vacias = 0
        Confirm = False
        RUCEmpresa = ("{0}{1}".format(self.ClienteInfo[4].GetLabel(), self.ClienteInfo[5].GetLabel()))

        ClienteIngreso = [self.ClienteInfo[6].GetValue(), str(self.ClienteInfo[7].GetValue()),
                          self.ClienteInfo[8].GetValue(), self.Distribucion[0].GetStringSelection(),
                          self.ClienteInfo[1].GetValue()]

        while total <= self.Producto[0].GetNumberRows() - 1:
            Filas.append([])

            for _ in range(8):
                Filas[llenas].append(self.Producto[0].GetCellValue(total, _))

            if len([x for x in Filas[llenas][1:3] + Filas[4:5] + Filas[llenas][7:8] if x == '']) > 0:
                Filas.pop(llenas)

                total = total + 1
                vacias = vacias + 1

            else:
                llenas = llenas + 1
                total = total + 1

        if vacias < total and vacias != 0:

            if ClienteIngreso[3] == 'Individuo':
                Responsable = [ClienteIngreso[0]]

            if ClienteIngreso[3] == 'Empresa':
                if ClienteIngreso[4] == '0':
                    ClienteIngreso[4] = ''

                Responsable = [ClienteIngreso[0], ClienteIngreso[4]]

            if len([x for x in Responsable if x == '']) == 0:

                if not ClienteIngreso[0] in self.NombreClientes:

                    self.parent.cursor.execute(
                        """SELECT idClientes FROM clientes WHERE NombreCliente='{0}'""".format(Responsable[0]))
                    idClienteInsert = self.parent.cursor.fetchall()

                    self.parent.cursor.execute("""INSERT INTO Clientes (idClientes,
                             NombreCliente, DNI, Domicilio, Responsable, RUC)
                             VALUES
                             ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')""".format(idClienteInsert[0][0] + 1,
                                                                                  ClienteIngreso[0],
                                                                                  ClienteIngreso[1],
                                                                                  ClienteIngreso[2],
                                                                                  ClienteIngreso[3],
                                                                                  ClienteIngreso[4]))
                    connection().commit()

                else:
                    self.parent.cursor.execute(
                        """SELECT idClientes FROM clientes WHERE NombreCliente='{0}'""".format(Responsable[0]))
                    idClienteUpdate = self.parent.cursor.fetchall()
                    self.parent.cursor.execute("""UPDATE clientes SET
                             DNI = '{0}',
                             Domicilio = '{1}',
                             Responsable = '{2}',
                             RUC = '{3}' WHERE 
                             idClientes = '{4}';""".format(ClienteIngreso[1], ClienteIngreso[2], ClienteIngreso[3],
                                                           ClienteIngreso[4], idClienteUpdate[0][0]))
                    connection().commit()

                self.parent.cursor.execute(
                    """SELECT idClientes FROM clientes WHERE NombreCliente='{0}'""".format(Responsable[0]))
                idCliente = self.parent.cursor.fetchall()

                self.parent.cursor.execute("""SELECT COUNT(*) FROM factura""")
                numFacturas = self.parent.cursor.fetchall()

                self.parent.cursor.execute("""
                    INSERT INTO factura (idFactura, RUC, Fecha_Limite, Pago, Concepto, Fecha_Factura, 
                    Clientes_idClientes, Total) 
                    VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}');""".
                                           format(int(numFacturas[0][0]) + 1, RUCEmpresa,
                                                  self.Fecha[1].GetValue().Format("%Y-%m-%d"),
                                                  self.ClienteInfo[9].GetStringSelection(),
                                                  self.Distribucion[1].GetStringSelection(),
                                                  self.Fecha[1].GetValue().Format("%Y-%m-%d"), int(idCliente[0][0]),
                                                  float(self.Resultados[1].GetValue())))
                connection().commit()

                if self.Distribucion[1].GetStringSelection() == 'Venta':

                    for productos in Filas:
                        self.parent.cursor.execute("""SELECT Nombre_Producto FROM productos_compra 
                        WHERE Nombre_Producto = '{0}'""".format(productos[1]))

                        Nombre_Producto = self.parent.cursor.fetchone()

                        if Nombre_Producto != '':

                            self.parent.cursor.execute("""SELECT Cantidad FROM productos_compra 
                            WHERE Nombre_Producto = '{0}'""".format(productos[1]))

                            Producto_Disposicion = self.parent.cursor.fetchone()

                            if Producto_Disposicion[0] - int(productos[2]) > 0:

                                self.parent.cursor.execute("""SELECT idFactura FROM factura 
                                WHERE RUC = '{0}'""".format(RUCEmpresa))
                                idFactura = self.parent.cursor.fetchone()

                                self.parent.cursor.execute("""SELECT idProductos_Compra FROM productos_compra 
                                WHERE Nombre_Producto='{0}'""".format(Nombre_Producto[0]))
                                idProductos = self.parent.cursor.fetchone()

                                self.parent.cursor.execute("""SELECT COUNT(*) FROM factura_ordinaria""")
                                idFacturaOrdinaria = self.parent.cursor.fetchone()

                                self.parent.cursor.execute("""INSERT INTO factura_ordinaria 
                                (idFactura_Ordinaria, Cantidad, Factura_idFactura, Compra_idProductos_Compra, 
                                Descripcion) 
                                VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".
                                                           format(idFacturaOrdinaria[0] + 1, Producto_Disposicion[0],
                                                                  idFactura[0], idProductos[0], productos[3]))

                                connection().commit()

                                Confirm = True


                            else:
                                show_messange(self.parent,
                                              "El producto '{0}' esta agotado o el pedido excede su cantidad actual de: "
                                              "'{1}'".format(productos[1], Producto_Disposicion))

                                Respuesta = wx.MessageDialog(self.parent,
                                                             '¿Desea actualizar la disposicion del producto?',
                                                             'Dispocision',
                                                             wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION).ShowModal()

                                if Respuesta == wx.ID_YES:

                                    Actualizar = CantidadAdicional(self.parent)
                                    Actualizar.ShowModal()
                                    CantidadAgregar = Actualizar.Result

                                    self.parent.cursor.execute("""UPDATE productos_compra SET Cantidad = '{0}' 
                                    WHERE Nombre_Producto = '{1}'""".format(CantidadAgregar, Nombre_Producto[0]))

                                    self.parent.cursor.execute("""DELETE FROM factura WHERE RUC = '{0}'""".
                                                               format(RUCEmpresa))

                                    connection().commit()

                                elif Respuesta == wx.ID_NO:
                                    pass

                        else:
                            show_messange(self.parent,
                                          "EL producto '{0}' no existe en nuestro inventario".format(productos[1]))

                else:
                    if len([x[5] for x in Filas if x[5]]) > 0:
                        cursor.execute("SELECT COUNT(*) FROM productos_compra")
                        Filas_Productos = cursor.fetchone()

                        for producto in Filas:
                            self.parent.cursor.execute("""SELECT Nombre_Producto FROM productos_compra 
                            WHERE Nombre_Producto = '{0}'""".format(producto[1]))

                            Nombre_Producto = self.parent.cursor.fetchone()

                            if Nombre_Producto is None:
                                Nombre_Producto = ['']

                            if Nombre_Producto[0] == '':

                                self.parent.cursor.execute("""SELECT idFactura FROM factura 
                                WHERE RUC = '{0}'""".format(RUCEmpresa))
                                idFactura = self.parent.cursor.fetchone()

                                self.parent.cursor.execute("""INSERT INTO productos_compra 
                                (idProductos_Compra, Nombre_Producto, Precio_Compra, Precio_Venta, Fecha, 
                                Factura_idFactura, Cantidad, Descripcion) VALUES ('{0}', '{1}', '{2}', '{3}', 
                                '{4}', '{5}', '{6}', '{7}')""".format(int(Filas_Productos[0]) + 1, producto[1],
                                                                      int(producto[4]), int(producto[5]),
                                                                      self.Fecha[1].GetValue().Format("%Y-%m-%d"),
                                                                      idFactura[0], int(producto[2]), producto[3]))

                                connection().commit()

                                self.parent.cursor.execute("""SELECT idProductos_Compra FROM productos_compra 
                                ORDER BY idProductos_Compra DESC LIMIT 1""")
                                lastid = self.parent.cursor.fetchone()

                                self.parent.cursor.execute("""SELECT Factura_idFactura FROM productos_compra 
                                WHERE idProductos_Compra = '{0}'""".format(lastid[0]))
                                idFactura = self.parent.cursor.fetchone()

                                try:
                                    self.parent.cursor.execute("""INSERT INTO factura_ordinaria (IDFACTURA_ORDINARIA,
                                    CANTIDAD, FACTURA_IDFACTURA, COMPRA_IDPRODUCTOS_COMPRA, DESCRIPCION) 
                                    VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".
                                                               format(Conteo_FacturaOrdinaria + 1, producto[2],
                                                                      idFactura[0],
                                                                      lastid[0], producto[3]))


                                except:
                                    pass
                            else:

                                self.parent.cursor.execute("""SELECT idFactura FROM factura 
                                WHERE factura.RUC='{0}'""".format(RUCEmpresa))
                                idFactura = self.parent.cursor.fetchone()

                                self.parent.cursor.execute("""SELECT Cantidad FROM productos_compra 
                                WHERE Nombre_Producto='{0}'""".format(Nombre_Producto[0]))
                                CantidadProducto = self.parent.cursor.fetchone()

                                try:
                                    self.parent.cursor.execute("""
                                    UPDATE productos_compra SET 
                                    idProductos_Compra='{0}', 
                                    Nombre_Producto='{1}', 
                                    Precio_Compra='{2}', 
                                    Precio_Venta='{3}', 
                                    Fecha='{4}', 
                                    Factura_idFactura= '{5}', 
                                    Cantidad= '{6}' + '{7}', 
                                    Descripcion= {8} WHERE Nombre_Producto='{1}'""".format(Filas_Productos[0] + 1, producto[1],
                                                                                           producto[4], producto[5],
                                                                                           self.Fecha[1].GetValue().
                                                                                           Format("%Y-%m-%d"),
                                                                                           idFactura[0],
                                                                                           int(CantidadProducto[0]),
                                                                                           int(producto[2]), producto[3]))

                                except:
                                    pass

                                connection().commit()

                                self.parent.cursor.execute("""SELECT idProductos_Compra FROM productos_compra 
                                ORDER BY idProductos_Compra DESC LIMIT 1""")
                                lastid = self.parent.cursor.fetchone()

                                self.parent.cursor.execute("""SELECT Factura_idFactura FROM productos_compra 
                                WHERE idProductos_Compra = '{0}'""".format(lastid[0]))
                                idFactura = self.parent.cursor.fetchone()

                                self.parent.cursor.execute("""INSERT INTO factura_ordinaria (IDFACTURA_ORDINARIA,
                                CANTIDAD, FACTURA_IDFACTURA, COMPRA_IDPRODUCTOS_COMPRA, DESCRIPCION) 
                                VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".
                                                           format(Conteo_FacturaOrdinaria[0] + 1, producto[2],
                                                                  idFactura[0], lastid[0], producto[3]))

                            Confirm = True

                    else:
                        show_messange(self.parent,
                                      "Debe Registrar un precio de Venta al producto que se va a adquirir")

                connection().commit()

            else:
                show_messange(self.parent, "Ciertos parametros deben estar llenados")

        else:
            show_messange(self.parent, "Para registrar deben haber pedidos")

        connection().commit()

        if Confirm is True:
            self.Sizers[0].ShowItems(False)
            self.parent.GrandParent.TopUsuario.Show()
            self.parent.SetBackgroundColour("#212F3C")
            self.parent.SetSizerAndFit(self.parent.MenuFacturacion())

            self.parent.GrandParent.Layout()

    def OnFillNombre(self, event):

        Object = event.GetEventObject().GetValue()
        if Object in self.NombreClientes:
            IndexNombre = self.NombreClientes.index(self.ClienteInfo[6].GetValue())

            ActualCliente = [str(x) for x in self.Cliente[IndexNombre]]

            for x in ActualCliente:
                if x == 'None':
                    ActualCliente[ActualCliente.index(x)] = '0'

            self.ClienteInfo[7].SetValue(int(ActualCliente[2]))
            self.ClienteInfo[8].SetValue(ActualCliente[3])
            self.ClienteInfo[1].SetValue(ActualCliente[5])

    def OnEditCell(self, event):
        SetPrecio = []
        SubTotalAll = []
        for x in range(self.Producto[0].GetNumberRows() - 1):
            SetPrecio.append(self.Producto[0].GetCellValue(x, 1))

            if self.Distribucion[1].GetStringSelection() == 'Venta':

                if SetPrecio[x] != '':
                    self.parent.cursor.execute("""SELECT Precio_Venta FROM productos_compra 
                    WHERE Nombre_Producto = '{0}'""".format(SetPrecio[x]))
                    Precio = self.parent.cursor.fetchone()

                    if Precio is None:
                        Precio = ('Sin Precio',)

                    self.Producto[0].SetCellValue((x, 4), str(Precio[0]))

                    if self.Producto[0].GetCellValue(x, 2) != '' and Precio[0] is not None and Precio[0] != 'Sin Precio':
                        SubTotal = int(Precio[0]) * int(self.Producto[0].GetCellValue(x, 2)) + (
                                    int(Precio[0]) * IGV / 100)
                        self.Producto[0].SetCellValue((x, 7), str(SubTotal))
                        self.Producto[0].SetCellValue((x, 4), str(Precio[0]))
                        SubTotalAll.append(SubTotal)

            if self.Distribucion[1].GetStringSelection() == 'Compra':

                Precio = self.Producto[0].GetCellValue(x, 4)

                try:
                    int(Precio)

                except ValueError:
                    Precio = 0

                if self.Producto[0].GetCellValue(x, 2) != '':
                    SubTotal = int(Precio) * int(self.Producto[0].GetCellValue(x, 2)) + \
                               (int(Precio) * IGV / 100)
                    self.Producto[0].SetCellValue((x, 7), str(SubTotal))
                    self.Producto[0].SetCellValue((x, 4), str(Precio))
                    SubTotalAll.append(SubTotal)

        self.Resultados[0].SetValue(str(IGV))
        self.Resultados[1].SetValue(str(sum(SubTotalAll)))
