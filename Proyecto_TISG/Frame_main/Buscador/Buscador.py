import wx
import wx.lib.mixins.listctrl as listmix

from Proyecto_TISG import connection
from Proyecto_TISG.Package import ShapedButton
from Proyecto_TISG.Variables import *

cursor = connection().cursor()

cursor.execute("""SELECT * FROM clientes WHERE idClientes > 1""")
Clientes = cursor.fetchall()

dataClientes = {}

index = 0

for x in Clientes:
    dataClientes[index] = (str(x[1]), str(x[2]), str(x[3]), str(x[4]), str(x[5]))
    index = index + 1

dataFactura = {}
facturasVenta = {}
facturasCompra = {}


class Search(object):
    def Box(self, parent):
        self.box_Main = wx.BoxSizer(wx.VERTICAL)
        self.parent = parent

        facturasordinarias = ListOrdinarias(parent, facturasVenta)
        listFactura = ListFacturas(parent, dataFactura, facturasordinarias)
        listClientes = ListCtrlClientes(parent, listFactura)

        self.listClientes = listClientes

        self.box_Main.Add(listClientes, 1, wx.EXPAND | wx.ALL, 5)

        self.box_Main.Add(listFactura, 1, wx.EXPAND | wx.ALL, 5)

        try:
            self.box_Main.Add(facturasordinarias, 1, wx.EXPAND | wx.ALL, 5)
        except:
            pass

        btn_Regresar = ShapedButton(parent, wx.Bitmap(Icon_Home[0]), wx.Bitmap(Icon_Home[1]),
                                    wx.Bitmap(Icon_Home[0]))
        self.box_Main.Add(btn_Regresar, 1, wx.EXPAND | wx.ALL, 5)
        btn_Regresar.Bind(wx.EVT_BUTTON, self.OnClickRegresar)

        return self.box_Main

    def OnClickRegresar(self, event):
        self.box_Main.ShowItems(False)
        self.parent.GrandParent.TopUsuario.Show()
        self.parent.SetBackgroundColour("#212F3C")
        self.parent.SetSizerAndFit(self.parent.MenuFacturacion())

        self.parent.GrandParent.Layout()


class ListCtrlClientes(wx.Panel, listmix.ColumnSorterMixin):

    # ----------------------------------------------------------------------
    def __init__(self, parent, listFactura):
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)

        self.parent = parent
        self.listFactura = listFactura

        self.list_ctrl = wx.ListCtrl(self, size=(-1, 100),
                                      style=wx.LC_REPORT | wx.BORDER_SUNKEN | wx.LC_SORT_ASCENDING)

        self.list_ctrl.InsertColumn(0, 'Cliente')
        self.list_ctrl.InsertColumn(1, 'DNI')
        self.list_ctrl.InsertColumn(2, 'Domicilio')
        self.list_ctrl.InsertColumn(3, 'Responsable')
        self.list_ctrl.InsertColumn(4, 'RUC')

        self.list_ctrl.SetColumnWidth(0, 200)
        self.list_ctrl.SetColumnWidth(1, 200)
        self.list_ctrl.SetColumnWidth(2, 200)
        self.list_ctrl.SetColumnWidth(3, 150)
        self.list_ctrl.SetColumnWidth(4, 150)

        items = dataClientes.items()
        indexCliente = 0
        for key, data in items:
            self.list_ctrl.InsertItem(indexCliente, data[0])
            self.list_ctrl.SetItem(indexCliente, 1, data[1])
            self.list_ctrl.SetItem(indexCliente, 2, data[2])
            self.list_ctrl.SetItem(indexCliente, 3, data[3])
            self.list_ctrl.SetItem(indexCliente, 4, data[4])
            self.list_ctrl.SetItemData(indexCliente, key)
            indexCliente += 1

        # Now that the list exists we can init the other base class,
        # see wx/lib/mixins/listctrl.py
        self.itemDataMap = dataClientes
        listmix.ColumnSorterMixin.__init__(self, 3)
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnclickRow)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = sizer
        sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer)

    # ----------------------------------------------------------------------
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetListCtrl(self):
        return self.list_ctrl

    def OnclickRow(self, event):
        Name = self.list_ctrl.GetItemText(self.list_ctrl.GetFirstSelected(), 0)

        cursor.execute("""SELECT idClientes FROM clientes WHERE NombreCliente = '{0}'""".format(Name))
        idCliente = cursor.fetchone()

        cursor.execute("""SELECT * FROM factura WHERE Clientes_idClientes = '{0}'""".format(idCliente[0]))
        facturasCliente = cursor.fetchall()

        indexFactura = 0
        dataFactura.clear()

        if not facturasCliente:
            facturasCliente.append(["", "", "", "", "", ""])

        for x in facturasCliente:
            dataFactura[indexFactura] = (str(x[1]), str(x[2]), str(x[3]), str(x[4]), str(x[5]), str(x[7]))
            indexFactura = indexFactura + 1

        items = dataFactura.items()
        indexFactura = 0

        self.listFactura.list_ctrl.DeleteAllItems()

        for key, data in items:
            self.listFactura.list_ctrl.InsertItem(indexFactura, data[0])
            self.listFactura.list_ctrl.SetItem(indexFactura, 1, data[1])
            self.listFactura.list_ctrl.SetItem(indexFactura, 2, data[2])
            self.listFactura.list_ctrl.SetItem(indexFactura, 3, data[3])
            self.listFactura.list_ctrl.SetItem(indexFactura, 4, data[5])
            self.listFactura.list_ctrl.SetItemData(indexFactura, key)
            indexFactura += 1


