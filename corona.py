from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import locale, tkinter, win32api, win32con, pywintypes

width=win32api.GetSystemMetrics(0)
width=int(width-0.15*width)

url='https://www.worldometers.info/coronavirus/'

header= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

class UpdateLabel():
    def __init__(self):
        self.win=tkinter.Tk()
        self.var=tkinter.StringVar()
        self.ctr=[]
        self.var.set("Fetching data...")

        # change your color here
        self.label = tkinter.Label(self.win, textvariable=self.var, font=('Consolas','11'), fg='white', bg='black')
        self.label.master.wm_attributes("-transparentcolor", "black")

        self.label.master.overrideredirect(True)        
        self.label.master.lift()
        self.label.master.wm_attributes("-disabled", True)
        res="+"+str(width)+"+"+str(0)
        self.label.master.geometry(res)

        # if you want always on top, uncomment this line
        # self.label.master.wm_attributes("-topmost", True)
        

        hWindow = pywintypes.HANDLE(int(self.label.master.frame(), 16))
        exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

        self.label.pack()
        self.updater()
        self.label.mainloop()
            
    def updater(self):
        try:
            req=Request(url=url, headers=header)
            page_html=urlopen(req).read()
            
        except:
            self.var.set("No Internet")
            self.win.after(1000, self.updater)
            
        soup=BeautifulSoup(page_html, 'html.parser')
        total_number=soup.findAll("div", {"class": "maincounter-number"})
        locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
        self.ctr=[]
        for i in total_number:
            temp=locale.atoi(i.text.strip())
            self.ctr.append(temp)
            
        d0=self.ctr[0]
        d1=self.ctr[1]
        d2=self.ctr[2]
        
        p0=100
        p1=round(self.ctr[1]/self.ctr[0]*100, 2)
        p2=round(self.ctr[2]/self.ctr[0]*100, 2)
        
        final_data="Cases   Death  Recov.\n"+str(d0)+"  "+str(d1)+"  "+str(d2)+"\n"+" "+str(p0)+"%"+"   "+str(p1)+"%"+"   "+str(p2)+"%"
        
        self.var.set(final_data)
        self.win.after(10000, self.updater)
        
UL=UpdateLabel()