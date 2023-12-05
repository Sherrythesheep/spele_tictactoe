from tkinter import*
from tkinter import messagebox #paziņojumi, ieteikumi
mansLogs=Tk() #loga objekts
mansLogs.title("TicTacToe")

#define mainigos
speletajsx=True
count=0

#divi speletaji viena datora, pirmais ir x(❀) otrais ir o(✿)
def btnClick(button):#padod visu pogu
    global speletajsx,count #kādi mainīgie tiks izmantoti
    if button["text"]==""and speletajsx==True:#spēlē x speletajs
        button["text"]="❀"#maina uz x
        speletajsx=False
        count+=1 #palielina rūtiņu skaitu(cikls)
        checkWinner()
    elif button["text"]=="" and speletajsx==False:
        button["text"]="✿"#maina uz o
        speletajsx=True
        count+=1
        checkWinner()
    else:
        messagebox.showerror("TicTacToe","Šeit kāds jau ir klikšķinājis!")
    return

#funkcija kas nosaka uzvaretaju
def checkWinner():
    global checkWinner
    winner=False #noteijs, ja bus neizskirts
    if (btn1["text"]=="❀"and btn2["text"]=="❀" and btn3["text"]=="❀" or btn4["text"]=="❀"and btn5["text"]=="❀" and btn6["text"]=="❀" or btn7["text"]=="❀"and btn8["text"]=="❀" and btn9["text"]=="❀" or btn1["text"]=="❀"and btn4["text"]=="❀" and btn7["text"]=="❀" or btn2["text"]=="❀"and btn5["text"]=="❀" and btn9["text"]=="❀" or btn1["text"]=="❀"and btn5["text"]=="❀" and btn9["text"]=="❀" or btn7["text"]=="❀"and btn5["text"]=="❀" and btn3["text"]=="❀" or btn3["text"]=="❀"and btn5["text"]=="❀" and btn7["text"]=="❀"):
        winner=True
        disableButtons()
        messagebox.showinfo("TicTacToe","Spēlētājs ❀ ir uzvarētājs!")
    elif (btn1["text"]=="✿"and btn2["text"]=="✿" and btn3["text"]=="✿" or btn4["text"]=="✿"and btn5["text"]=="✿" and btn6["text"]=="✿" or btn7["text"]=="✿"and btn8["text"]=="✿" and btn9["text"]=="✿" or btn1["text"]=="✿"and btn4["text"]=="✿" and btn7["text"]=="✿" or btn2["text"]=="✿"and btn5["text"]=="✿" and btn9["text"]=="✿" or btn1["text"]=="✿"and btn5["text"]=="✿" and btn9["text"]=="✿" or btn7["text"]=="✿"and btn5["text"]=="✿" and btn3["text"]=="✿" or btn3["text"]=="✿"and btn5["text"]=="✿" and btn7["text"]=="✿"):
        winner=True
        disableButtons()
        messagebox.showinfo("TicTacToe", "Spēlētājs ✿ ir uzvarētājs!")
    elif count==9 and winner==False:
        disableButtons()
        messagebox.showinfo("TicTacToe","Spēle beidzās ar neizšķirtu!")
    return

    
btn1=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="pink",command=lambda:btnClick(btn1))
btn2=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="lightpink",command=lambda:btnClick(btn2))
btn3=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="pink",command=lambda:btnClick(btn3))
btn4=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="lightpink",command=lambda:btnClick(btn4))
btn5=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="pink",command=lambda:btnClick(btn5))
btn6=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="lightpink",command=lambda:btnClick(btn6))
btn7=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="pink",command=lambda:btnClick(btn7))
btn8=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="lightpink",command=lambda:btnClick(btn8))
btn9=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="pink",command=lambda:btnClick(btn9))

#GALVENĀ IZVĒLNE
galvenaIzvelne=Menu(mansLogs)
mansLogs.config(menu=galvenaIzvelne)#pievieno galvenajam logam

#MAZĀ IZVĒLNE
opcijas=Menu(galvenaIzvelne,tearoff=False)#pievieno galvenajam logam
galvenaIzvelne.add_cascade(label='Opcijas',menu=opcijas)

btn1.grid(row=0,column=0)#pievieno pogas
btn2.grid(row=1,column=0)
btn3.grid(row=2,column=0)
btn4.grid(row=0,column=1)
btn5.grid(row=1,column=1)
btn6.grid(row=2,column=1)
btn7.grid(row=0,column=2)
btn8.grid(row=1,column=2)
btn9.grid(row=2,column=2)

#POGU STĀVOKLIS
def disableButtons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)
    return 0

def reset():
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)

    btn1['text']=''
    btn2['text']=''
    btn3['text']=''
    btn4['text']=''
    btn5['text']=''
    btn6['text']=''
    btn7['text']=''
    btn8['text']=''
    btn9['text']=''

opcijas.add_command(label='Jauna spēle',command=reset)
opcijas.add_command(label='Iziet',command=mansLogs.quit)

mansLogs.mainloop()