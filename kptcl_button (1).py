import tkinter as tk
import webbrowser

def open_website():
    webbrowser.open("https://kgis.ksrsac.in/KPTCL/")

root = tk.Tk()
root.title("My App")
root.geometry("300x150")

button = tk.Button(
    root,
    text="KPTCL",
    font=("Arial", 10),
    bg="#171718",
    fg="white",
    padx=10,
    pady=5,
    command=open_website
)
button.pack(expand=True)

root.mainloop()
