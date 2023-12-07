import tkinter as tk

def clear_window():
    # Destroy all widgets in the window
    for widget in window.winfo_children():
        widget.destroy()

def on_button_click(button_text):
    clear_window()
    
    # Display a message based on the clicked button
    label = tk.Label(window, text=f"You clicked the {button_text} button!")
    label.pack(pady=10)

def get_entry_text():
    text = entry.get()
    print("Entry Text:", text)

# Create the main window
window = tk.Tk()
window.title("Clear Window on Button Click")

# Create buttons
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# Create a button to get the entry text
button = tk.Button(window, text="Get Entry Text", command=get_entry_text)
button.pack()

# Start the Tkinter event loop
window.mainloop()
