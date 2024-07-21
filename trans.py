import tkinter 
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator
from tkinter import Frame
root=tkinter.Tk()
root.title("TRANSLATOR")
root.geometry("1080x400")
root.resizable(False  , False )
root.configure(bg="white")
def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000 , label_change)
     
def translate_now():
        text_=text1.get(1.0 , "end")
        t1=Translator()
        trans_text=t1.translate(text_ , src=combo1.get() , dest=combo2.get())   
        trans_text=trans_text.text
        
        text2.delete(1.0 , "end")
        text2.insert("end" , trans_text)
arrow_image=tkinter.PhotoImage(file="arrow.png")
image_label=ttk.Label(root,image=arrow_image , width=150)
image_label.place(x=460 , y= 50)
language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()
combo1=ttk.Combobox(root  ,  values=languageV , font="Roboto  14"  , state ="r")
combo1.place(x=110 , y =20)
combo1.set("ENGLISH")

label1=ttk.Label(root , text="ENGLISH" , font="Arial  30 bold "  , width= 18  , relief = "groove")
label1.place(x= 10 , y = 50)


combo2=ttk.Combobox(root  ,  values=languageV , font="Roboto  14"  , state ="r")
combo2.place(x=730 , y =20)
combo2.set("SELECT LANGUAGE")

label2=tkinter.Label(root , text="ENGLISH" , font="seoge  30 bold "   , width= 18 ,  relief = "groove")
label2.place(x= 620 , y = 50)







f=Frame(root , background="black"  , border = 5)
f.place(x=10 , y = 118, width = 440, height = 210)


text1=tkinter.Text(f , font = "arial  14" ,  wrap = "word" , relief = "flat")
text1.place(x = 0, y = 0 , width = 430 , height = 200)

scrollbar1=ttk.Scrollbar(f)
scrollbar1.pack(side = "right" , fill = "y")
scrollbar1.configure(command = text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)
f1=Frame(root , background="black"  , border = 5)
f1.place(x=620 , y = 118, width = 440, height = 210)


text2=tkinter.Text(f1, font = "arial  14" ,  wrap = "word" , relief = "flat")
text2.place(x = 0, y = 0 , width = 430 , height = 200)

scrollbar2=ttk.Scrollbar(f1)
scrollbar2.pack(side = "right" , fill = "y")
scrollbar2.configure(command = text1.yview)
text2.configure(yscrollcommand=scrollbar2.set)

translate_button=ttk.Button(root , text="Translate" ,   command =translate_now, width = 10  ,  cursor  =" hand2")
translate_button.place(x=476 , y =250)
label_change()
root.mainloop()

