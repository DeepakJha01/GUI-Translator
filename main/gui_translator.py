from tkinter import *
from textblob import TextBlob                   ##language translation API
from tkinter.scrolledtext import ScrolledText   ##for scrollable text box

def toHindi():
    try:
        output.delete("1.0",END)                ##to delete previous entry in the output box
        inputSTR = input_str.get("1.0",END)
        obj = TextBlob(str(inputSTR))
        outputSTR = obj.translate(to='hi')
        output.insert(END,str(outputSTR))       ##insert output to the output box
    except:
        pass

root = Tk()
root.title("Instant Translator")
root.geometry("360x400+400+200")                ##width x height + xpos + ypos
root.configure(bg = "orange")

label1 = Label(root,text = "Translate to Hindi", fg="white",bg="black", font = ("Times New Roman","18"))
label1.place(x=90,y=30)

label2 = Label(root,text = "Type Anything:",fg="blue",font = ("Times New Roman","12"))
label2.place(x=20,y=90)
                                                ##scrollable text box with multiple lines of input
input_str = ScrolledText(root,width=38,height=5,font=("Times New Roman","12"))
input_str.place(x=20,y=120)
                                                ##button binded to toHindi() function
translate_button = Button(root,text = "Translate",command = toHindi,fg="black",bg="red")
translate_button.place(x=150,y=232)
                                                ##scrollable text box with multiple lines of output
output = ScrolledText(root,width = 38,height=5,font=("Times New Roman","12"))
output.place(x=20,y=270)

root.mainloop()
