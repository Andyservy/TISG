#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# System Packages

# Project Packages
from Proyecto_TISG.Package import Btnbicolor, show_messange
from Proyecto_TISG import connection

# Third party packages
import wx

# CONSULTA

"""
Advertencias: 
- Un caso en el que definitivamente tienes que hacer event.Skip()es en el controlador al vincularte a 
  wx.EVT_CLOSE. Si no lo hace, el cierre no sucederá correctamente
- Revisar para la propagación de eventos: https://wiki.wxpython.org/EventPropagation
- Herencia multiple: https://realpython.com/python-super/#an-overview-of-pythons-super-function
"""


class Verificacion(wx.Dialog):
    """
    DEFINICIÓN DE INSTANCIA
    - Es recomendable y, si el caso lo requiere, obligatorio ubicar como 'self' al la clase en donde se lo llama

    CONTROL DE LOS MÉTODOS
    - Para hacer la llamada, se debe usar ShowModal (Esto limita al usuario a no saltarse la verificación)
    - Si el padre es un wx.Panel, debe especificar manualmente que el Dialogo se centre con 'Centre()'
    - Las definiciones de los controles OK y Cancel deben llamarse por OnClickOk y OnclickCancel, y deben estar ubicadas dentro del padre
    - El código a proteger debería estar dentro de la definición de OnClickOK
    - Al condicionar OnClickCancel, si se cierra el padre también, debe especificar un control de error

    """

    def __init__(self, parent, place=None):
        super(Verificacion, self).__init__(parent, size=(500, 300), style=wx.BORDER_NONE)

        # PROPIEDADES

        self.inheritance()

        self.Centre()
        self.Colour = "#212F3C"
        self.SetBackgroundColour(self.Colour)

        if place is None:
            place = self.Parent

        self.Place = place

        Panel(self)

        # ATRIBUTOS_TimeRunUpDate

    @classmethod
    def inheritance(cls):
        cls.User = "Andy"


