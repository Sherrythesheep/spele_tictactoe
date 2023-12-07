from tkinter import*
from tkinter import messagebox #paziņojumi, ieteikumi
mansLogs=Tk() #loga objekts
mansLogs.title("TicTacToe")

btn1=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="pink",command=lambda:btnClick(btn1),bd=10)
btn2=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="lightpink",command=lambda:btnClick(btn2),bd=10)
btn3=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="pink",command=lambda:btnClick(btn3),bd=10)
btn4=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="lightpink",command=lambda:btnClick(btn4),bd=10)
btn5=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="pink",command=lambda:btnClick(btn5),bd=10)
btn6=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="lightpink",command=lambda:btnClick(btn6),bd=10)
btn7=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="pink",command=lambda:btnClick(btn7),bd=10)
btn8=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="lightpink",command=lambda:btnClick(btn8),bd=10)
btn9=Button(mansLogs,text="",width=6, height=3,font=("Helvica", 24), bg="pink",command=lambda:btnClick(btn9),bd=10)


btn1.grid(row=0,column=0)#pievieno pogas
btn2.grid(row=1,column=0)
btn3.grid(row=2,column=0)
btn4.grid(row=0,column=1)
btn5.grid(row=1,column=1)
btn6.grid(row=2,column=1)
btn7.grid(row=0,column=2)
btn8.grid(row=1,column=2)
btn9.grid(row=2,column=2)

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

    global winner, count, speletajsx
    winner=False
    count=0
    speletajsx=True
    return 0


#define mainigos
speletajsx=True
count=0
winner=True

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

def infoLogs():
    jaunsLogs=Toplevel()
    jaunsLogs.title("Noteikumi")
    jaunsLogs.geometry("1250x170")
    virsraksts=Label(jaunsLogs,text="Spēles noteikumi", font=("Verdana",20,"Bold"), padx=0)
    virsraksts.grid(row=0,column=0)

    noteikums1=Label(jaunsLogs,text="1. spēlē piedalās divi spēlētāji - ❀ un ✿, pirmais spēli sāk ❀", font=("Verdana",12))
    noteikums1.grid(row=1,column=0)

    noteikums2=Label(jaunsLogs,text="2. Lai uzvarētu, vienam no spēlētājiem jāaizpilda 3 blakus esošie lauciņi (vertikāli, horizontāli vai pa diagonāli)", font=('Verdana',12))
    noteikums2.grid(row=2,column=0)

    noteikums3=Label(jaunsLogs,text="3. Ja neviens no spēlētājiem neuzvar, spēle beidzas ar neizšķirtu", font=("Verdana",12))
    noteikums3.grid(row=3,column=0)
    return 0

        

#GALVENĀ IZVĒLNE
galvenaIzvelne=Menu(mansLogs)
mansLogs.config(menu=galvenaIzvelne)#pievieno galvenajam logam

#MAZĀ IZVĒLNE
opcijas=Menu(galvenaIzvelne,tearoff=False)#pievieno galvenajam logam
galvenaIzvelne.add_cascade(label='Opcijas',menu=opcijas)
galvenaIzvelne.add_command(label="Noteikumi", command=infoLogs)

opcijas.add_command(label='Jauna spēle',command=reset)
opcijas.add_command(label='Iziet',command=mansLogs.quit)

mansLogs.mainloop()