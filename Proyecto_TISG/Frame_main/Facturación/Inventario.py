import wx
import wx.grid as grid
from datetime import datetime

from Proyecto_TISG.Variables import *
from Proyecto_TISG.Package import ShapedButton, Btnbicolor, show_messange
from Proyecto_TISG.Package.Formulary import Verificacion
from Proyecto_TISG.data.SERVIRDOR.DATABASE import connection


class Inventario(object):

    def Box(self, parent):

        self.parent = parent
        self.guardar = None

        parent.cursor = connection().cursor()

        self.Producto = []
        self.Sizer = []
        Box_Main = wx.GridBagSizer(3, 6)

        Tabla_Inventario = grid.Grid(parent, -1)
        Box_Main.Add(Tabla_Inventario, pos=(0, 0), span=(0, 5))
        Tabla_Inventario.CreateGrid(20, 8)
        Tabla_Inventario.SetRowLabelSize(0)

        Tabla_Inventario.SetColLabelValue(0, 'ID')
        Tabla_Inventario.SetColLabelValue(1, 'Nombre')
        Tabla_Inventario.SetColLabelValue(2, 'Compra (s/.)')
        Tabla_Inventario.SetColLabelValue(3, 'Venta (s/.)')
        Tabla_Inventario.SetColLabelValue(4, 'Fecha')
        Tabla_Inventario.SetColLabelValue(5, 'RUC')
        Tabla_Inventario.SetColLabelValue(6, 'Cantidad')
        Tabla_Inventario.SetColLabelValue(7, 'Descripcion')

        Tabla_Inventario.SetColSize(0, 50)
        Tabla_Inventario.SetColSize(1, 100)
        Tabla_Inventario.SetColSize(2, 100)
        Tabla_Inventario.SetColSize(3, 100)
        Tabla_Inventario.SetColSize(4, 100)
        Tabla_Inventario.SetColSize(5, 100)
        Tabla_Inventario.SetColSize(6, 100)
        Tabla_Inventario.SetColSize(7, 300)

        Tabla_Inventario.SetColFormatDate(4, "%Y-%d-%m")

        Tabla_Inventario.SetColFormatNumber(2)
        Tabla_Inventario.SetColFormatNumber(3)
        Tabla_Inventario.SetColFormatNumber(6)

        for _ in range(6):
            Tabla_Inventario.DisableColResize(_)
            Tabla_Inventario.DisableRowResize(_)

        for _ in range(Tabla_Inventario.GetNumberRows()):

            if Tabla_Inventario.GetCellValue(_, 0) == '':
                Tabla_Inventario.SetCellValue(_, 0, "{0}".format(_ + 1))

        attr = grid.GridCellAttr()
        attr.SetReadOnly(True)
        Tabla_Inventario.SetColAttr(0, attr)
        Tabla_Inventario.SetColAttr(5, attr)

        Tabla_Inventario.SetMinSize((950, 420))

        self.Producto.append(Tabla_Inventario)

        btn_Guardar = wx.Button(parent, -1, 'GUARDAR')
        Box_Main.Add(btn_Guardar, pos=(1, 0), span=(0, 2), flag=wx.EXPAND | wx.ALL, border=10)

        btn_Regresar = ShapedButton(parent, wx.Bitmap(Icon_Home[0]), wx.Bitmap(Icon_Home[1]), wx.Bitmap(Icon_Home[0]))
        Box_Main.Add(btn_Regresar, pos=(2, 0), span=(0, 2), flag=wx.EXPAND | wx.ALL, border=10)

        AgregarQuitar = wx.BoxSizer(wx.HORIZONTAL)

        btn_Agregar = ShapedButton(parent, wx.Bitmap(Agregar[0]), wx.Bitmap(Agregar[1]), wx.Bitmap(Agregar[0]))
        AgregarQuitar.Add(btn_Agregar, 1, wx.EXPAND | wx.ALL, border=10)

        btn_Quitar = ShapedButton(parent, wx.Bitmap(Quitar[0]), wx.Bitmap(Quitar[1]), wx.Bitmap(Quitar[0]))
        AgregarQuitar.Add(btn_Quitar, 1, wx.EXPAND | wx.ALL, border=10)

        Box_Main.Add(AgregarQuitar, pos=(1, 4), span=(0, 2), flag=wx.ALIGN_RIGHT)

        # Estilos

        Botones = [btn_Guardar]
        Btnbicolor(Botones, '#2C4158', '#384A5F')

        # Eventos

        btn_Regresar.Bind(wx.EVT_BUTTON, self.OnClickRegresar)
        btn_Agregar.Bind(wx.EVT_BUTTON, self.OnClickAgregar)
        btn_Quitar.Bind(wx.EVT_BUTTON, self.OnClickQuitar)
        btn_Guardar.Bind(wx.EVT_BUTTON, self.OnClickGuardar)

        self.Sizer.append(Box_Main)

        self.Actualizar()

        return self.Sizer[0]

    def Actualizar(self):

        self.parent.cursor.execute("""SELECT 
        productos_compra.IDPRODUCTOS_COMPRA, 
        productos_compra.NOMBRE_PRODUCTO,
        productos_compra.PRECIO_COMPRA,
        productos_compra.PRECIO_VENTA,
        productos_compra.FECHA,
        factura.RUC,
        productos_compra.CANTIDAD,       
        productos_compra.DESCRIPCION
        FROM productos_compra, factura """)
        productos = self.parent.cursor.fetchall()

        for x in range(self.Producto[0].GetNumberRows()):
            term = False

            for _ in range(8):
                try:
                    self.Producto[0].SetCellValue(x, _, "{0}".format(productos[x][_]))

                except IndexError:
                    term = True
                    break

            if term:
                break

    def OnClickRegresar(self, event):
        self.Sizer[0].ShowItems(False)
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
        x = 0
        y = 0
        vacias = 0

        while x <= self.Producto[0].GetNumberRows()-1:
            Filas.append([])

            for _ in range(8):
                Filas[y].append(self.Producto[0].GetCellValue(x, _))

            if not Filas[y][1] and not Filas[y][2] and not Filas[y][3] and not Filas[y][4] and not Filas[y][5] and not Filas[y][6] and not Filas[y][7]:
                Filas.pop(y)
                x = x + 1
                vacias = vacias + 1

            else:
                if Filas[y][1] != '' and Filas[y][2] != '' and Filas[y][3] != '' and Filas[y][4] != '' and Filas[y][6] \
                        != '' and Filas[y][7] != '':

                    self.parent.cursor.execute("""SELECT COUNT(*) FROM productos_compra""")
                    numFilas = self.parent.cursor.fetchone()

                    self.parent.cursor.execute("""SELECT idProductos_Compra FROM productos_compra 
                    WHERE idProductos_Compra = '{0}'""".format(Filas[y][0]))
                    exist = self.parent.cursor.fetchone()

                    if exist:
                        pass

                    else:
                        self.parent.cursor.execute("""INSERT INTO productos_compra (IDPRODUCTOS_COMPRA, NOMBRE_PRODUCTO, 
                        PRECIO_COMPRA, PRECIO_VENTA,  FECHA,FACTURA_IDFACTURA, CANTIDAD, DESCRIPCION) VALUES ('{0}', '{1}', 
                        '{2}', '{3}' , '{4}', '{5}', '{6}', '{7}')""".format(numFilas[0]+1, Filas[y][1], Filas[y][2],
                                                                             Filas[y][3], Filas[y][4], 1, Filas[y][6],
                                                                             Filas[y][7]))

                    connection().commit()

                    x = x + 1
                    y = y + 1

                else:
                    show_messange(self.parent, "Verifique que los datos esten completos en el item '{0}'".format(x + 1))

            if vacias == self.Producto[0].GetNumberRows():
                show_messange(self.parent, "Para poder realizar una alteracion de gran escala necesita permisos")
                Verificacion(self.parent, self).ShowModal()

    def OnClickOK(self):
        for x in range(self.Producto[0].GetNumberRows()-1):
            self.parent.cursor.execute("DELETE FROM productos_compra")

            connection().commit()


