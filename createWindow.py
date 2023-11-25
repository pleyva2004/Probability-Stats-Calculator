import tkinter 
import customtkinter

def clear_window():
    # Destroy all widgets in the window
    for widget in window.winfo_children():
        widget.destroy()

def on_button_click(button_text):

      if button_text == 'Statistics':
            make_stats_window()
            
      if button_text == 'Probability':
            make_prob_window() 

      if button_text == 'Back':
            clear_window()
            main_window()

def make_stats_window():
      clear_window()

      title = customtkinter.CTkLabel(window, text='Statistics')
      title.pack(padx = 10, pady = 10)

      button = customtkinter.CTkButton(window, text="Back",  command=lambda: on_button_click("Back"))
      button.pack(pady = 10)

def make_prob_window():
      #clear previous window
      clear_window()

      title = customtkinter.CTkLabel(window, text='Probability')
      title.pack(padx = 10, pady = 10)

      button = customtkinter.CTkButton(window, text="Back",  command=lambda: on_button_click("Back"))
      button.pack(pady = 10)

def main_window():
      # Adding UI Elements
      title = customtkinter.CTkLabel(window, text='Home')
      title.pack(padx = 10, pady = 10)


      # Adding Buttons
      button = customtkinter.CTkButton(window, text="Statistics",  command=lambda: on_button_click("Statistics"))
      button.pack(pady = 10)

      button = customtkinter.CTkButton(window, text="Probability",  command=lambda: on_button_click("Probability"))
      button.pack(pady = 10)

      
# System Settings
customtkinter.set_appearance_mode('Sytem')
customtkinter.set_default_color_theme('blue')

# Our app frame
window = customtkinter.CTk()
window.geometry('720x480')
window.title('Probability & Statistics Calculator')

# Open Window
main_window()
window.mainloop()




