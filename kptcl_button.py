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
    font=("Arial", 14),
    bg="#4285f4",
    fg="white",
    padx=20,
    pady=10,
    command=open_website
)
button.pack(expand=True)

root.mainloop()
