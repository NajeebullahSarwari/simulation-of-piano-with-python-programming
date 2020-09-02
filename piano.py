from tkinter import*
import time;
import datetime
import pygame

pygame.init()
root=Tk()
root.title("MUSIC BOX")
root.geometry('1352x700+0+0')
root.configure(background='white')
ABC=Frame(root,bg="powder blue",bd=20,relief=RIDGE)
ABC.grid()
ABC1=Frame(ABC,bg="powder blue",bd=20,relief=RIDGE)
ABC1.grid()
ABC2=Frame(ABC,bg="powder blue",relief=RIDGE)
ABC2.grid()
ABC3=Frame(ABC,bg="powder blue",relief=RIDGE)
ABC3.grid()

str1=StringVar()
str1.set("JUST LIKE MUSIC")
Date1=StringVar()
Time1=StringVar()

Date1.set(time.strftime("%d/%m/%y"))
Time1.set(time.strftime("%H:%M:%S"))
#===========================================================
def Value_Cs():
      str1.set("C#")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\C_s.wav")
      sound.play()
      
def Value_Ds():
      str1.set("D#")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\D_s.wav")
      sound.play()

def Value_Fs():
      str1.set("F#")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\F_s.wav")
      sound.play()

def Value_Gs():
      str1.set("G#")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\G_s.wav")
      sound.play()

def Value_Bb():
      str1.set("Bb")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\Bb.wav")
      sound.play()

def Value_Gs():
      str1.set("G#")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\G_s.wav")
      sound.play()
def Value_Cs1():
      str1.set("C#1")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\C_s1.wav")
      sound.play()

def Value_Ds1():
      str1.set("D#1")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\D_s1.wav")
      sound.play()
#lower music keys
def Value_C():
      str1.set("C")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\C.wav")
      sound.play()
def Value_D():
      str1.set("D")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\D.wav")
      sound.play()
def Value_E():
      str1.set("E")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\E.wav")
      sound.play()
def Value_F():
      str1.set("F")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\F.wav")
      sound.play()
def Value_G():
      str1.set("G")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\G.wav")
      sound.play()
def Value_A():
      str1.set("A")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\A.wav")
      sound.play()
def Value_B():
      str1.set("B")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\B.wav")
      sound.play()
def Value_C1():
      str1.set("C1")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\C1.wav")
      sound.play()
def Value_D1():
      str1.set("D1")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\D1.wav")
      sound.play()
def Value_E1():
      str1.set("E1")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\E1.wav")
      sound.play()
def Value_F1():
      str1.set("F1")
      sound=pygame.mixer.Sound("E:\pyproject\Music_Notes\F1.wav")
      sound.play()





#==================LABEL WITH TITLE==========
Label(ABC1,text="piano musical keys",font=('arial',25,'bold'),padx=8,pady=8,bd=4,bg="powder blue",
      fg="white",justify=CENTER).grid(row=0,column=0,columnspan=11)
#=================================textbox=============
txtDate=Entry(ABC1,textvariable=Date1,font=('arial',18,'bold'),bd=34,bg="powder blue",
      fg="black",width=28,justify=CENTER).grid(row=1,column=0,pady=1)

txtDisplay=Entry(ABC1,textvariable=str1,font=('arial',18,'bold'),bd=34,bg="powder blue",
      fg="black",width=28,justify=CENTER).grid(row=1,column=1,pady=1)

txtTime=Entry(ABC1,textvariable=Time1,font=('arial',18,'bold'),bd=34,bg="powder blue",
      fg="black",width=28,justify=CENTER).grid(row=1,column=2,pady=1)

#===========================================================
btnCs=Button(ABC2,height=6,width=6,bd=4,text="C#",font=('arial',18,'bold'),bg="black",fg="white",command=Value_Cs)
btnCs.grid(row=0,column=0,padx=5,pady=5)

btnDs=Button(ABC2,height=6,width=6,bd=4,text="D#",font=('arial',18,'bold'),bg="black",fg="white",command=Value_Ds)
btnDs.grid(row=0,column=1,padx=5,pady=5)

