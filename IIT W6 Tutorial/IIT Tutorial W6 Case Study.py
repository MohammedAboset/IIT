# Student Marks Calculator

# 1) Calculate Average and Result

def calculate_marks(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3

    if average >= 50:
        result = "Passed"
    else:
        result = "Failed"

    return average, result

# 2) Gui

# Import Tkinter
import tkinter as tk

# Calculate button function
def show_result():
    try:
        # Get the three marks
        mark1 = float(entry1.get())
        mark2 = float(entry2.get())
        mark3 = float(entry3.get())

        # Calculate average and result
        average, result = calculate_marks(mark1, mark2, mark3)

        # Display the result
        output.config(text=f"Average: {average:.2f}\nResult: {result}")

    except ValueError:
        output.config(text="Please enter valid marks.")

# Create the window
root = tk.Tk()
root.title("Student Marks Calculator")
root.geometry("350x300")

# Mark inputs
tk.Label(root, text="Mark 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Mark 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Mark 3:").pack()
entry3 = tk.Entry(root)
entry3.pack()

# Calculate button
tk.Button(root, text="Calculate", command=show_result).pack(pady=10)

# Result
output = tk.Label(root, text="")
output.pack(pady=10)

# Keep window running
root.mainloop()
