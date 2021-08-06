import wx

from Proyecto_TISG.Variables import *
from Proyecto_TISG.Package import Btnbicolor
from Proyecto_TISG import connection


class DataFacturacion(wx.Dialog):
    """
    Esta clase instaura los datos necesarios para cada facturación
    """

    def __init__(self, parent):
        super(DataFacturacion, self).__init__(parent, size=(500, 650), style=wx.BORDER_NONE)

        self.Centre()
        self.Colour = "#212F3C"
        self.SetBackgroundColour(self.Colour)

        Panel_DataFT(self)


class Panel_DataFT(wx.Panel):

    def __init__(self, parent):
        super(Panel_DataFT, self).__init__(parent)

        self.cursor = connection().cursor()
        self.initGUI()

    def initGUI(self):

        box_Main = wx.BoxSizer(wx.VERTICAL)
        box_Titulo = wx.BoxSizer(wx.VERTICAL)
        box_Data = wx.StaticBoxSizer(wx.HORIZONTAL, self, "Datos de la empresa")
        box_Label = wx.BoxSizer(wx.VERTICAL)
        box_CtrlText = wx.BoxSizer(wx.VERTICAL)
        box_BtnAction = wx.BoxSizer(wx.HORIZONTAL)

        # Titulo
        label_Titulo = wx.StaticText(self, -1, "Refactorizar")
        box_Titulo.Add(label_Titulo, 1, wx.ALIGN_CENTRE | wx.ALL, 20)

        # Data
        box_Data.Add(box_Label, 1, wx.EXPAND)
        box_Data.Add(box_CtrlText, 2, wx.EXPAND)

        label_RazonSocial = wx.StaticText(box_Data.GetStaticBox(), -1, 'Razon Social')
        label_Direccion = wx.StaticText(box_Data.GetStaticBox(), -1, 'Dirección Matriz')
        label_NRUC = wx.StaticText(box_Data.GetStaticBox(), -1, 'N° RUC')
        label_Resumen = wx.StaticText(box_Data.GetStaticBox(), -1, 'Resumen')
        label_IGV = wx.StaticText(box_Data.GetStaticBox(), -1, '% IGV')
        label_TipoEmpresa = wx.StaticText(box_Data.GetStaticBox(), -1, 'Tipo de Empresa')
        label_Telefono = wx.StaticText(box_Data.GetStaticBox(), -1, 'Telefono')

        label = [label_RazonSocial, label_Direccion, label_NRUC, label_Resumen, label_IGV, label_TipoEmpresa,
                 label_Telefono]
        for _ in label:
            box_Label.Add(_, 1, wx.EXPAND | wx.ALL, 10)

        ctrl_RazonSocial = wx.TextCtrl(box_Data.GetStaticBox(), -1)
        ctrl_Direccion = wx.TextCtrl(box_Data.GetStaticBox(), -1)
        ctrl_NRUC = wx.TextCtrl(box_Data.GetStaticBox(), -1)
        ctrl_Resumen = wx.TextCtrl(box_Data.GetStaticBox(), -1)
        ctrl_IGV = wx.TextCtrl(box_Data.GetStaticBox(), -1)
        choc_TipoEmpresa = wx.Choice(box_Data.GetStaticBox(), -1, choices=TiposEmpresa)
        ctrl_Telefono = wx.TextCtrl(box_Data.GetStaticBox(), -1)

        ctrl = [ctrl_RazonSocial, ctrl_Direccion, ctrl_NRUC, ctrl_Resumen, ctrl_IGV, choc_TipoEmpresa, ctrl_Telefono]
        for _ in ctrl:
            box_CtrlText.Add(_, 1, wx.EXPAND | wx.ALL, 10)

        # Actions
        self.BTN_Guardar = wx.Button(self, -1, 'GUARDAR')
        self.BTN_Guardar.Disable()
        box_BtnAction.Add(self.BTN_Guardar, 1, wx.EXPAND | wx.ALL, 20)

        BTN_CERRAR = wx.Button(self, -1, "CERRAR")
        box_BtnAction.Add(BTN_CERRAR, 1, wx.EXPAND | wx.ALL, 20)

        # Estilo
        label_Titulo_Font = wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL)
        label_Titulo.SetFont(label_Titulo_Font)

        for _ in label:
            label_Font = wx.Font(15, wx.ROMAN, wx.NORMAL, wx.NORMAL)
            _.SetFont(label_Font)
            _.SetForegroundColour('#CBC0C0')

        Botones = [self.BTN_Guardar, BTN_CERRAR]
        Btnbicolor(Botones, '#2C4158', '#384A5F')

        # Sizer
        box_Main.Add(box_Titulo, 1, wx.EXPAND)
        box_Main.Add(box_Data, 4, wx.EXPAND | wx.ALL, 10)
        box_Main.Add(box_BtnAction, 1, wx.EXPAND)

        self.SetSizer(box_Main)

        # Eventos

        BTN_CERRAR.Bind(wx.EVT_BUTTON, self.OnClickCancel)
        self.BTN_Guardar.Bind(wx.EVT_BUTTON, self.OnClickGuardar)

        for r in ctrl:

            if str(r.GetId()) == str(choc_TipoEmpresa.GetId()):
                choc_TipoEmpresa.Bind(wx.EVT_CHOICE, self.ChoiceTipoEmpresa)

            else:
                r.Bind(wx.EVT_TEXT, self.OnTextFill)

            if str(r.GetId()) == str(ctrl_NRUC.GetId()) or str(r.GetId()) == str(ctrl_IGV.GetId()):
                r.Bind(wx.EVT_CHAR, self.OnTextChar)

            self.CTRL = ctrl

    # Coleccionar los valores llenos
    def Values_Fill(self):
        ctrlValue = [self.CTRL[0].GetValue(), self.CTRL[1].GetValue(), self.CTRL[2].GetValue(), self.CTRL[3].GetValue(),
                     self.CTRL[4].GetValue(), self.CTRL[5].GetString(self.CTRL[5].GetSelection()),
                     self.CTRL[6].GetValue()]

        self.ctrlValue = ctrlValue

    def OnTextFill(self, event):
        self.Values_Fill()
        Object = event.GetEventObject()

        if len(Object.GetValue()):
            self.BTN_Guardar.Enable()
        else:
            self.BTN_Guardar.Disable()

        for _ in self.ctrlValue:
            if _:
                self.BTN_Guardar.Enable()

    def OnTextChar(self, event):
        key_code = event.GetKeyCode()

        # Allow ASCII numerics
        if ord('0') <= key_code <= ord('9'):
            event.Skip()
            return

        # Allow decimal points
        if key_code == ord('.'):
            event.Skip()
            return

        # Allow tabs, for tab navigation between TextCtrls
        if key_code == ord('\t'):
            event.Skip()
            return

        if key_code in (8, 127, 314, 316):
            event.Skip()
            return

        # Block everything else
        return

    def ChoiceTipoEmpresa(self, event):
        choice = event.GetEventObject()
        Selection = choice.GetString(choice.GetSelection())

        self.BTN_Guardar.Enable()

        if Selection == '':
            self.BTN_Guardar.Disable()

    def OnClickGuardar(self, event):
        x = 0
        self.Values_Fill()

        for _ in self.ctrlValue:
            if _ != '':
                Consulta = """UPDATE DataEmpresa
                                    SET %s = '%s'
                                    WHERE id = 1"""
                self.cursor.execute(Consulta % (list_DatosEmpresa[x], _))
                connection().commit()

            x = x + 1

        self.Parent.Close()

    def OnClickCancel(self, event):
        self.Parent.Close()
