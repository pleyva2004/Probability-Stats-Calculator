import tkinter as tk
import customtkinter
import statsFunctions

#global history 
history = []

def stats_button_click():
      
      make_stats_window()

def mean_button_click():

      history.append('Mean') 
      print(history)

      standard_window('Mean')  

      def place_button(var, Button):
            if len(var.get()):
                  Button.pack()
            else:
                  Button.pack_forget()
      def getMean():
            nums = entry_text.get().split(',')
            for i,j in enumerate(nums):
                  nums[i] = float(j)

            myMean = statsFunctions.Mean(nums)
            print(f'Sample: {nums} \n \nAverage: {myMean}')
           

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

      def place_button(var, Button):
            if len(var.get()):
                  Button.pack()
            else:
                  Button.pack_forget()
      def getVariance():
            nums = entry_text.get().split(',')
            for i,j in enumerate(nums):
                  nums[i] = float(j)

            myVariance = statsFunctions.Variance(nums)
            print(f'Sample: {nums} \n \nVariance: {myVariance}')
           

      entry_text = tk.StringVar()

      entry = customtkinter.CTkEntry(window, textvariable=entry_text, width=500)
      entry.pack(pady=10)

      label = customtkinter.CTkLabel(window, text='Enter numbers seperated by commas.')
      label.pack(pady=10)

      button = customtkinter.CTkButton(window, text="Calculate", command=getVariance)
      
      entry_text.trace_add('write',lambda *args: place_button(entry_text, button))

def stanDev_button_click():

      history.append('Standard Deviation')
      print(history)

      standard_window('Standard Deviation')

      def place_button(var, Button):
            if len(var.get()):
                  Button.pack()
            else:
                  Button.pack_forget()
      def getVariance():
            nums = entry_text.get().split(',')
            for i,j in enumerate(nums):
                  nums[i] = float(j)

            myDeviation = statsFunctions.Standard_Dev(nums)
            print(f'Sample: {nums} \n \nStandard Deviation: {myDeviation}')
           

      entry_text = tk.StringVar()

      entry = customtkinter.CTkEntry(window, textvariable=entry_text, width=500)
      entry.pack(pady=10)

      label = customtkinter.CTkLabel(window, text='Enter numbers seperated by commas.')
      label.pack(pady=10)

      button = customtkinter.CTkButton(window, text="Calculate", command=getVariance)
      
      entry_text.trace_add('write',lambda *args: place_button(entry_text, button))

def stem_leaf_button_click():
      history.append('Stem and Leaf Plot')
      print(history)

      standard_window('Stem and Leaf Plot')

      def place_button(var, Button):
            if len(var.get()):
                  Button.pack()
            else:
                  Button.pack_forget()
      def plot():
            nums = entry_text.get().split(',')
            for i,j in enumerate(nums):
                  nums[i] = int(j)

            myStem_Leaf = statsFunctions.stem_leaf_plot(nums)

            clear_window()
            standard_window('Stem and Leaf Plot')

            for strB in myStem_Leaf:
                  label = customtkinter.CTkLabel(window, text=strB)
                  label.pack()



            #print(f'Sample: {nums} \n \nStandard Deviation: {myDeviation}')
           

      entry_text = tk.StringVar()

      entry = customtkinter.CTkEntry(window, textvariable=entry_text, width=500)
      entry.pack(pady=10)

      label = customtkinter.CTkLabel(window, text='Enter numbers seperated by commas.')
      label.pack(pady=10)

      button = customtkinter.CTkButton(window, text="Plot", command=plot)
      
      entry_text.trace_add('write',lambda *args: place_button(entry_text, button))





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
          
def clear_window():
    # Destroy all widgets in the window
    for widget in window.winfo_children():
        widget.destroy()
        
def make_stats_window():

      history.append('Statistics') # reading history by calling method 'append'
      print(history)
 
      standard_window('Statistics')

      button = customtkinter.CTkButton(window, text="Mean", command=mean_button_click)
      button.pack(pady=10)

      button = customtkinter.CTkButton(window, text="Variance", command=variance_button_click)
      button.pack(pady=10)
      
      button = customtkinter.CTkButton(window, text="Standard Deviation", command=stanDev_button_click)
      button.pack(pady=10)

      button = customtkinter.CTkButton(window, text="Stem and Leaf Plot", command=stem_leaf_button_click)
      button.pack(pady=10)

def make_prob_window():

      history.append('Probability')
      print(history)

      standard_window('Probability')

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




