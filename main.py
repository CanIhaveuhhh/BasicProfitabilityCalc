import tkinter as tk

def calculate_values():
    try:
        # Attempt to read values from entry widgets, defaulting to 0 if empty or invalid
        avg_order_value = float(avg_order_value_var.get() if avg_order_value_var.get() else 0)
        avg_cost = float(avg_cost_var.get() if avg_cost_var.get() else 0)
        return_percentage = float(return_percentage_var.get() if return_percentage_var.get() else 0) / 100
        conversion_rate = float(conversion_rate_var.get() if conversion_rate_var.get() else 0) / 100
        cost_per_click = float(cost_per_click_var.get() if cost_per_click_var.get() else 0)

        # Calculate dependent values
        avg_return_costs = avg_cost * return_percentage
        avg_gross = avg_order_value - avg_cost - avg_return_costs
        clicks_per_order = float('inf') if conversion_rate == 0 else 1 / conversion_rate
        cost_per_order = clicks_per_order * cost_per_click
        profit_after_marketing = avg_gross - cost_per_order

        # Update the output labels with calculated values
        avg_return_costs_var.set(f"{avg_return_costs:.2f} €")
        avg_gross_var.set(f"{avg_gross:.2f} €")
        clicks_per_order_var.set(f"{clicks_per_order:.2f}")
        cost_per_order_var.set(f"{cost_per_order:.2f} €")
        profit_after_marketing_var.set(f"{profit_after_marketing:.2f} €")
    except ValueError:
        # Reset the output labels if the input is invalid
        avg_return_costs_var.set("Invalid input")
        avg_gross_var.set("Invalid input")
        clicks_per_order_var.set("Invalid input")
        cost_per_order_var.set("Invalid input")
        profit_after_marketing_var.set("Invalid input")

def reset_values():
    # Clear all input variables
    avg_order_value_var.set("")
    avg_cost_var.set("")
    return_percentage_var.set("")
    conversion_rate_var.set("")
    cost_per_click_var.set("")
    
    # Recalculate values to reset outputs
    calculate_values()

# Create the main window
root = tk.Tk()
root.title("Product Profitability Calculator")

# Variable definitions
avg_order_value_var = tk.StringVar()
avg_cost_var = tk.StringVar()
return_percentage_var = tk.StringVar()
conversion_rate_var = tk.StringVar()
cost_per_click_var = tk.StringVar()

avg_return_costs_var = tk.StringVar()
avg_gross_var = tk.StringVar()
clicks_per_order_var = tk.StringVar()
cost_per_order_var = tk.StringVar()
profit_after_marketing_var = tk.StringVar()

# Create and place entry widgets for inputs, binding them to calculate_values on change
tk.Label(root, text="Average Order Value (€):").grid(row=0, column=0, sticky="e")
tk.Entry(root, textvariable=avg_order_value_var).grid(row=0, column=1, sticky="ew")
avg_order_value_var.trace_add("write", lambda *args: calculate_values())

tk.Label(root, text="Average Cost (€):").grid(row=1, column=0, sticky="e")
tk.Entry(root, textvariable=avg_cost_var).grid(row=1, column=1, sticky="ew")
avg_cost_var.trace_add("write", lambda *args: calculate_values())

tk.Label(root, text="Return Percentage (%):").grid(row=2, column=0, sticky="e")
tk.Entry(root, textvariable=return_percentage_var).grid(row=2, column=1, sticky="ew")
return_percentage_var.trace_add("write", lambda *args: calculate_values())

tk.Label(root, text="Conversion Rate (%):").grid(row=3, column=0, sticky="e")
tk.Entry(root, textvariable=conversion_rate_var).grid(row=3, column=1, sticky="ew")
conversion_rate_var.trace_add("write", lambda *args: calculate_values())

tk.Label(root, text="Cost per Click (€):").grid(row=4, column=0, sticky="e")
tk.Entry(root, textvariable=cost_per_click_var).grid(row=4, column=1, sticky="ew")
cost_per_click_var.trace_add("write", lambda *args: calculate_values())

# Create and place labels for displaying the results
tk.Label(root, text="Average Return Costs:").grid(row=5, column=0, sticky="e")
tk.Label(root, textvariable=avg_return_costs_var).grid(row=5, column=1, sticky="w")

tk.Label(root, text="Average Gross Profit:").grid(row=6, column=0, sticky="e")
tk.Label(root, textvariable=avg_gross_var).grid(row=6, column=1, sticky="w")

tk.Label(root, text="Clicks per Order:").grid(row=7, column=0, sticky="e")
tk.Label(root, textvariable=clicks_per_order_var).grid(row=7, column=1, sticky="w")

tk.Label(root, text="Total Cost per Order:").grid(row=8, column=0, sticky="e")
tk.Label(root, textvariable=cost_per_order_var).grid(row=8, column=1, sticky="w")

tk.Label(root, text="Net Profit After Marketing:").grid(row=9, column=0, sticky="e")
tk.Label(root, textvariable=profit_after_marketing_var).grid(row=9, column=1, sticky="w")

# Create and place the reset button
tk.Button(root, text="Reset", command=reset_values).grid(row=10, column=0, columnspan=2)

# Configure the grid to resize with the window
root.columnconfigure(1, weight=1)
for i in range(10):
    root.rowconfigure(i, weight=1)

# Initialize all outputs
calculate_values()

# Run the main loop
root.mainloop()