class ListFacturas (wx.Panel, listmix.ColumnSorterMixin):
    def __init__(self, parent, list, facturaOrdinaria):

        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)

        self.ListProductos = list
        self.FacturaOrdinaria = facturaOrdinaria
        self.parent = parent
        self.list_ctrl = wx.ListCtrl(self, size=(-1, 100),
                                     style=wx.LC_REPORT | wx.BORDER_SUNKEN | wx.LC_SORT_ASCENDING)
        self.list_ctrl.InsertColumn(0, 'RUC')
        self.list_ctrl.InsertColumn(1, 'Fecha')
        self.list_ctrl.InsertColumn(2, 'Fecha Limite')
        self.list_ctrl.InsertColumn(3, 'Concepto')
        self.list_ctrl.InsertColumn(4, 'Total')

        items = list.items()
        indexFactura = 0

        self.list_ctrl.SetColumnWidth(0, 200)
        self.list_ctrl.SetColumnWidth(1, 200)
        self.list_ctrl.SetColumnWidth(2, 200)
        self.list_ctrl.SetColumnWidth(3, 150)
        self.list_ctrl.SetColumnWidth(4, 150)

        for key, data in items:
            self.list_ctrl.InsertItem(indexFactura, data[0])
            self.list_ctrl.SetItem(indexFactura, 1, data[1])
            self.list_ctrl.SetItem(indexFactura, 2, data[2])
            self.list_ctrl.SetItem(indexFactura, 3, data[3])
            self.list_ctrl.SetItem(indexFactura, 4, data[4])
            self.list_ctrl.SetItemData(indexFactura, key)
            indexFactura += 1

        self.itemDataMap = list
        listmix.ColumnSorterMixin.__init__(self, 4)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = sizer
        sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnclickRow)

        self.SetSizer(sizer)

    def GetListCtrl(self):
        return self.list_ctrl

    def OnclickRow(self, event):
        global facturas

        facturaVenta = []
        facturaCompra = []

        Serie = self.list_ctrl.GetItemText(self.list_ctrl.GetFirstSelected(), 0)

        cursor.execute("""SELECT idFactura FROM factura WHERE RUC = '{0}'""".format(Serie))
        idFactura = cursor.fetchone()

        if Serie[0] == 'F':
            self.FacturaOrdinaria.list_ctrl.DeleteAllColumns()

            self.FacturaOrdinaria.list_ctrl.InsertColumn(0, 'Producto')
            self.FacturaOrdinaria.list_ctrl.InsertColumn(1, 'Precio')
            self.FacturaOrdinaria.list_ctrl.InsertColumn(2, 'Cantidad')
            self.FacturaOrdinaria.list_ctrl.InsertColumn(3, 'Descripcion')
            self.FacturaOrdinaria.list_ctrl.InsertColumn(4, 'SubTotal')

            self.FacturaOrdinaria.list_ctrl.SetColumnWidth(0, 100)
            self.FacturaOrdinaria.list_ctrl.SetColumnWidth(1, 200)
            self.FacturaOrdinaria.list_ctrl.SetColumnWidth(2, 200)
            self.FacturaOrdinaria.list_ctrl.SetColumnWidth(3, 150)
            self.FacturaOrdinaria.list_ctrl.SetColumnWidth(4, 150)

            cursor.execute("""SELECT * FROM factura_ordinaria WHERE Factura_idFactura = '{0}'""".
                           format(idFactura[0]))
            facturaOrdinariaVenta = cursor.fetchall()

            facturasnum = 0
            for x in facturaOrdinariaVenta:
                facturaVenta.append([])

                cursor.execute("""SELECT Nombre_Producto, Precio_Venta FROM productos_compra 
                WHERE idProductos_Compra = '{0}'""".format(x[3]))
                NombreProducto = cursor.fetchall()

                facturaVenta[facturasnum].append(NombreProducto[0][0])
                facturaVenta[facturasnum].append(NombreProducto[0][1])
                facturaVenta[facturasnum].append(x[1])
                facturaVenta[facturasnum].append(x[4])
                facturaVenta[facturasnum].append(str(int(x[1] * int(NombreProducto[0][1]))))

                facturasnum = facturasnum + 1

            indexFactura = 0

            if not facturaVenta:
                facturaVenta.append(["", "", "", "", ""])

            for x in facturaVenta:
                facturasVenta[indexFactura] = (str(x[0]), str(x[1]), str(x[2]), str(x[3]), str(x[4]))
                indexFactura = indexFactura + 1

            items = facturasVenta.items()
            indexFactura = 0

            self.FacturaOrdinaria.list_ctrl.DeleteAllItems()

            for key, data in items:
                self.FacturaOrdinaria.list_ctrl.InsertItem(indexFactura, data[0])
                self.FacturaOrdinaria.list_ctrl.SetItem(indexFactura, 1, data[1])
                self.FacturaOrdinaria.list_ctrl.SetItem(indexFactura, 2, data[2])
                self.FacturaOrdinaria.list_ctrl.SetItem(indexFactura, 3, data[3])
                self.FacturaOrdinaria.list_ctrl.SetItem(indexFactura, 4, data[4])
                self.FacturaOrdinaria.list_ctrl.SetItemData(indexFactura, key)
                indexFactura += 1

        if Serie[0] == 'B':

            self.FacturaOrdinaria.list_ctrl.DeleteAllColumns()

            self.FacturaOrdinaria.list_ctrl.InsertColumn(0, 'Producto')
            self.FacturaOrdinaria.list_ctrl.InsertColumn(1, 'Precio Compra')
            self.FacturaOrdinaria.list_ctrl.InsertColumn(2, 'Precio Venta')
            self.FacturaOrdinaria.list_ctrl.InsertColumn(3, 'Fecha')
            self.FacturaOrdinaria.list_ctrl.InsertColumn(4, 'Cantidad')
            self.FacturaOrdinaria.list_ctrl.InsertColumn(5, 'Descripcion')

            self.FacturaOrdinaria.list_ctrl.SetColumnWidth(0, 100)
            self.FacturaOrdinaria.list_ctrl.SetColumnWidth(1, 200)
            self.FacturaOrdinaria.list_ctrl.SetColumnWidth(2, 200)
            self.FacturaOrdinaria.list_ctrl.SetColumnWidth(3, 150)
            self.FacturaOrdinaria.list_ctrl.SetColumnWidth(4, 150)
            self.FacturaOrdinaria.list_ctrl.SetColumnWidth(5, 150)

            cursor.execute("""SELECT * FROM productos_compra WHERE Factura_idFactura = '{0}'""".format(idFactura[0]))
            productos = cursor.fetchall()

            facturasnum = 0
            for x in productos:
                facturaCompra.append([])

                facturaCompra[facturasnum].append(x[1])
                facturaCompra[facturasnum].append(x[2])
                facturaCompra[facturasnum].append(x[3])
                facturaCompra[facturasnum].append(x[4])
                facturaCompra[facturasnum].append(x[6])
                facturaCompra[facturasnum].append(x[7])

                facturasnum = facturasnum + 1

            indexFactura = 0

            if not facturaCompra:
                facturaVenta.append(["", "", "", "", ""])

            for x in facturaCompra:
                facturasCompra[indexFactura] = (str(x[0]), str(x[1]), str(x[2]), str(x[3]), str(x[4]))
                indexFactura = indexFactura + 1

            items = facturasCompra.items()
            indexFactura = 0

            self.FacturaOrdinaria.list_ctrl.DeleteAllItems()

            for key, data in items:
                self.FacturaOrdinaria.list_ctrl.InsertItem(indexFactura, data[0])
                self.FacturaOrdinaria.list_ctrl.SetItem(indexFactura, 1, data[1])
                self.FacturaOrdinaria.list_ctrl.SetItem(indexFactura, 2, data[2])
                self.FacturaOrdinaria.list_ctrl.SetItem(indexFactura, 3, data[3])
                self.FacturaOrdinaria.list_ctrl.SetItem(indexFactura, 4, data[4])
                self.FacturaOrdinaria.list_ctrl.SetItemData(indexFactura, key)
                indexFactura += 1




















