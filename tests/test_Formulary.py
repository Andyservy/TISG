import wx
app = wx.App(redirect=False)
top = wx.Frame(None)
top.SetSize((320, 280))
sizer = wx.GridBagSizer()

def on_char(event):
    event.Skip()
    getValue = searchExpectedResults.GetValue() # get the entered string in TextCtrl with GetValue method
    print (getValue)
    search_items = sorted(['test', 'entry']) # Create a list of all searchable items in a list
    textareaExpectedResults.Clear()
    for item in search_items:
        if getValue in item:
            textareaExpectedResults.Append(item) # Clear the ListBox and append the matching strings in search_items to the ListBox


searchExpectedResults = wx.TextCtrl(top, -1, "", size=(175, -1))
sizer.Add(searchExpectedResults, (2, 8), (2, 14), wx.EXPAND)
searchExpectedResults.Bind(wx.EVT_KEY_UP, on_char) # Bind an EVT_CHAR event to your TextCtrl
search_items = sorted(['test', 'entry'])
textareaExpectedResults = wx.ListBox(top, choices=search_items, size=(270, 250))
sizer.Add(textareaExpectedResults, (6, 8), (2, 14), wx.EXPAND)
top.Sizer = sizer
top.Sizer.Fit(top)
top.Show()
app.MainLoop()