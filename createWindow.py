import tkinter as tk
import customtkinter
import statsFunctions

#global history 
history = []

def clear_window():
    # Destroy all widgets in the window
    for widget in window.winfo_children():
        widget.destroy()

def stats_button_click():
      
      make_stats_window()

def prob_button_click():
      
      make_prob_window()

def back_button_click():

      clear_window()

      global history
      temp = history[-2]
      print(temp)
      history = history[:-2] # writing history -> becomes local variable
      print(history)

      if temp == 'Home':
            main_window()
      elif temp == 'Statistics':
            make_stats_window()
      elif temp == 'Probability':
            make_prob_window()
          
def make_stats_window():

      history.append('Statistics')
      print(history)

      standard_window('Statistics')

      button = customtkinter.CTkButton(window, text="Mean", command=mean_button_click)
      button.pack(pady=10)

      button = customtkinter.CTkButton(window, text="Variance", command=variance_button_click)
      button.pack(pady=10)

def make_prob_window():

      history.append('Probability')
      print(history)

      standard_window('Probability')

def mean_button_click():

      history.append('Mean') # reading history by calling method 'append'
      print(history)

      def place_button(var, Button):
            if len(var.get()):
                  Button.pack()
            else:
                  Button.pack_forget()
      def getMean():
            nums = entry_text.get().split(',')
            for i,j in enumerate(nums):
                  nums[i] = int(j)

            myMean = statsFunctions.Mean(nums)
            print(f'Sample: {nums} \n \nAverage: {myMean}')
           
      
      
      standard_window('Mean')  

      entry_text = tk.StringVar()

      entry = customtkinter.CTkEntry(window, textvariable=entry_text, width=500)
      entry.pack(pady=10)

      label = customtkinter.CTkLabel(window, text='Enter numbers seperated by commas.')
      label.pack(pady=10)

      button = customtkinter.CTkButton(window, text="Calculate", command=getMean)
      
      entry_text.trace_add('write',lambda *args: place_button(entry_text, button))

def variance_button_click():

      history.append('Variance')
      print(history)

      standard_window('Variance')

def standard_window(title):
      clear_window()

      title_of_widow = customtkinter.CTkLabel(window, text=f'{title}')
      title_of_widow.pack(padx=10, pady=10)

      button = customtkinter.CTkButton(window, text="Back",  command=back_button_click)
      button.place(x=10, y=10)

def main_window():

      history.append('Home')
      print(history)


      # Adding UI Elements
      title = customtkinter.CTkLabel(window, text='Home')
      title.pack(padx = 10, pady = 10)

      # Adding Buttons
      button = customtkinter.CTkButton(window, text="Statistics",  command=stats_button_click)
      button.pack(pady = 10)

      button = customtkinter.CTkButton(window, text="Probability",  command=prob_button_click)
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




