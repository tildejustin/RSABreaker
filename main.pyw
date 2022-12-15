"""
RSA Breaker
9 Dec. 2022
"""

import tkinter as tk
from tkinter import ttk
import decrypt
import encrypt
import typing


class Root(tk.Tk):
    """
    Makes an instance of a tk class with window settings automatically managed.

    Arguments:
        none

    Ar
    """
    def __init__(self) -> None:
        super().__init__()
        self.geometry("1000x600")
        self.resizable(False, False)
        self.title("RSA Breaker")
        self.iconbitmap("assets/lock.ico")
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except ModuleNotFoundError:
            pass

    # def gui(self) -> dict[str, int, int, str]:


    # def enter(self):
    #     my_input = Input(in_e.get())


# class Input():
#     def __init__(self) -> None:
#         self.p = p
#         self.q = q
#         self.e = e
#         self.encoded_text = text

def main():
    root = Root()
    root.mainloop()


if __name__ == "__main__":
    main()
