import wx

from Proyecto_TISG.Frame_main import FrameMain


def main():
    app = wx.App()

    ventana = FrameMain(None, title='Boost Manager', size=(1000, 700))
    try:
        ventana.Show()
    except RuntimeError:
        exit(0)

    app.MainLoop()


"""Punto de entrada"""
