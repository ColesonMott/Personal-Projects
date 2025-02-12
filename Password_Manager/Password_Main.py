# Version: 1.0
import Encrypter.Encrypter_Main as Encrypter

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import json, os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "Passwords.json")


def save():
    global data
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    messagebox.showinfo("Saved", "Passwords have been saved!")
    return

def load():
    global data
    with open(file_path, "r") as f:
        data = json.load(f)
    return

def add():
    global data
    website = simpledialog.askstring("Website", "Enter the website (without the \".com\"): ")
    username = simpledialog.askstring("Username", "Enter the username (no spaces): ")
    password = simpledialog.askstring("Password", "Enter the password (no spaces): ")
    if username is None or password is None:
        return
    data[website] = {"Username": Encrypter.encrypt(username), "Password": Encrypter.encrypt(password)}
    messagebox.showinfo("Added", "Password has been added!")
    return

def view():
    global data
    website = simpledialog.askstring("Website", "Enter the website (without the \".com\"): ")
    if website in data:
        messagebox.showinfo("Password", f"Username: {Encrypter.decrypt(data[website]['Username'])}\nPassword: {Encrypter.decrypt(data[website]['Password'])}")
    else:
        messagebox.showerror("Error", "Website not found!")
    return


def main():
    global data
    data = {}
    if os.path.exists(file_path):
        load()
    else:
        save()

    while True:
        choice = simpledialog.askstring("Choice", "What would you like to do? (Add, Save, Load, View, Quit): ")
        if choice is None:
            break
        if choice.lower() == "add":
            add()
        elif choice.lower() == "save":
            save()
        elif choice.lower() == "load":
            load()
            messagebox.showinfo("Loaded", "Passwords have been loaded!")
        elif choice.lower() == "quit":
            save()
            break
        elif choice.lower() == "view":
            view()
        else:
            messagebox.showerror("Error", "Invalid choice!")
            view()
    return

if __name__ == "__main__":
    main()