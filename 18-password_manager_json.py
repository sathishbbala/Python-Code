from tkinter import *
from tkinter import messagebox
from random import shuffle, choice
import json

# Generate a 12 character password with atleast 1 upper case 1 spl char and a number
def generate_password():
    password_entry.delete(0, END)
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    special_chars=['!','#','$','%','&','(',')','*','+']
    password_letters=[]
    password=""
    for i in range(0,9):
        password_letters.append(choice(letters))     #8 Lower case characters
    password_letters.append(choice(letters).upper()) # 1 upper case
    password_letters.append(choice(numbers))         # 1 numeric
    password_letters.append(choice(special_chars))   # 1 special character
    shuffle(password_letters)
    password = "".join(password_letters)
    password_entry.insert(0, password)
    

#save password
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0: 
        messagebox.showinfo(title = "Information", message = "Either Website or Email or Password is empty. Please check!")
    else:
        is_ok = messagebox.askokcancel(title = website, message = f"Saving Email as {email} and Password as {password} for the website {website}")
        if is_ok:
            try:
                with open('data.json', "r") as data_file:
                    data = json.load(data_file)
            except (json.JSONDecodeError,FileNotFoundError):
                data={}
            finally:
                data.update(new_data)
                with open('data.json', "w") as data_file:
                    json.dump(data, data_file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# Search for the password 
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showinfo(title="Error", message="File not found or JSON File is empty. Please check!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"{website} information not found")

     
# Create a window 
window = Tk()
window.title("Password Generator")
window.config(padx = 20, pady = 20)

# Canvas creation
canvas = Canvas(height = 200, width = 200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0, column = 1)

# create labels
website_label = Label(text = "Website")
website_label.grid(row = 1, column = 0)
email_label = Label(text = "Email Address")
email_label.grid(row = 2, column = 0)
password_label = Label(text = "Password")
password_label.grid(row = 3, column = 0)

# Entries
website_entry = Entry(width = 25)
website_entry.grid(row = 1, column = 1)
website_entry.focus()
email_entry = Entry(width = 35)
email_entry.grid(row = 2, column = 1, columnspan = 2)
email_entry.insert(0, "alan@testmail.com")
password_entry = Entry(width = 35)
password_entry.grid(row = 3, column = 1, columnspan = 2)

#Buttons
generate_password_button = Button(text = "Generate Password", command = generate_password)
generate_password_button.grid(row = 3, column = 2)
add_button = Button(text = "Add", width = 36, command = save)
add_button.grid(row = 4, column = 1, columnspan = 2)
search_button = Button(text = "Search", command = find_password)
search_button.grid(row = 1, column = 2)
window.mainloop()