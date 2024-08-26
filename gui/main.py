
import tkinter as tk
from home_screen import show_home_screen

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ChessBot GUI")
    root.geometry("600x600")
    show_home_screen(root)
    root.mainloop()