btnspace2=Button(ABC2,state=DISABLED,width=2,height=6,bg="powder blue",relief=FLAT)
btnspace2.grid(row=0,column=3,padx=0,pady=0)

btnFs=Button(ABC2,height=6,width=6,bd=4,text="F#",font=('arial',18,'bold'),bg="black",fg="white",command=Value_Fs)
btnFs.grid(row=0,column=4,padx=5,pady=5)

btnGs=Button(ABC2,height=6,width=6,bd=4,text="G#",font=('arial',18,'bold'),bg="black",fg="white",command=Value_Gs)
btnGs.grid(row=0,column=6,padx=5,pady=5)

btnBs=Button(ABC2,height=6,width=6,bd=4,text="Bb",font=('arial',18,'bold'),bg="black",fg="white",command=Value_Bb)
btnBs.grid(row=0,column=8,padx=5,pady=5)

btnspace5=Button(ABC2,state=DISABLED,width=2,height=6,bg="powder blue",relief=FLAT)
btnspace5.grid(row=0,column=9,padx=0,pady=0)

btnCs1=Button(ABC2,height=6,width=6,bd=4,text="c#1",font=('arial',18,'bold'),bg="black",fg="white",command=Value_Cs1)
btnCs1.grid(row=0,column=10,padx=5,pady=5)

btnDs1=Button(ABC2,height=6,width=6,bd=4,text="D#1",font=('arial',18,'bold'),bg="black",fg="white",command=Value_Ds1)
btnDs1.grid(row=0,column=12,padx=5,pady=5)
#========================================================================
btnC=Button(ABC3,bd=4,width=6,height=8,text="C",bg="white",fg="black",font=('arial',18,'bold'),command=Value_C)
btnC.grid(row=0,column=0,padx=5,pady=5)
btnD=Button(ABC3,bd=4,width=6,height=8,text="D",bg="white",fg="black",font=('arial',18,'bold'),command=Value_B)
btnD.grid(row=0,column=1,padx=5,pady=5)
btnE=Button(ABC3,bd=4,width=6,height=8,text="E",bg="white",fg="black",font=('arial',18,'bold'),command=Value_E)
btnE.grid(row=0,column=2,padx=5,pady=5)
btnF=Button(ABC3,bd=4,width=6,height=8,text="F",bg="white",fg="black",font=('arial',18,'bold'),command=Value_F)
btnF.grid(row=0,column=3,padx=5,pady=5)

btnG=Button(ABC3,bd=4,width=6,height=8,text="G",bg="white",fg="black",font=('arial',18,'bold'),command=Value_G)
btnG.grid(row=0,column=4,padx=5,pady=5)
btnA=Button(ABC3,bd=4,width=6,height=8,text="A",bg="white",fg="black",font=('arial',18,'bold'),command=Value_A)
btnA.grid(row=0,column=5,padx=5,pady=5)
btnB=Button(ABC3,bd=4,width=6,height=8,text="B",bg="white",fg="black",font=('arial',18,'bold'),command=Value_B)
btnB.grid(row=0,column=6,padx=5,pady=5)
btnC1=Button(ABC3,bd=4,width=6,height=8,text="C1",bg="white",fg="black",font=('arial',18,'bold'),command=Value_C1)
btnC1.grid(row=0,column=7,padx=5,pady=5)

btnD1=Button(ABC3,bd=4,width=6,height=8,text="D1",bg="white",fg="black",font=('arial',18,'bold'),command=Value_D1)
btnD1.grid(row=0,column=8,padx=5,pady=5)
btnE1=Button(ABC3,bd=4,width=6,height=8,text="E1",bg="white",fg="black",font=('arial',18,'bold'),command=Value_E1)
btnE1.grid(row=0,column=9,padx=5,pady=5)
btnF1=Button(ABC3,bd=4,width=6,height=8,text="F1",bg="white",fg="black",font=('arial',18,'bold'),command=Value_F1)
btnF1.grid(row=0,column=10,padx=5,pady=5)












root.mainloop()
