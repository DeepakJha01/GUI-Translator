from tkinter import *
from textblob import TextBlob                   ##language translation API
from tkinter.scrolledtext import ScrolledText   ##for scrollable text box

#-----translation function----------------------------------------------------------------------
def toLang(lang):
    try:
        output.delete("1.0",END)            ##to delete previous entry in the output box
        inputSTR = input_str.get("1.0",END)
        obj = TextBlob(str(inputSTR))
        outputSTR = obj.translate(to=lang)
        output.insert(END,str(outputSTR))   ##insert output to the output box
    except:
        output.insert(END, "**Please enter a meaningful word/sentence**")

        
#-----user interface section---------------------------------------------------------------------
root = Tk()
root.title("Instant Translator")
root.geometry("400x500+400+200")            ##width x height + xpos + ypos
root.configure(bg = "orange")

label1 = Label(root,text = "Translate from English to any language", fg="white",bg="black", font = ("Times New Roman","18"))
label1.place(x=10,y=30)

label2 = Label(root,text = "Type Anything:",fg="blue",font = ("Times New Roman","12"))
label2.place(x=20,y=90)
                                            ##scrollable text box with multiple lines of input
input_str = ScrolledText(root,width=42,height=6,font=("Times New Roman","12"))
input_str.place(x=20,y=120)

label3 = Label(root,text = "Translate to :",fg="black",bg="yellow",font = ("Times New Roman","13"))
label3.place(x=150,y=270)

translate_button = Button(root,text = "HINDI",command = toLang('hi'),fg="white",bg="green")
translate_button.place(x=75,y=300)

translate_button = Button(root,text = "FRENCH",command = toLang(''fr'),fg="white",bg="blue")
translate_button.place(x=130,y=300)

translate_button = Button(root,text = "SPANISH",command = toLang('es'),fg="white",bg="#B80000")
translate_button.place(x=200,y=300)

translate_button = Button(root,text = "RUSSIAN",command = toLang('ru'),fg="white",bg="#330099")
translate_button.place(x=270,y=300)
                                            ##scrollable text box with multiple lines of output
output = ScrolledText(root,width = 42,height=6,font=("Times New Roman","12"))
output.place(x=20,y=350)

credit_label = Label(root,text = "© Deepak Jha")
credit_label.place(x=320,y=480)

root.mainloop()
