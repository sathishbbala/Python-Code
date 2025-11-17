from tkinter import *

def calculate_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km:.2f}")

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx = 20, pady = 20)

# Allow grid expansion
#for i in range(3):
#    window.columnconfigure(i, weight=1)
#for i in range(3):
#    window.rowconfigure(i, weight=1)

# Widgets
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0, sticky="nsew", pady=10)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0, sticky="w")

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1, sticky="e")

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1, sticky="nsew")

kilometer_label = Label(text="KMs")
kilometer_label.grid(column=2, row=1, sticky="w")

calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2, sticky="nsew", pady=20)

window.mainloop()