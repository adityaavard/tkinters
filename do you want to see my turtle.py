#imports
import tkinter
import customtkinter
import turtle
import subprocess
import PIL
import os


#initial setup
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")
ctk = customtkinter.CTk()
ctk.geometry("720x480")
ctk.title("customtkinter window setup")

#text
text = customtkinter.CTkLabel(ctk, text="do you want to see my turtle?")
text.pack(padx=50, pady=150)
#exit button
exit_button = customtkinter.CTkButton(ctk, text="exit", command=ctk.destroy)
exit_button.pack(padx=5, pady=4)

#turtle button

button = customtkinter.CTkButton(ctk, text="see turtle!", command=lambda: subprocess.run(["python", "mouse.py"]))
button.pack(padx=10, pady=15)
list = ["mrbeast", "lalith"]


img = customtkinter.CTkButton(ctk, text="open ctk image", command=lambda: os.startfile("wallpaper.jpg"))
img.pack()

#mainloop
ctk.mainloop()