import wx
import wolframalpha
import wikipedia
import pyttsx3 as pk
engine = pk.init()
engine.say("welcome my buddy nice to see you :)")
engine.runAndWait()
class My_Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,
        pos=wx.DefaultPosition,size=wx.Size(600,100),
        style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
        wx.CLOSE_BOX | wx.CLIP_CHILDREN,
        title="MY_vAS")
        panel=wx.Panel(self)
        my_sizer=wx.BoxSizer(wx.VERTICAL)
        lbl=wx.StaticText(panel,label="HELLO MY NAME IS 'VAS' THE PERSIONAL ASSISTANT OF 'DANDE VAMSHIKRISHNA'HOW CAN I HELP YOU?")
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
        try:
            engine = pk.init()
            app_id='GAGHGV-76KGJTLV2L'
            client=wolframalpha.Client(app_id)
            res=client.query(input)
            answer=next(res.results).text
            print(answer)
            engine.say("the answer is "+answer)
            engine.runAndWait()
        except:
            engine =pk.init()
            engine.say("hurry searched for "+input)
            print(wikipedia.summary(input))
            engine.runAndWait()
if __name__=="__main__":
    app=wx.App(True)
    frame=My_Frame()
    app.MainLoop()
