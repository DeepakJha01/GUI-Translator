from tkinter import *
from textblob import TextBlob
from tkinter.scrolledtext import ScrolledText
def toHindi():
    try:
        output.delete("1.0",END)
        inputSTR = input_str.get("1.0",END)
        obj = TextBlob(str(inputSTR))
        outputSTR = obj.translate(to='hi')
        output.insert(END,str(outputSTR))
    except:
        pass

root = Tk()
root.title("Instant Translator")
root.geometry("360x400+400+200")
root.configure(bg = "orange")

label1 = Label(root,text = "Translate to Hindi", fg="white",bg="black", font = ("Times New Roman","18"))
label1.place(x=90,y=30)

label2 = Label(root,text = "Type Anything:",fg="blue",font = ("Times New Roman","12"))
label2.place(x=20,y=90)

input_str = ScrolledText(root,width=38,height=5,font=("Times New Roman","12"))
input_str.place(x=20,y=120)

translate_button = Button(root,text = "Translate",command = toHindi,fg="black",bg="red")
translate_button.place(x=150,y=232)

output = ScrolledText(root,width = 38,height=5,font=("Times New Roman","12"))
output.place(x=20,y=270)

root.mainloop()
