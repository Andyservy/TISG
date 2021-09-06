import wx
import wx.adv
import wx.grid as grid
import wx.lib.intctrl as intctrl

from Proyecto_TISG.Variables import *
from Proyecto_TISG.data.SERVIRDOR.DATABASE import connection
from Proyecto_TISG.Package import JustInt, show_messange, ShapedButton, AutoComplete, CantidadAdicional


class ComercialBillings(object):

    def Box(self, parent, boton):
        parent.cursor = connection().cursor()
        Box_Comprobante = wx.BoxSizer(wx.VERTICAL)
        self.parent = parent

        self.Sizers = []
        self.ClienteInfo = []
        self.Producto = []
        self.Fecha = []
        self.Distribucion = []

        Box_Main = wx.GridBagSizer(24, 13)
        # Top---------------------------------------------------------------------------------------------------------------

        parent.cursor.execute("""SELECT * FROM clientes""")
        self.Cliente = parent.cursor.fetchall()

        self.NombreClientes = [x[1] for x in self.Cliente if not None in x]

        label_ResumenEmpresa = wx.StaticText(parent, -1, str(Consult_DataEmpresa[4]))
        Box_Main.Add(label_ResumenEmpresa, pos=(0, 0), span=(0, 10),
                     flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        fontlabel_ResumenEmpresa = wx.Font(16, wx.ROMAN, wx.NORMAL, wx.NORMAL)

        label_Ubicacion = wx.StaticText(parent, -1, "{0} Telefono: {1}".format(str(Consult_DataEmpresa[2]), Consult_DataEmpresa[7]))
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

        label_Num = wx.StaticText(parent, -1, '{0}'.format(Conteo_FacturaOrdinaria[0] + 1))
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
        ctrl_Nombre.Bind(wx.EVT_TEXT, self.OnFillNombre)

        Tabla_Articulos.SetMinSize((950, 184))

        self.Sizers.append(Box_Main)

        return self.Sizers[0]

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

    def CompraVenta(self, event):
        if self.Distribucion[1].GetStringSelection() == 'Venta':
            self.ClienteInfo[3].Hide()
            self.Producto[0].HideCol(5)
            self.ClienteInfo[4].SetLabelText(Serie[0])

        if self.Distribucion[1].GetStringSelection() == 'Compra':
            self.ClienteInfo[3].Show()
            self.Producto[0].ShowCol(5)
            self.ClienteInfo[4].SetLabelText(Serie[1])

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

        Filas = []
        total = 0
        llenas = 0
        vacias = 0
        Confirm = False
        RUCEmpresa = ("{0}{1}".format(self.ClienteInfo[4].GetLabel(), self.ClienteInfo[5].GetLabel()))

        ClienteIngreso = [self.ClienteInfo[6].GetValue(), self.ClienteInfo[7].GetValue(),
                          self.ClienteInfo[8].GetValue(), self.Distribucion[0].GetStringSelection(),
                          self.ClienteInfo[1].GetValue()]

        while total <= self.Producto[0].GetNumberRows() - 1:
            Filas.append([])

            for _ in range(8):
                Filas[llenas].append(self.Producto[0].GetCellValue(total, _))

            if not list(filter(None, Filas[llenas][1:5] + Filas[llenas][6:8])):
                Filas.pop(llenas)

                total = total + 1
                vacias = vacias + 1

            else:
                llenas = llenas + 1
                total = total + 1

        if vacias < total:

            if (self.ClienteInfo[6:8] + self.ClienteInfo[1:2]) != '':

                if not ClienteIngreso[0] in self.NombreClientes:
                    self.parent.cursor.execute("""INSERT INTO Clientes (
                             NombreCliente, DNI, Domicilio, Responsable, RUC)
                             VALUES
                             ('{0}', '{1}', '{2}', '{3}', '{4}')""".format(self.ClienteInfo[6].GetValue(),
                                                                           self.ClienteInfo[7].GetValue(),
                                                                           self.ClienteInfo[8].GetValue(),
                                                                           self.Distribucion[0].GetStringSelection(),
                                                                           self.ClienteInfo[1].GetValue()))
                    connection().commit()

                else:
                    self.parent.cursor.execute("""UPDATE clientes SET
                             NombreCliente = '{0}',
                             DNI = '{1}',
                             Domicilio = '{2}',
                             Responsable = '{3}',
                             RUC = '{4}')
                             WHERE NombreCliente = '{0}'
                             """.format(self.ClienteInfo[6], self.ClienteInfo[7], self.ClienteInfo[8],
                                        self.Distribucion[0].GetStringSelection(), self.ClienteInfo[1]))
                    connection().commit()

                self.parent.cursor.execute("""SELECT idClientes INTO @idCliente FROM clientes WHERE NombreCliente='{0}';
                    SELECT COUNT(*) INTO @idFactura FROM factura;
                    INSERT INTO factura (idFactura, RUC, Fecha_Limite, Pago, Concepto, Fecha_Factura, Clientes_idClientes) 
                    VALUES (@idFactura+1, '{1}', '{2}', '{3}', '{4}', '{5}', @idCliente);""".
                                           format(RUCEmpresa, self.Fecha[0].GetValue(),
                                                  self.ClienteInfo[9].GetStringSelection(),
                                                  self.Distribucion[1].GetStringSelection(),
                                                  self.Fecha[1].GetValue(), ClienteIngreso[0]), multi=True)
                connection().commit()

                if self.Distribucion[1].GetStringSelection() == 'Venta':

                    for productos in Filas:
                        self.parent.cursor.execute("""SELECT Nombre_Producto FROM productos_compra 
                        WHERE Nombre_Producto = '{0}'""".format(productos[1]))

                        Nombre_Producto = self.parent.cursor.fechone()

                        if Nombre_Producto != '':

                            self.parent.cursor.execute("""SELECT Cantidad FROM productos_compra 
                            WHERE Nombre_Producto = '{0}'""".format(productos[1]))

                            Producto_Disposicion = self.parent.cursor.fechone()

                            if Producto_Disposicion - int(productos[2]) > 0:

                                self.parent.cursor.execute("""SELECT idFactura INTO @idFactura FROM factura 
                                WHERE RUC = '{0}';
                                SELECT idProductos_Compra INTO @idProductos FROM productos_compra 
                                WHERE Nombre_Producto='{1}';
                                INSERT INTO factura_ordinaria 
                                (Cantidad, Factura_idFactura, Compra_idProductos_Compra, Descripcion) 
                                VALUES ('{2}', @idFactura, @idProductos, '{3}')""".format(RUCEmpresa, Nombre_Producto,
                                                                                          Producto_Disposicion,
                                                                                          Filas[3]))

                                connection().commit()

                            else:
                                show_messange(self.parent,
                                              "El producto '{0}' esta agotado o el pedido excede su cantidad actual de: "
                                              "'{1}'".format(productos[1], Producto_Disposicion))

                                Respuesta = wx.MessageDialog(self.parent, '¿Desea actualizar la disposicion del producto?',
                                                 'Dispocision',
                                                 wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION).ShowModal()

                                if Respuesta == wx.ID_YES:

                                    Respuesta.Destroy()
                                    Actualizar = CantidadAdicional(self.parent).ShowModal()
                                    CantidadAgregar = Actualizar.Result

                                    self.parent.cursor.execute("""INSERT INTO productos_compra (productos_compra.Cantidad) 
                                    VALUE ('{0}')""".format(CantidadAgregar))

                                elif Respuesta == wx.ID_NO:
                                    Respuesta.Destroy()

                        else:
                            show_messange(self.parent,
                                          "EL producto '{0}' no existe en nuestro inventario".format(productos[1]))



                else:
                    if len([x[5] for x in Filas if x[5]]) > 0:

                        for producto in Filas:
                            self.parent.cursor.execute("""SELECT Nombre_Producto FROM productos_compra 
                            WHERE Nombre_Producto = '{0}'""".format(producto[1]))

                            Nombre_Producto = self.parent.cursor.fechone()

                            if Nombre_Producto == '':
                                self.parent.cursor.execute("""SELECT idFactura INTO @idFactura FROM factura 
                                WHERE RUC='{0}';
                                INSERT INTO productos_compra (idProductos_Compra, Nombre_Producto, Precio_Compra, 
                                Precio_Venta, Fecha, Factura_idFactura, Cantidad, Descripcion) 
                                VALUES ('{1}', '{2}', '{3}', '{4}', {5}, @idFactura, {6}, {7}})""".
                                                       format(RUCEmpresa, Filas_Productos + 1, producto[1],
                                                              producto[4], producto[5], self.Fecha[0].GetValue(),
                                                              producto[2], producto[3]))
                                connection().commit()

                                self.parent.cursor.execute("""SELECT idProductos_Compra INTO @lastid 
                                FROM productos_compra ORDER BY idProductos_Compra DESC LIMIT 1;
                                SELECT Factura_idFactura INTO @idFactura FROM productos_compra 
                                WHERE idProductos_Compra = @lastid;
                                INSERT INTO factura_ordinaria (IDFACTURA_ORDINARIA,
                                CANTIDAD, FACTURA_IDFACTURA, COMPRA_IDPRODUCTOS_COMPRA, DESCRIPCION) 
                                VALUES ('{0}', '{1}', @idFactura, @lastid, '{2}')""".
                                                           format(Conteo_FacturaOrdinaria+1, producto[2], producto[3]))
                            else:
                                self.parent.cursor.execute("""SELECT idFactura INTO @idFactura 
                                FROM factura WHERE RUC='{0}';
                                SELECT Cantidad INTO @Cantidad FROM productos_compra;
                                UPDATE productos_compra SET 
                                idProductos_Compra='{1}', 
                                Nombre_Producto='{2}', 
                                Precio_Compra='{3}', 
                                Precio_Venta='{4}', 
                                Fecha=, {5}, 
                                Factura_idFactura=@idFactura, 
                                Cantidad=, {6}+@Cantidad, 
                                Descripcion=, {7};""".format(RUCEmpresa, Filas_Productos + 1, producto[1],
                                                             producto[4], producto[5], self.Fecha[0].GetValue(),
                                                             int(producto[2]), producto[3]))

                                connection().commit()

                                self.parent.cursor.execute("""SELECT idProductos_Compra INTO @lastid 
                                FROM productos_compra ORDER BY idProductos_Compra DESC LIMIT 1;
                                SELECT Factura_idFactura INTO @idFactura FROM productos_compra 
                                WHERE idProductos_Compra = @lastid;
                                INSERT INTO factura_ordinaria (IDFACTURA_ORDINARIA,
                                CANTIDAD, FACTURA_IDFACTURA, COMPRA_IDPRODUCTOS_COMPRA, DESCRIPCION) 
                                VALUES ('{0}', '{1}', @idFactura, @lastid, '{2}')""".
                                                           format(Conteo_FacturaOrdinaria+1, producto[2], producto[3]))

                    else:
                        show_messange(self.parent,
                                      "Debe Registrar un precio de Venta al producto que se va a adquirir")

                connection().commit()

            else:
                show_messange(self.parent, "Ciertos parametros deben estar llenados")

        else:
            show_messange(self.parent, "Para registrar deben haber pedidos")

        connection().commit()
        # if Filas[llenas][1] != '' and Filas[llenas][3] != '' and Filas[llenas][5:6] != '':
        #
        #     if self.Distribucion[1].GetStringSelection() == 'Compra':
        #
        #         self.parent.cursor.execute("""INSERT INTO productos_compra """)

        # if Filas[llenas][1] != '' and Filas[llenas][3] != '' and Filas[llenas][5:6] != '':
        #
        #     if (self.ClienteInfo[6:8] + self.ClienteInfo[1:2]) != '':
        #

        #
        #     else:
        #         show_messange(self.parent, "Ciertos parametros deben estar llenados")
        #
        # connection().commit()

        # self.parent.cursor.execute("""SELECT COUNT(*) FROM productos_compra""")
        # numFilas = self.parent.cursor.fetchone()
        #
        #         for e in self.ProductoTable:
        #             ProductosTable = [str(r) for r in e]
        #
        #             if Filas[y] == ProductosTable:
        #                 pass
        #
        #             elif int(Filas[y][0]) <= numFilas[0]:
        #                 self.parent.cursor.execute("""UPDATE productos_compra
        #                 SET Nombre_Producto = '{0}',
        #                 Precio_Compra = '{1}',
        #                 Precio_Venta = '{2}',
        #                 Fecha = '{3}',
        #                 Cantidad = '{4}',
        #                 Descripcion = '{5}'
        #                 WHERE idProductos_Compra='{6}'""".format(Filas[y][1], Filas[y][2], Filas[y][3],
        #                                                          Filas[y][4], Filas[y][6], Filas[y][7],
        #                                                          Filas[y][0]))
        #
        #             else:
        #                 self.parent.cursor.execute("""INSERT INTO productos_compra (IDPRODUCTOS_COMPRA, NOMBRE_PRODUCTO,
        #                 PRECIO_COMPRA, PRECIO_VENTA,  FECHA,FACTURA_IDFACTURA, CANTIDAD, DESCRIPCION) VALUES ('{0}', '{1}',
        #                 '{2}', '{3}' , '{4}', '{5}', '{6}', '{7}')""".format(numFilas[0]+1, Filas[y][1], Filas[y][2],
        #                                                                      Filas[y][3], Filas[y][4], 1, Filas[y][6],
        #                                                                      Filas[y][7]))
        #
        #         connection().commit()
        #
        #         x = x + 1
        #         y = y + 1
        #
        #     else:
        #         show_messange(self.parent, "Verifique que los datos esten completos en el item '{0}'".format(x + 1))
        #         break
        #
        # if vacias == self.Producto[0].GetNumberRows():
        #     show_messange(self.parent, "Para poder realizar una alteracion de gran escala necesita permisos")
        #     Verificacion(self.parent, self).ShowModal()

    def OnFillNombre(self, event):

        Object = event.GetEventObject().GetValue()
        if Object in self.NombreClientes:
            IndexNombre = self.NombreClientes.index(self.ClienteInfo[6].GetValue())

            self.ClienteInfo[7].SetValue(int(self.Cliente[IndexNombre][2]))
            self.ClienteInfo[8].SetValue(self.Cliente[IndexNombre][3])
            self.ClienteInfo[1].SetValue(self.Cliente[IndexNombre][5])
