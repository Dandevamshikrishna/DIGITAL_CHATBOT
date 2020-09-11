import wx

class My_Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,
        pos=wx.DefaultPosition,size=wx.Size(600,100),
        style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
        wx.CLOSE_BOX | wx.CLIP_CHILDREN,
        title="ALPHA")
        panel=wx.Panel(self)
        my_sizer=wx.BoxSizer(wx.VERTICAL)
        lbl=wx.StaticText(panel,label="HELLO MY NAME IS 'ALPHA' THE PERSIONAL ASSISTANT OF 'VAMSHIKRISHNA'HOW CAN I HELP YOU?")
        my_sizer.Add(lbl,0,wx.ALL,5)
        self.txt=wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER,size=(500,60))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEnter)
        my_sizer.Add(self.txt,0,wx.ALL,5)
        panel.SetSizer(my_sizer)
        self.Show()
    def OnEnter(self,event):
        input=self.txt.GetValue()
        input=input.lower()
        print("hello i am alive")

if __name__=="__main__":
    app=wx.App(True)
    frame=My_Frame()
    app.MainLoop()
