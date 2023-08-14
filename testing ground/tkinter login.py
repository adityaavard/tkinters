import customtkinter

import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()

window.geometry("500x350")

def login():
    print("login button clicked")



frame = customtkinter.CTkFrame(master=window)

frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="login system")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="login", command=lambda:
    print("password entered"))
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="remember me")
checkbox.pack(pady=12, padx=10)

window.mainloop()