class ListOrdinarias (wx.Panel, listmix.ColumnSorterMixin):
    def __init__(self, parent, list):
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)

        self.list_ctrl = wx.ListCtrl(self, size=(-1, 100),
                                     style=wx.LC_REPORT | wx.BORDER_SUNKEN | wx.LC_SORT_ASCENDING)
        self.list_ctrl.InsertColumn(0, 'Producto')
        self.list_ctrl.InsertColumn(1, 'Precio')
        self.list_ctrl.InsertColumn(2, 'Cantidad')
        self.list_ctrl.InsertColumn(3, 'Descripcion')
        self.list_ctrl.InsertColumn(4, 'SubTotal')

        items = list.items()
        indexFactura = 0

        self.list_ctrl.SetColumnWidth(0, 100)
        self.list_ctrl.SetColumnWidth(1, 200)
        self.list_ctrl.SetColumnWidth(2, 200)
        self.list_ctrl.SetColumnWidth(3, 150)
        self.list_ctrl.SetColumnWidth(4, 150)

        for key, data in items:
            self.list_ctrl.InsertItem(indexFactura, data[0])
            self.list_ctrl.SetItem(indexFactura, 1, data[1])
            self.list_ctrl.SetItem(indexFactura, 2, data[2])
            self.list_ctrl.SetItem(indexFactura, 3, data[3])
            self.list_ctrl.SetItem(indexFactura, 4, data[4])
            self.list_ctrl.SetItemData(indexFactura, key)
            indexFactura += 1

        self.itemDataMap = list
        listmix.ColumnSorterMixin.__init__(self, 4)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = sizer
        sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer)

    def GetListCtrl(self):
        return self.list_ctrl


