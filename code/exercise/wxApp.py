#_*_coding:utf-8_*_
import wx


class APP(wx.App):
    def OnInit(self):
        frame =wx.Frame(parent=None, title="我想学python")
        frame.Show()
        return True


if __name__ == "__main__":
    app = APP()
    app.MainLoop()
    app_1 = wx.App()
    frame_1=wx.Frame(None,title="我是下一个窗口啦！")
    frame_1.Show()
    app_1.MainLoop()