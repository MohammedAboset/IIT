# 1) Smallest Tkinter App

# Import Tkinter
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("My First App")

# Set the window size
root.geometry("320x160")

# Cretae a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# Keep the window running
root.mainloop()

# 2) Buttons and Callbacks

# Import Tkinter
import tkinter as tk

# Function that runs when the button is clicked
def say_hello():
    print("Hello from the button!")

# Create the main window
root = tk.Tk()
root.title("Callbacks")

# Create the button
btn = tk.Button(root, text="Click me", command=say_hello)
btn.pack(pady=10)

# Keep the window running
root.mainloop()

# 3) Entry + Label

# Import Tkinter
import tkinter as tk

# Function to get the name and display a greeting
def greet():
    name = name_entry.get()
    output.config(text=f"Hello, {name or 'friend'}!")

# Create the main window
root = tk.Tk()
root.title("Greeter")

# Create the name label
tk.Label(root, text="Your name:").pack()

# Create the text box
name_entry = tk.Entry(root, width=24)
name_entry.pack()

# Create the Greet button
tk.Button(root, text="Greet", command=greet).pack(pady=6)

# Create the output label
output = tk.Label(root, text="")
output.pack()

# Keep the window running
root.mainloop()

# 4) Layout with Grid

# Import Tkinter
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Grid Example")

# Create labels in row 0
tk.Label(root, text="Row 0, Col 0").grid(row=0, column=0, padx=6, pady=6)
tk.Label(root, text="Row 0, Col 1").grid(row=0, column=1, padx=6, pady=6)

# Create buttons in row 1
tk.Button(root, text="A").grid(row=1, column=0, sticky="ew", padx=6, pady=6)
tk.Button(root, text="B").grid(row=1, column=1, sticky="ew", padx=6, pady=6)

# Allow the columns to expand
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Keep the window running
root.mainloop()

# 5) Temperature Converter

# Import Tkinter
import tkinter as tk

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Function that runs when Convert is clicked
def convert():
    try:
        f = float(entry_f.get())
        c = fahrenheit_to_celsius(f)
        result_var.set(f"{c:.2f} °C")
        status_var.set("Converted successfully.")
    except ValueError:
        result_var.set("")
        status_var.set("Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("360x160")

# Fahrenheit input
tk.Label(root, text="Fahrenheit:").grid(row=0, column=0, padx=8, pady=8, sticky="e")
entry_f = tk.Entry(root, width=12)
entry_f.grid(row=0, column=1, padx=8, pady=8, sticky="w")

# Convert button
tk.Button(root, text="Convert", command=convert).grid(row=0, column=2, padx=8, pady=8)

# Celsius result
tk.Label(root, text="Celsius:").grid(row=1, column=0, padx=8, pady=8, sticky="e")
result_var = tk.StringVar(value="")
tk.Label(root, textvariable=result_var).grid(row=1, column=1, padx=8, pady=8, sticky="w")

# Status message
status_var = tk.StringVar(value="")
tk.Label(root, textvariable=status_var, fg="green").grid(row=2, column=0, columnspan=3, pady=6)

# Allow the middle column to expand
root.columnconfigure(1, weight=1)

# Keep the window running
root.mainloop()

# 6) Click Counter

# Import Tkinter
import tkinter as tk

# Starting number
count = 0

# Function to increase the number
def increment():
    global count
    count += 1
    label.config(text=str(count))

# Create the main window
root = tk.Tk()
root.title("Click Counter")

# Create the number label
label = tk.Label(root, text="0", font=("Arial", 18))
label.pack(pady=10)

# Create the Add 1 button
tk.Button(root, text="Add 1", command=increment).pack(pady=6)

# Keep the window running
root.mainloop()

# 7) Stringvar Example

# Create a Tkinter variable
# name_var = tk.StringVar(value="")

# Connect the variable to an Entry box
# name_entry = tk.Entry(root, textvariable=name_var)

# 8) Mini Calculator

# Import Tkinter
import tkinter as tk

# CALCULATION FUNCTION
def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "×":
        return a * b
    elif op == "÷":
        return a / b
    
# COMPUTE FUNCTION
def compute():
    try:
        # Get the two numbers
        a = float(entry_a.get())
        b = float(entry_b.get())

        # Get the selected operation
        op = operation.get()

        # Calculate the answer
        answer = calculate(a, b, op)

        # Display the answer
        result.config(text=f"Result: {answer}")

    except ValueError:
        result.config(text="Please enter valid numbers.")

    except ZeroDivisionError:
        result.config(text="Cannot divide by zero.")
        
# CREATE THE WINDOW
root = tk.Tk()
root.title("Mini Calculator")
root.geometry("350x220")

# NUMBER INPUTS
tk.Label(root, text="First number:").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Second number:").pack()
entry_b = tk.Entry(root)
entry_b.pack()

# OPERATION DROPDOWN
operation = tk.StringVar(value="+")

tk.OptionMenu(root, operation, "+", "-", "×", "÷").pack(pady=10)

# COMPUTE BUTTON
tk.Button(root, text="Compute", command=compute).pack()

# RESULT
result = tk.Label(root, text="")
result.pack(pady=10)

# KEEP WINDOW RUNNING
root.mainloop()

