from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
      website: {
      "email": email,
      "password": password,
    }
  }
    


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any of the fields empty!")

    else:
      try:
        with open("data.json", "r") as data_file:
            #Reading old data
            data = json.load(data_file)
      except FileNotFoundError:
        with open ("data.json", "w") as data_file:
            #Saving updated data
            json.dump(new_data, data_file, indent=4)
      else:
          #Updating old data with new data
          data.update(new_data)
              
        with open ("data.json", "w") as data_file:
            #Saving updated data
            json.dump(data, data_file, indent=4)
      finally:        
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
#logo_img = PhotoImage(file="logo.png")
#canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


#Website Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

#Email/Username Label
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

#Password Label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#Generate Password button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

#Add Button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


#Website Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

#Email/Username Entry
email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "satoshi@gmail.com")

#Password Entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

window.mainloop()
