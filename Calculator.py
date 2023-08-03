import tkinter as tk


def delete():
    result_label.config(text="Result: ")
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            result = round(num1 + num2, 10)
        elif operator == "-":
            result = round(num1 - num2, 10)
        elif operator == "*":
            result = round(num1 * num2, 10)
        elif operator == "/":
            if num2 != 0:
                result = round(num1 / num2, 10)
            else:
                result = "Error: Division by zero"
        else:
            result = "Error: Invalid operator"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Error: Invalid input")


def convert_units():
    try:
        value = float(entry1.get())
        unit = unit_var.get()
        conversion = conversion_var.get()

        if unit == "cm" and conversion == "inches":
            result = round(value / 2.54, 2)
        elif unit == "inches" and conversion == "cm":
            result = round(value * 2.54, 2)
        elif unit == "kg" and conversion == "lbs":
            result = round(value * 2.20462, 2)
        elif unit == "lbs" and conversion == "kg":
            result = round(value / 2.20462, 2)
        else:
            result = "Error: Invalid conversion"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Error: Invalid input")


# Create the main window
window = tk.Tk()
window.title("Calculator")


# Labels for input fields
label1 = tk.Label(window, text="Number 1:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Number 2:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

# OptionMenu for selecting the operator
operator_var = tk.StringVar(window)
operator_var.set("+")
operator_option = tk.OptionMenu(window, operator_var, "+", "-", "*", "/")
operator_option.pack()

# Calculate and delete buttons
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()
delete_button = tk.Button(window, text='Delete', command=delete)
delete_button.pack()

# Label for displaying the result
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# OptionMenu and button for unit conversion
unit_var = tk.StringVar(window)
unit_var.set("cm")
conversion_var = tk.StringVar(window)
conversion_var.set("inches")

convert_units_button = tk.Button(window, text="Convert Units", command=convert_units)
convert_units_button.pack()

unit_option = tk.OptionMenu(window, unit_var, "cm", "inches", "kg", "lbs")
unit_option.pack()

conversion_option = tk.OptionMenu(window, conversion_var, "inches", "cm", "lbs", "kg")
conversion_option.pack()

# Start the main event loop
window.mainloop()