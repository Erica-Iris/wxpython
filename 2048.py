import wx


class MyFrame(wx.Frame):
    PANEL_ORIG_POINT = wx.Point(15, 15)

    def __init__(self, title):
        super(MyFrame, self).__init__(None, title=title, size=(500, 550))
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Centre()
        self.SetFocus()
        self.Show()

    def on_paint(self, e):
        self.draw_tiles()

    def draw_tiles(self):
        dc = wx.ClientDC(self)
        dc.SetBackground(wx.Brush("#FAF8EF"))
        dc.Clear()
        dc.SetBrush(wx.Brush("#C0B0A0"))
        dc.SetPen(wx.Pen("", 1, wx.TRANSPARENT))
        dc.DrawRoundedRectangle(self.PANEL_ORIG_POINT.x, self.PANEL_ORIG_POINT.y, 450, 450, 5)
        for row in range(4):
            for column in range(4):
                dc.SetBrush(wx.Brush("#CCC0B3"))
                dc.DrawRoundedRectangle(self.PANEL_ORIG_POINT.x + 110 * column + 10,
                                        self.PANEL_ORIG_POINT.y + 110 * row + 10, 100, 100, 5)


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame('2048')
        frame.Show(True)
        return True

if __name__ == "__main__":
    app=MyApp()
    app.MainLoop()