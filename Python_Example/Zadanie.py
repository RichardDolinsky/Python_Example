from tkinter import *

def openNewWindow(image_name):

    Noveokno=Toplevel(window) #musi tu byt
    Noveokno.title("nove okno s fotkou susiastky")
    Noveokno.geometry("400x200+0+0")
    Noveokno.configure(background='gold')


    
    Noveokno.mainloop()

def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        Definicia= my_compdictionary[entered_text]
        output.insert(END, Definicia)
        openNewWindow(entered_text+'.png')

    except:
        Definicia="Napisal si zle slovo! skus znovu!!!"
        output.insert(END, Definicia)

window = Tk()
window.title("Napis co chces vediet")
window.geometry('405x400+0+0')
window.configure(background="grey")
background_image=PhotoImage(file='Componentes.png')
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, )


#Fotka pozadia
photo=PhotoImage(file="Silueta.png")
Label (window, image=photo, bg="black") .grid(row=1, column=0, sticky=S)
#text v okne
Label (window, text="Vloz slovo suciastky ktoreho chces vediet definiciu, bez mekcenov", bg="black", fg="white", font="none 9 bold") .grid(row=7, column=0, sticky=S)
#textvariable
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=8, column=0, sticky=S)
#tlacidlo
Button(window, text="Povrdit", width=7, command=click) .grid(row=9, column=0, sticky=S)
Label(window, text="Definicia", bg="black", fg="white", font="none 10 bold") .grid(row=15, column=0, sticky=W)

output= Text(window, width=50, height=6, wrap= WORD, background="white" ,)
output.grid(row=16, column=0, columnspan=2, sticky=W)
my_compdictionary = {'tranzistor': 'Tranzistor alebo zriedkavo polovodičová trióda je polovodičová súčiastka, používaná ako zosilňovač, spínač, stabilizátor a modulátor elektrického napätia alebo prúdu.',
'bug':'je to chyba', 'dioda':'Dióda je elektronická súčiastka s dvoma elektródami, ktorá (ideálne) vedie elektrický prúd len jedným smerom. Hovoríme, že prúd usmerňuje. V starších textoch sa ako dióda. (v užšom zmysle) niekedy označovala vákuová dióda.',
'kondenzator':'V zásade vždy ide o dve elektródy s vloženým dielektrikom, ale v závislosti od detailov konštrukcie kondenzátora sa za rôznych podmienok prejavujú ich nežiaduce (parazitné) vlastnosti (napr. sériový odpor, zvod, indukčnosť, teplotné závislosti.'
,'trimre': 'su to casovace',
'rezistor':'Rezistor alebo odpor (nesprávne odporník) je lineárny elektronický prvok, ktorého prevažujúca vlastnosť je jeho elektrický odpor. Vyskytuje sa buď ako súčasť integrovaného obvodu,'
,'cievka':'Cievka je pasívny elektrický (elektrotechnický) prvok, ktorý je reálnou reprezentáciou indukčnosti v elektrickom obvode.'
,'RLC':'Paralelný a sériový RLC obvod je základnou časovou každého elektronického oscilátora, ktorý sa využíva v rádiotechnike, televíznej technike, rádiolokácii a pod.'
}
#otvot okno ak napise







#koniec______________

Label (window, text="Pre ukoncenie klikni Exit", bg="black", fg="white", font="none 12 bold") .grid(row=17, column=0, sticky=W)
def close_window():
    window.destroy()
    exit()
Button (window, text="Exit", width=14, command=close_window) .grid(row=18, column=0, sticky=W)
window.mainloop()
