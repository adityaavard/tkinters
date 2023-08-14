#imports
import tkinter
import customtkinter

#initial setup
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

#window setup
p = customtkinter.CTk()
p.geometry("420x380")
p.title("test")

#using lambda
button = customtkinter.CTkButton(p, text="button", command=lambda:
     print("clicked button!"))
button.pack(padx=10, pady=15)
#mainloop
p.mainloop()