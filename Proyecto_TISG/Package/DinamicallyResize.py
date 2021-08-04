import os
import wx


class PhotoCtrl(object):
    def __init__(self, parent, path, bpm):
        self.Path = path
        self.Parent = parent
        self.BPM = bpm
        self.image_loaded = False
        self.current_size = self.Parent.GetSize()
        self.filepath = None

        self.Parent.Bind(wx.EVT_SIZE, self.onResize)

        self.PhotoMaxSize = self.current_size.GetHeight() - 10

        self.createWidgets()

    def createWidgets(self):
        self.onView()

        self.Parent.Layout()

    def scale_image(self):
        if self.filepath:
            img = wx.Image(self.filepath, wx.BITMAP_TYPE_ANY)
            # scale the image, preserving the aspect ratio
            W = img.GetWidth()
            H = img.GetHeight()
            if W > H:
                NewW = self.PhotoMaxSize
                NewH = self.PhotoMaxSize * H / W
            else:
                NewH = self.PhotoMaxSize
                NewW = self.PhotoMaxSize * W / H

            try:
                img = img.Scale(NewW,NewH)
            except wx._core.wxAssertionError:
                pass
            return img

    def onView(self):
        self.filepath = self.Path
        img = self.scale_image()
        self.BPM.SetBitmap(wx.BitmapFromImage(img))
        self.Parent.Refresh()
        self.image_loaded = True

    def onResize(self, event):
        if self.image_loaded:
            if self.current_size != self.Parent.GetSize():
                self.current_size = self.Parent.GetSize()

                self.PhotoMaxSize = self.current_size.GetHeight() - 30
                img = self.scale_image()
                self.BPM.SetBitmap(wx.BitmapFromImage(img))
                self.Parent.Refresh()
                self.Parent.Layout()

