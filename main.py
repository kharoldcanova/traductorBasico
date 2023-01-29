import tkinter as tk
import traductor

#inicializate
root = tk.Tk()
root.geometry("400x100")
root.title("Traductor")

#create a label
label = tk.Label(root, text="Ingresa un texto: ")
label.pack()

#variable 
word = tk.StringVar()

#create a entry
entry = tk.Entry(root, textvariable=word)
entry.config(width=50)
entry.pack()

#set a label
texttranslate = tk.StringVar()
texttranslate.set("Aqui se mostrara la traducccion")

#create a new label 
wordtranslate = tk.Label(root, textvariable=texttranslate)
wordtranslate.pack()


# function
def handle_input():
    entered_word = word.get()
    translate = traductor.translate(entered_word)
    texttranslate.set(translate)
    print(translate)

#create a button 
bottom = tk.Button(root, text="Traducir", command=handle_input)

bottom.pack()

root.mainloop()

