import wx


class AutoComplete(wx.TextCompleter):
    def __init__(self, AutoList):
        wx.TextCompleter.__init__(self)
        self._iLastReturned = wx.NOT_FOUND
        self._sPrefix = ''
        self.AutoList = AutoList

    def Start(self, prefix):
        self._sPrefix = prefix.lower()
        self._iLastReturned = wx.NOT_FOUND
        for item in self.AutoList:
            if item.lower().startswith(self._sPrefix):
                return True
        # Nothing found
        return False

    def GetNext(self):
        for i in range(self._iLastReturned+1, len(self.AutoList)):
            if self.AutoList[i].lower().startswith(self._sPrefix):
                self._iLastReturned = i
                return self.AutoList[i]
        # No more corresponding item
        return ''