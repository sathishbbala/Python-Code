from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card={}

def next_card():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="#000000")
    canvas.itemconfig(card_word, text=current_card["French"], fill="#000000")
    canvas.itemconfig(card_background_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="#FFFFFF")
    canvas.itemconfig(card_word, text=current_card["English"], fill="#FFFFFF")


window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Create a canvas and place the card_front image and text 
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Add 2 buttons below the image
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()