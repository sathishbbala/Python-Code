import tkinter

window = tkinter.Tk()
window.title("My First Window")
window.minsize(width=1200, height=600)

# Label
my_label = tkinter.Label(text = "I am a Label", font = ("Arial", 24, "bold"))
my_label.pack()



# To make the window stay up
window.mainloop()