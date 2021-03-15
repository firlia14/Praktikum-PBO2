import wx
import Gui2

class subClass(Gui2.MyFrame5):
    def __init__(self, parent):
        Gui2.MyFrame5.__init__(self, parent)

    def m_button2OnButtonClick ( self, event ):
        Nama=self.Nama.GetValue()
        Nim=self.Nim.GetValue()
        Prodi=self.Prodi.GetValue()
        print('****Hello WX****')
        print("Nama : ", Nama)
        print("Nim : ", Nim)
        print("Prodi : ", Prodi)

app = wx.App()
frame = subClass(parent=None)
frame.Show()
app.MainLoop()