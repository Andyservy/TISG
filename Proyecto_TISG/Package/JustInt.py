import  wx


class JustInt(object):
    def __init__(self, TextCtrl):

        TextCtrl.Bind(wx.EVT_CHAR, self.OnTextChar)

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