class Panel(wx.Panel, Verificacion):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        super(Panel, self).inheritance()

        self.initGUI()

        # PROPIEDADES

        self.cursor = connection().cursor()

        """
        RECORDATORIO:
        def surface_area(self):
            face_area = super(Square, self).area()
            return face_area * 6

        def volume(self):
            face_area = super(Square, self).area()
            return face_area * self.length
            
        En este ejemplo específico, el comportamiento no cambia. Pero imagina que Square también implementó una 
        .area()función que querías asegurarte de Cube que no se usara. Llamar super()de esta manera le permite hacer 
        eso. 
        """

    def initGUI(self):
        # Contenedores
        Box_Main = wx.BoxSizer(wx.VERTICAL)
        Box_Entrada = wx.BoxSizer(wx.VERTICAL)
        Box_Cancel_OK = wx.BoxSizer(wx.HORIZONTAL)

        # CONTROLES

        ENTRADA_Name = wx.TextCtrl(self, -1,
                                   style=wx.BORDER_NONE | wx.ALIGN_CENTER & ~ wx.TE_PASSWORD)
        ENTRADA_Name.SetHint('Ingrese su nombre')
        Box_Entrada.Add(ENTRADA_Name, 1, wx.EXPAND | wx.ALL, 10)
        self.Entrada_Name = ENTRADA_Name

        ENTRADA_Contraseña = wx.TextCtrl(self, -1,
                                         style=wx.BORDER_NONE | wx.ALIGN_CENTER | wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        ENTRADA_Contraseña.SetHint('Ingrese su contraseña')
        Box_Entrada.Add(ENTRADA_Contraseña, 1, wx.EXPAND | wx.ALL, 10)
        self.ENTRADA_Contraseña = ENTRADA_Contraseña

        """Esto es parcialmente incorrecto, pero gracias a ello puedo usar estos dos atributos dentro de las 
        funciones, o sea, asignar a un atributo una variable, lo cual hace que paresca que si esta dentro del 
        __init__ """

        BTN_OK = wx.Button(self, -1, 'OK')

        BTN_Cancel = wx.Button(self, -1, "CANCEL")
        self.BTN_Cancel = BTN_Cancel

        Box_Cancel_OK.Add(BTN_OK, 1, wx.EXPAND | wx.ALL, 15)

        Box_Cancel_OK.Add(BTN_Cancel, 1, wx.EXPAND | wx.ALL, 15)

        # AÑADIENDO LOS BOXERS HIJOS AL PADRE

        Box_Main.Add(Box_Entrada, 3, wx.EXPAND)
        Box_Main.Add(Box_Cancel_OK, 2, wx.EXPAND)

        # CONFIGURANDO SIZER

        self.SetSizer(Box_Main)

        # MODIFICANDO FUENTES

        Font_Entrada = wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL)
        ENTRADA_Name.SetFont(Font_Entrada)
        ENTRADA_Contraseña.SetFont(Font_Entrada)

        # MODIFICANDO COLOR

        ENTRADA_Name.SetBackgroundColour('#283747')

        ENTRADA_Contraseña.SetBackgroundColour('#283747')

        # ESTILO A LOS BOTONES

        Botones_OK_CANCEL = [BTN_OK, BTN_Cancel]
        Btnbicolor(Botones_OK_CANCEL, '#2C4158', '#384A5F')

        # EVENTOS

        BTN_OK.Bind(wx.EVT_BUTTON, self.OnClickOK)
        BTN_Cancel.Bind(wx.EVT_BUTTON, self.GrandParent.OnClickCancel)
        BTN_Cancel.Bind(wx.EVT_BUTTON, self.OnClickCancel)

    def OnClickOK(self, event):

        Nombre_Entrada = self.Entrada_Name.GetValue()
        Contraseña_Entrada = self.ENTRADA_Contraseña.GetValue()
        """Como se puede evidenciar, estoy usando los atributos de Entrada_Name pertenecientes al panel; sin embargo 
        esto no sería posible si haber instanciado como atributo el Entrada_Name """

        # Llamamos al objeto que llama a Verificación

        consult_mysql = "SELECT Contraseña FROM login_history WHERE Nombre_User = '{0}'".format(Nombre_Entrada)
        consult_Datos = "SELECT * FROM login_history"

        if Nombre_Entrada and Contraseña_Entrada:

            self.cursor.execute(consult_mysql)
            Contraseña = self.cursor.fetchall()  # Colectamos en un tuple el valor seleccionado

            if Contraseña:
                if (Contraseña[0][0]) == Contraseña_Entrada:
                    self.Entrada_Name.Clear()
                    self.ENTRADA_Contraseña.Clear()

                    self.Parent.Close()

                    self.cursor.execute(consult_Datos)
                    Login = self.cursor.fetchall()
                    # self.User = Login[0][0]
                    self.Parent.Place.OnClickOK()  # Dentro del super padre, hay un método, esta función ejecuta
                    # lo que se debe hacer después

                    """
                    Para destruir la ventana directamente, se necesita especificar el parámetro en Panel,
                    para que, al ser dhbusado en Ventana, se introduzca un self, así:

                    import wx

                    class MainScene(wx.Frame):
                      def __init__(self, parent, title):
                        super(MainScene, self).__init__(parent, title=title, size=(300, 300))
                        self.InitUI()

                      def InitUI(self):
                        # Define Master Panel
                        masterPanel = wx.Panel(self)
                        masterPanel.SetBackgroundColour("gold")
                        horzbox = wx.BoxSizer(wx.HORIZONTAL)
                        subPanel=SubPanel(parent=masterPanel, size=(200, 200), mainWin=self)

                    class SubPanel(wx.Panel):
                      def __init__(self, parent, size, mainWin):
                        wx.Panel.__init__(self, parent, size=size)
                        self.mainWin = mainWin
                        self.SetBackgroundColour("gray")
                        vbox = wx.BoxSizer(wx.VERTICAL)
                        exit_button = wx.Button(self, label="Exit")
                        exit_button.Bind(wx.EVT_BUTTON, self.onClose)
                        vbox.Add(exit_button, proportion=1, flag=wx.ALL | wx.CENTER, border=5)
                        self.SetSizer(vbox)

                      def onClose(self, event):
                        print('Called from SubPanel')
                        self.mainWin.Destroy()
                    """  # Si alguna vez se necesita especificar que es lo que se debe cerrar

                else:
                    show_messange(Panel, "Contraseña no válida")

            else:
                show_messange(Panel, "Usuario no existente")

        else:
            show_messange(Panel, "Nombre de usuario o la contraseña no deberían estar vacíos")

    def OnClickCancel(self, event):
        self.Parent.Close()
        event.Skip()
