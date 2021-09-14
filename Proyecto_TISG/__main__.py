import wx

from Proyecto_TISG.Frame_main import FrameMain


def main():
    app = wx.App()

    FrameMain(None, title='Boost Manager')
    try:
        app.MainLoop()

    except:
        pass

"""Punto de entrada"""