class ListOrdinariasCompra (wx.Panel, listmix.ColumnSorterMixin):
    def __init__(self, parent, list):
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)

        self.list_ctrl = wx.ListCtrl(self, size=(-1, 100),
                                     style=wx.LC_REPORT | wx.BORDER_SUNKEN | wx.LC_SORT_ASCENDING)
        self.list_ctrl.InsertColumn(0, 'Producto')
        self.list_ctrl.InsertColumn(1, 'Precio Compra')
        self.list_ctrl.InsertColumn(2, 'Precio Venta')
        self.list_ctrl.InsertColumn(3, 'Fecha')
        self.list_ctrl.InsertColumn(4, 'Cantidad')
        self.list_ctrl.InsertColumn(5, 'Descripcion')

        items = list.items()
        indexFactura = 0

        self.list_ctrl.SetColumnWidth(0, 100)
        self.list_ctrl.SetColumnWidth(1, 200)
        self.list_ctrl.SetColumnWidth(2, 200)
        self.list_ctrl.SetColumnWidth(3, 150)
        self.list_ctrl.SetColumnWidth(4, 150)
        self.list_ctrl.SetColumnWidth(5, 150)

        for key, data in items:
            self.list_ctrl.InsertItem(indexFactura, data[0])
            self.list_ctrl.SetItem(indexFactura, 1, data[1])
            self.list_ctrl.SetItem(indexFactura, 2, data[2])
            self.list_ctrl.SetItem(indexFactura, 3, data[3])
            self.list_ctrl.SetItem(indexFactura, 4, data[4])
            self.list_ctrl.SetItem(indexFactura, 5, data[5])
            self.list_ctrl.SetItemData(indexFactura, key)
            indexFactura += 1

        self.itemDataMap = list
        listmix.ColumnSorterMixin.__init__(self, 5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = sizer
        sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer)

    def GetListCtrl(self):
        return self.list_ctrl








