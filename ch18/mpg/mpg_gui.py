#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MyFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.message = ""
        self.pack()

        # Define string variables for text entry fields
        self.test = tk.StringVar()
        self.milesDriven = tk.StringVar()
        self.gallonsUsed = tk.StringVar()
        self.result = tk.StringVar()
        

        # Display the grid of components
        ttk.Label(self, text="Miles Driven:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.milesDriven).grid(
            column=1, row=0)
        ttk.Label(self, text="Gallons of Gas Used:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.gallonsUsed).grid(
            column=1, row=1)
        ttk.Label(self, text="Miles Per Gallon:").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.result, state ="readonly").grid(
            column=1, row=2)
        ttk.Button(self, text="Calculate", command=self.Calculate ).grid(
            column=3, row=3, sticky=tk.E)

        # Add padding to all components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)
        

    def GetFloat (self, val, tag):
        try:
            return float(val)
        except ValueError:
            self.message = f" {tag} must be a valid number.\n"
    def Calculate(self):
        self.message = ""
        miles = self.GetFloat(self.milesDriven.get(), "Miles Driven")
        gallons = self.GetFloat(self.gallonsUsed.get(), "Gallons Used")

        if self.message == "":
            mpg = miles / gallons
            mpg = round(mpg,2)
            self.result.set(mpg)
        else:
            messagebox.showerror("Error", self.message)
            



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Miles Per Gallon Calculator")
    MyFrame(root)
    root.mainloop()
