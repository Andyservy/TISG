import wx

from Proyecto_TISG.Package import Btnbicolor, show_messange
from Proyecto_TISG.data.SERVIRDOR.DATABASE import connection

import wx.adv


class Restablecimiento_de_datos(wx.Dialog):
    def __init__(self, parent):
        super(Restablecimiento_de_datos, self).__init__(parent)

        self.SetBackgroundColour("#212F3C")
        self.SetSize(700, 500)
        self.Centre()

        Panel_Confi(self)


# Después de cerrarme recién entra al segundo ok que esta dentro del formulario

class Panel_Confi(wx.Panel):

    def __init__(self, parent):
        super(Panel_Confi, self).__init__(parent)

        self.init_GUI()

        # Levantamos la conexión

        self.cursor = connection().cursor()

    def init_GUI(self):

        box_main = wx.BoxSizer(wx.VERTICAL)
        box_Titulo = wx.BoxSizer(wx.VERTICAL)
        box_Usuario = wx.StaticBoxSizer(wx.HORIZONTAL, self, "Usuario")
        box_Contraseña = wx.StaticBoxSizer(wx.VERTICAL, self, "Contraseña")
        box_OkCancel = wx.BoxSizer(wx.HORIZONTAL)

        box_Contraseña_1 = wx.BoxSizer(wx.HORIZONTAL)
        box_Contraseña_2 = wx.BoxSizer(wx.HORIZONTAL)

        # --------------------------------------------------------------------------------------------------------------

        Label_Titulo = wx.StaticText(self, -1, "\nRestablecimiento de datos\n", style=wx.ALIGN_CENTER)
        box_Titulo.Add(Label_Titulo, 1, wx.ALIGN_CENTER | wx.ALL, 20)

        Label_Usuario = wx.StaticText(box_Usuario.GetStaticBox(), -1, "Coloque su nuevo nombre de usuario")
        box_Usuario.Add(Label_Usuario, 1, wx.EXPAND | wx.ALL, 5)

        Entrada_Usuario = wx.TextCtrl(box_Usuario.GetStaticBox(), -1, style=wx.BORDER_NONE)
        box_Usuario.Add(Entrada_Usuario, 1, wx.EXPAND | wx.ALL, 5)

        pic_username = wx.Bitmap('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/GUARDAR_ICON.png', wx.BITMAP_TYPE_PNG)
        Guardar_username = wx.BitmapButton(box_Usuario.GetStaticBox(), -1, pic_username, size=(50, 50))
        box_Usuario.Add(Guardar_username)

        # --------------------------------------------------------------------------------------------------------------
        box_Contraseña.Add(box_Contraseña_1, 1, wx.EXPAND)
        box_Contraseña.Add(box_Contraseña_2, 1, wx.EXPAND)

        Label_Contraseña = wx.StaticText(box_Contraseña.GetStaticBox(), -1, "Coloque su nueva contraseña")
        box_Contraseña_1.Add(Label_Contraseña, 1, wx.EXPAND | wx.ALL, 5)

        Entrada_Contraseña = wx.TextCtrl(box_Contraseña.GetStaticBox(), -1, style=wx.BORDER_NONE | wx.TE_PASSWORD)
        box_Contraseña_1.Add(Entrada_Contraseña, 1, wx.EXPAND | wx.ALL, 5)
        self.tip = wx.adv.RichToolTip('LIMIT', 'La contraseña debe tener mas de 6 dígitos')

        pic_contraseña = wx.Bitmap('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/GUARDAR_ICON.png', wx.BITMAP_TYPE_PNG)
        Guardar_contraseña = wx.BitmapButton(box_Contraseña.GetStaticBox(), -1, pic_contraseña, size=(50, 50))
        box_Contraseña_1.Add(Guardar_contraseña)

        Label_Contraseña_Repit = wx.StaticText(box_Contraseña.GetStaticBox(), -1, "Repita la contraseña",
                                               style=wx.BORDER_NONE)
        box_Contraseña_2.Add(Label_Contraseña_Repit, 1, wx.EXPAND | wx.ALL, 5)

        Entrada_Contraseña_Repit = wx.TextCtrl(box_Contraseña.GetStaticBox(), -1,  # No t atrevas a mover
                                               # esto, aún no se como funciona, pero si lo mueves la
                                               # configuración falla, o sea de lo que esta bien ubicado, se mueve
                                               style=wx.BORDER_NONE | wx.TE_PASSWORD)

        box_Contraseña_2.Add(Entrada_Contraseña_Repit, 1, wx.EXPAND | wx.ALL, 4)
        box_Contraseña_2.Add(50, wx.RIGHT)

        # --------------------------------------------------------------------------------------------------------------

        BTN_ACEPTAR = wx.Button(self, -1, "ACEPTAR")
        BTN_ACEPTAR.Disable()

        BTN_Restablecer = wx.Button(self, -1, "RESTABLECER")

        BTN_Cancelar = wx.Button(self, -1, "CANCELAR")

        box_OkCancel.Add(BTN_ACEPTAR, 1, wx.EXPAND | wx.ALL, 10)
        box_OkCancel.Add(BTN_Restablecer, 1, wx.EXPAND | wx.ALL, 10)
        box_OkCancel.Add(BTN_Cancelar, 1, wx.EXPAND | wx.ALL, 10)

        # AÑADIENDO LOS SIZES HIJOS AL PADRE

        box_main.Add(box_Titulo, 1, wx.EXPAND)
        box_main.Add(box_Usuario, 1, wx.EXPAND | wx.ALL, 10)
        box_main.Add(box_Contraseña, 2, wx.EXPAND | wx.ALL, 10)
        box_main.Add(box_OkCancel, 1, wx.EXPAND)

        # CONFIGURANDO SIZER

        self.SetSizer(box_main)

        # DANDO COLOR Y TAMAÑO

        color = "#636C75"
        Entrada_Usuario.SetBackgroundColour(color)
        Entrada_Contraseña.SetBackgroundColour(color)
        Entrada_Contraseña_Repit.SetBackgroundColour(color)

        Label_Contraseña.SetForegroundColour("#9B9D9F")
        Label_Usuario.SetForegroundColour("#9B9D9F")
        Label_Contraseña_Repit.SetForegroundColour("#9B9D9F")

        botones = [BTN_ACEPTAR, BTN_Cancelar, BTN_Restablecer]
        Btnbicolor(botones, '#2C4158', '#384A5F')

        Label_Titulo_Font = wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL)
        Label_Titulo.SetFont(Label_Titulo_Font)

        # BOTONES

        self.Guardar_username = Guardar_username
        self.Guardar_contraseña = Guardar_contraseña

        self.BTN_ACEPTAR = BTN_ACEPTAR

        # ENTRADAS

        self.Entrada_Usuario = Entrada_Usuario
        self.Entrada_Contraseña = Entrada_Contraseña
        self.Entrada_Contraseña_Repit = Entrada_Contraseña_Repit

        # EVENTOS

        Guardar_username.Bind(wx.EVT_BUTTON, self.OnClickSave_username)
        Guardar_contraseña.Bind(wx.EVT_BUTTON, self.OnClickSave_contraseña)
        BTN_ACEPTAR.Bind(wx.EVT_BUTTON, self.OnClickAceptar)
        BTN_Restablecer.Bind(wx.EVT_BUTTON, self.OnClickRestablecer)
        BTN_Cancelar.Bind(wx.EVT_BUTTON, self.OnClickCancel)

        # Asimilaciones

        Entrada_Contraseña.Bind(wx.EVT_TEXT, self.OnContraseñaFill)
        self.Parent.Bind(wx.EVT_CLOSE, self.OnClose)

    # GENERAL

    def OnClickSave_username(self, event):
        New_username = self.Entrada_Usuario.GetValue()
        Consulta_Mysql = "INSERT INTO login_history (Nombre_User) VALUE ('{0}')".format(New_username)

        if New_username:
            self.cursor.execute(Consulta_Mysql)
            connection().commit()
            btn_SaveUsername = event.GetEventObject()
            btn_SaveUsername.Disable()
            self.BTN_ACEPTAR.Enable()

        else:
            show_messange(self, "No se admite un usuario sin nombre")

    def OnClickSave_contraseña(self, event):

        New_contraseña = self.Entrada_Contraseña.GetValue()
        Verificar_contraseña = self.Entrada_Contraseña_Repit.GetValue()

        Consulta_Mysql = "INSERT INTO login_history (Contraseña) VALUE ('{0}')".format(New_contraseña)

        if New_contraseña:
            if New_contraseña == Verificar_contraseña:
                self.cursor.execute(Consulta_Mysql)
                connection().commit()

                btn_SaveContraseña = event.GetEventObject()
                btn_SaveContraseña.Disable()

                self.BTN_ACEPTAR.Enable()

            else:
                show_messange(self, "las contraseñas no coinciden")

        else:
            show_messange(self, "Tiene que insertar una contraseña")

    def OnClickAceptar(self, event):
        # no todavía se cubre el error que puede ocurrir si es que no se usa los otros botones

        Consulta_MySQL_Filas = "SELECT COUNT(*) FROM login_history"
        Consulta_MySQL_Nombre_user_Estado = "SELECT Nombre_User FROM login_history"
        Consulta_MySQL_Contraseña_Estado = "SELECT Contraseña FROM login_history"

        self.cursor.execute(Consulta_MySQL_Filas)
        Num_Filas = (self.cursor.fetchone()[0])

        if Num_Filas == 2:

            self.cursor.execute(Consulta_MySQL_Nombre_user_Estado)
            Estado_User = self.cursor.fetchall()

            self.cursor.execute(Consulta_MySQL_Contraseña_Estado)
            Estado_Contraseña = self.cursor.fetchall()

            self.cursor.execute("DELETE FROM login_history WHERE Nombre_User = '{0}'".format(Estado_User[1][0]))
            connection().commit()

            if Estado_User[1][0] is None:
                pass

            else:
                print(Estado_User[1][0])
                print(Estado_User[0][0])
                self.cursor.execute("UPDATE login_history SET Nombre_User = '{0}' WHERE "
                                    "Nombre_User = '{1}'".format(Estado_User[1][0], Estado_User[0][0]))
                connection().commit()

            if Estado_Contraseña[1][0] is None:
                pass

            else:
                self.cursor.execute("UPDATE login_history SET Contraseña = '{0}' WHERE Nombre_User = '{1}'".format(
                    Estado_Contraseña[1][0], Estado_Contraseña[0][0]))
                connection().commit()
        else:
            connection().rollback()

        # self.DataBase.close()
        self.Parent.Close()

    def OnClickRestablecer(self, event):

        Consulta_MySQL_Nombre_user_Estado = "SELECT Nombre_User FROM login_history"

        self.cursor.execute(Consulta_MySQL_Nombre_user_Estado)
        User_Falso = self.cursor.fetchall()

        try:

            if User_Falso[1][0]:
                ConsultaMysql_restablecer = "DELETE FROM login_history WHERE Nombre_User = '{0}'".format(
                    User_Falso[1][0])
                self.cursor.execute(ConsultaMysql_restablecer)
                connection().commit()

                # ACTIVAR BOTONES
                self.BTN_ACEPTAR.Disable()
                self.Guardar_username.Enable()
                self.Guardar_contraseña.Enable()

                # VACIAR
                self.Entrada_Contraseña.SetValue('')
                self.Entrada_Contraseña_Repit.SetValue('')
                self.Entrada_Usuario.SetValue('')

        except IndexError:
            show_messange(self, "no se hizo ninguna modificación")
            connection().rollback()

    def OnClickCancel(self, event):

        self.Parent.Close()

        event.Skip()

    # OnClickCancel
    def OnClose(self, event):

        self.cursor.execute('SELECT * FROM login_history')
        Verificación = self.cursor.fetchall()

        try:
            if Verificación[1]:
                if Verificación[1][0] == '':
                    pass

                else:
                    self.cursor.execute(
                        "DELETE FROM login_history WHERE Nombre_User = '{0}'".format(Verificación[1][0]))

                if Verificación[1][1] == '':
                    pass

                else:
                    print(str(Verificación[1][1]))
                    self.cursor.execute(
                        "DELETE FROM login_history WHERE Contraseña = '{0}'".format(Verificación[1][1]))
                    connection().commit()

        except IndexError:

            connection().rollback()

        event.Skip()

    # OnFillContraseña
    def OnContraseñaFill(self, event):

        if len(self.Entrada_Contraseña.GetValue()) < 8:
            self.tip.ShowFor(self.Entrada_Contraseña)
            self.Guardar_contraseña.Disable()
        else:
            self.Guardar_contraseña.Enable()
