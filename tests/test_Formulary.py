import wx


# Create class
class ChangeFrame(wx.Frame):
    # initialization
    def __init__(self):
        # Inherit the __init__() function of the parent class
        wx.Frame.__init__(self, None, -1, 'Change Picture', size=(400, 360))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        # Create panel
        panel = wx.Panel(self, -1)
        # Using wxpython's GridBagSizer() for page layout
        sizer = wx.BoxSizer(wx.VERTICAL)  # Column interval is 10, row interval is 20
        # Add the Shanghai field, and add the page layout, as the first row, the first column
        text1 = wx.StaticText(panel, label="Shanghai")
        sizer.Add(text1, wx.EXPAND, flag=wx.ALL, border=5)
        # Get the shanghai.png picture, convert it to Bitmap format, and add it to the first row and second column
        image1 = wx.Image('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Factura ordinaria.png',
                          wx.BITMAP_TYPE_PNG).Rescale(320, 120).ConvertToBitmap()
        bmp1 = wx.StaticBitmap(panel, -1, image1)  # Convert to wx.StaticBitmap() form
        sizer.Add(bmp1, wx.EXPAND, flag=wx.ALL, border=5)
        # Add the Beijing field and add the page layout to the second row and first column
        self.text2 = wx.StaticText(panel, label="Beijing")
        sizer.Add(self.text2, wx.EXPAND, flag=wx.ALL, border=5)
        # Get the beijing.png picture, convert it to Bitmap format, add it to the second row, second column
        image2 = wx.Image('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Factura resumen.png', wx.BITMAP_TYPE_PNG).Rescale(320, 120).ConvertToBitmap()
        self.bmp2 = wx.StaticBitmap(panel, -1, image2)  # Convert to wx.StaticBitmap() form
        sizer.Add(self.bmp2, wx.EXPAND, flag=wx.ALL, border=5)
        # Add login button, and add the page layout, as the fourth row, the second column
        btn = wx.Button(panel, -1, "Change Beijing to Guangzhou")
        sizer.Add(btn, wx.EXPAND, flag=wx.ALL, border=5)
        # Binding change_picture event for login button
        self.Bind(wx.EVT_BUTTON, self.change_picture, btn)
        # Adapt Panmel to GridBagSizer() placement
        panel.SetSizerAndFit(sizer)

    # Define text and image conversion functions
    def change_picture(self, event):
        # Replace the text "Beijing" with "Guangzhou"
        self.text2.SetLabel("Guangzhou")
        # Get pictures of Guangzhou and convert them into Bitmap format
        image = wx.Image('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Pagaré.png', wx.BITMAP_TYPE_PNG).Rescale(320, 120).ConvertToBitmap()
        # Update self.bmp2 of GridBagSizer()
        self.bmp2.SetBitmap(wx.BitmapFromImage(image))


# Main function
if __name__ == '__main__':
    app = wx.App()
    frame = ChangeFrame()
    app.MainLoop()

import os
import wx

class PhotoCtrl(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.frame = wx.Frame(None, title='Photo Control', size=(400, 400))
        self.image_loaded = False
        self.current_size = self.frame.GetSize()
        self.filepath = None

        self.panel = wx.Panel(self.frame)
        self.Bind(wx.EVT_SIZE, self.onResize)

        self.PhotoMaxSize = self.current_size.GetHeight() - 10

        self.createWidgets()
        self.frame.Show()

    def createWidgets(self):
        instructions = 'Browse for an image'
        img = wx.EmptyImage(240,240)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                         wx.BitmapFromImage(img))

        instructLbl = wx.StaticText(self.panel, label=instructions)
        self.photoTxt = wx.TextCtrl(self.panel, size=(200,-1))
        browseBtn = wx.Button(self.panel, label='Browse')
        browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY),
                           0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(instructLbl, 0, wx.ALL, 5)
        self.mainSizer.Add(self.imageCtrl, 0, wx.ALL, 5)
        self.sizer.Add(self.photoTxt, 0, wx.ALL, 5)
        self.sizer.Add(browseBtn, 0, wx.ALL, 5)
        self.mainSizer.Add(self.sizer, 0, wx.ALL, 5)

        self.panel.SetSizer(self.mainSizer)

        self.panel.Layout()

    def onBrowse(self, event):
        """
        Browse for file
        """
        wildcard = "JPG files (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.photoTxt.SetValue(dialog.GetPath())
            self.onView()
        dialog.Destroy()

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
            img = img.Scale(NewW,NewH)
            return img


    def onView(self):
        self.filepath = self.photoTxt.GetValue()
        img = self.scale_image()
        self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
        self.panel.Refresh()
        self.image_loaded = True

    def onResize(self, event):
        print('resizing')
        if self.image_loaded:
            if self.current_size != self.frame.GetSize():
                self.current_size = self.frame.GetSize()

                self.PhotoMaxSize = self.current_size.GetHeight() - 30
                img = self.scale_image()
                self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
                self.panel.Refresh()
                self.panel.Layout()


if __name__ == '__main__':
    app = PhotoCtrl()
    app.MainLoop()



