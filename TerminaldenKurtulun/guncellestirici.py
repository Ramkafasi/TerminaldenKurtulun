import os
from tkinter import *
def guncelleme():
    yazi2.config(text="Program güncelleniyor, lütfen bekleyiniz.")
    try:
        os.system("sudo apt install git")
        os.system("sudo git clone https://github.com/Ramkafasi/TerminaldenKurtulun.git")
        os.system("sudo rm /usr/local/bin/TerminaldenKurtulun/TerminaldenKurtulun.py")
        os.system("sudo rm /usr/local/bin/TerminaldenKurtulun/surum.txt")
        os.system("sudo cp -r /usr/local/bin/TerminaldenKurtulun/TerminaldenKurtulun/TerminaldenKurtulun/TerminaldenKurtulun.py /usr/local/bin/TerminaldenKurtulun")
        os.system("sudo cp -r /usr/local/bin/TerminaldenKurtulun/TerminaldenKurtulun/TerminaldenKurtulun/surum.txt /usr/local/bin/TerminaldenKurtulun")
        os.system("sudo rm -rf /usr/local/bin/TerminaldenKurtulun/TerminaldenKurtulun/*")
        os.system("sudo rmdir /usr/local/bin/TerminaldenKurtulun/TerminaldenKurtulun")
        yazi2.config("Güncelleme tamamlanmıştır.")
    except:
        yazi2.config(text="Bir şeyler yanlış gitti, lütfen tekrar deneyiniz.")
pencere=Tk()
pencere.title("Terminalden kurtulun güncelleştirici")

fotograf= PhotoImage(file="/usr/local/bin/TerminaldenKurtulun/tk.png")
fotocikti=Label(pencere, image=fotograf)
fotocikti.pack()

yazi=Label(pencere)
yazi.config(text="Programın yapımcısı=Ram_kafasi, Merhabalar, Terminalden kurtulun programını tercih ettiğiniz için teşekkürler, başınıza gelebilecek herhangi bir durumdan sorumluluk almayacağımızı belirtiriz.",font ="arial 10 bold")
yazi.pack()

yazi2=Label(pencere)
yazi2.config(text="Merhabalar, bizi seçtiğiniz için teşekkür ederiz, programı güncellemek için lütfen devam ediniz.")
yazi2.pack()

buton=Button(pencere)
buton.config(text="Devam et",command=guncelleme)
buton.pack()

mainloop()