
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import random 
from datetime import date
from datetime import datetime

import pygame
import os


#----------FOR MUSIC----------#
def play_background_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)  # -1 means play indefinitely

# Replace the 'music_file.mp3' with the path to music file
music_file_path = 'bg_music.mp3'

play_background_music(music_file_path)

# Adding a delay to keep the script running while the music plays
pygame.time.delay(10)  


#----------FOR INTRO----------#

class MultiPageApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("BICOLANO'S FRESHLY PICK FRUITS")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Page1, Page2, Page3, Page4, Page5):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NWE")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load background image for the start page
        bg_image = ImageTk.PhotoImage(Image.open("logo.png"))
        background_label = tk.Label(self, image=bg_image)
        background_label.image = bg_image
        background_label.pack(fill="both", expand=True)

        label = tk.Label(self, text="Welcome Mr. Danilo Madrigalejos!", font=("Sans Serif", 18, "bold"), foreground="white", background="#00688B")
        label.pack(pady=10)

        next_button = tk.Button(self, text="Next", command=lambda: controller.show_frame(Page1))
        next_button.pack(pady=10)

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load background image for Page 1
        bg_image = ImageTk.PhotoImage(Image.open("heard.png"))
        background_label = tk.Label(self, image=bg_image)
        background_label.image = bg_image
        background_label.pack(fill="both", expand=True)

        label = tk.Label(self, text="I heard that you were asked by your \n mom to buy some apples and oranges? \n Is it true? \n Click the \"Next\" if true. \n Click the \"Exit\" or the \"Exit Button\" if false.", font=("Helvetica", 10), foreground="white", background="#00688B")
        label.pack(pady=10)
        
        next_button = tk.Button(self, text="Next", command=lambda: controller.show_frame(Page2))
        next_button.pack(pady=10)

        back_button = tk.Button(self, text="Exit", command=lambda: controller.show_frame(StartPage))
        back_button.pack(pady=10)
        
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load background image for Page 2
        bg_image = ImageTk.PhotoImage(Image.open("thinking.png"))
        background_label = tk.Label(self, image=bg_image)
        background_label.image = bg_image
        background_label.pack(fill="both", expand=True)

        label = tk.Label(self, text="Then, how many apple and orange \n would you like to buy?", font=("Helvetica", 10), foreground="white", background="#00688B")
        label.pack(pady=10)
        
        next_button = tk.Button(self, text="Next", command=lambda: controller.show_frame(Page3))
        next_button.pack(pady=10)
        
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Page2))
        back_button.pack(pady=10)

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load background image for Page 3
        bg_image = ImageTk.PhotoImage(Image.open("perhaps.png"))
        background_label = tk.Label(self, image=bg_image)
        background_label.image = bg_image
        background_label.pack(fill="both", expand=True)

        label = tk.Label(self, text="Perhaps, 25 apples and 15 oranges?", font=("Helvetica", 10), foreground="white", background="#00688B")
        label.pack(pady=10)
        
        back_button = tk.Button(self, text="Next", command=lambda: controller.show_frame(Page4))
        back_button.pack(pady=10)
        
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Page2))
        back_button.pack(pady=10)
        
class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load background image for Page 4
        bg_image = ImageTk.PhotoImage(Image.open("thinking.png"))
        background_label = tk.Label(self, image=bg_image)
        background_label.image = bg_image
        background_label.pack(fill="both", expand=True)

        label = tk.Label(self, text="More? \n" + "Then, visit the \"BICOLANO'S FRESHLY PICK FRUITS,\" to order. \n It is easy and very convient store", font=("Helvetica", 10), foreground="white", background="#00688B")
        label.pack(pady=10)
        
        next_button = tk.Button(self, text="Next", command=lambda: controller.show_frame(Page5))
        next_button.pack(pady=10)
        
        back_button = tk.Button(self, text="Exit", command=lambda: controller.show_frame(Page3))
        back_button.pack(pady=10)
        
class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load background image for Page 5
        bg_image = ImageTk.PhotoImage(Image.open("click_the_exit_tab.png"))
        background_label = tk.Label(self, image=bg_image)
        background_label.image = bg_image
        background_label.pack(fill="both", expand=True)

        label = tk.Label(self, text="Just click the exit tab. \n Enjoy. \n Have a great day.", font=("Helvetica", 10), foreground="white", background="#00688B")
        label.pack(pady=10)
        
if __name__ == "__main__":
    app = MultiPageApp()
    app.mainloop()



#----------#-----ORDER SYSTEM-----#---------#
#Root of the system
root = Tk()
root.title("BICOLANO'S FRESHLY PICK FRUITS")

#Price
prices = {
    "Apple": 20,    
    "Orange": 25,
    "Mango": 30,
    "Strawberry": 60,
    "Lemon": 20,
}

#----------FUNCTIONS----------#
#Region at the Right: Remove Button Functionality
def remove():
    fruits_to_remove = display_label.cget("text") + "...." + str(prices[display_label.cget("text")])
    transaction_list  = order_transaction.cget("text").split("pesos ")
    transaction_list.pop(len(transaction_list)-1)
    
    if fruits_to_remove in transaction_list:
        #update transaction label
        transaction_list.remove(fruits_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item + "pesos "
            
        order_transaction.configure(text = "updated_order")
        
        #update transaction total
        order_total = total_label.cget("text").replace("Total", "")
        order_total = order_total.replace("pesos", "")
        updated_total = int(order_total) - prices[display_label.cget("text")]
        total_label.configure(text = "Total : " + str(updated_total) + "pesos")
      
#Region at the Middle: Add to Order Button Functionality
def add():
    #updating the transaction label
    current_order = order_transaction.cget("text")
    added_fruit = display_label.cget("text") + (".....") + str(prices[display_label.cget("text")]) + str("pesos") + ("\n") 
    updates_order = current_order + added_fruit
    order_transaction.configure(text = updates_order)
     
    #updating the order total label
    order_total = total_label.cget("text").replace("Total : ", "")
    order_total = order_total.replace("pesos", "")
    
    current_total = int(''.join(filter(str.isdigit, order_total)))
    
    updated_total = current_total + prices[display_label.cget("text")]
    total_label.config(text=f"Total: {updated_total}")
    
#Generating A Random Order ID When Starting A New Order
def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    order_id = "BICOL_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))
        
    order_id += random_letters + random_digits
    return order_id

#Diplay Button Function: Generating Receipt from Order Button
def order():
    new_receipt = order_ID_Label.cget("text")
    new_receipt = new_receipt.replace("ORDER ID: ", "")
    transaction_list = order_transaction.cget("text").split("pesos ")
    transaction_list.pop(len(transaction_list) - 1)
    
    order_day = date.today()
    order_time = datetime.now()
    
    for item in transaction_list:
        item + "pesos "
        
    with open(new_receipt, 'w') as file:
        file.write("BICOLANO'S FRESHLY PICK FRUITS")
        file.write("\n")
        file.write("---------------------")
        file.write("\n")
        file.write(order_day.strftime("Date: %Y-%m-%d"))
        file.write("\n")
        file.write(order_time.strftime("Time: %H:%M:%S"))
        file.write("\n\n")
        for item in transaction_list:
            file.write(item + "\n")
        file.write("\n\n")
        file.write(total_label.cget("text"))
        
    total_label.configure(text = "TOTAL : 0 pesos")
    order_ID_Label.configure(text= "ORDER ID: " + ORDER_ID())
    order_transaction.configure(text = " ")

#Region at the Left: Display Functions where it generates different color when you click
def displayapple():
    apple_fruit.configure(
        relief = "sunken",
        style = "selected_fruit.TFrame"
    )
    
    orange_fruit.configure(style = "fruits_frame.TFrame")
    mango_fruit.configure(style = "fruits_frame.TFrame")
    strawberry_fruit.configure(style = "fruits_frame.TFrame")
    lemon_fruit.configure(style = "fruits_frame.TFrame")
    
    display_label.configure(
        image = apple_fruit_image,
        text = "Apple",
        font = ('Helvetica', 14, "bold"),
        compound = "bottom",
        padding = (5, 5, 5, 5),  
    )
    
def displayorange():
    orange_fruit.configure(
        relief = "sunken",
        style = "selected_fruit.TFrame"
    )
    
    apple_fruit.configure(style = "fruits_frame.TFrame")
    mango_fruit.configure(style = "fruits_frame.TFrame")
    strawberry_fruit.configure(style = "fruits_frame.TFrame")
    lemon_fruit.configure(style = "fruits_frame.TFrame")
    
    display_label.configure(
        image = orange_fruit_image,
        text = "Orange",
        font = ('Helvetica', 14, "bold"),
        compound = "bottom",
        padding = (5, 5, 5, 5),  
    )
    
def displaymango():
    mango_fruit.configure(
        relief = "sunken",
        style = "selected_fruit.TFrame"
    )
    
    orange_fruit.configure(style = "fruits_frame.TFrame")
    apple_fruit.configure(style = "fruits_frame.TFrame")
    strawberry_fruit.configure(style = "fruits_frame.TFrame")
    lemon_fruit.configure(style = "fruits_frame.TFrame")
    
    display_label.configure(
        image = mango_fruit_image,
        text = "Mango",
        font = ('Helvetica', 14, "bold"),
        compound = "bottom",
        padding = (5, 5, 5, 5),  
    )

def displaystrawberry():
    strawberry_fruit.configure(
        relief = "sunken",
        style = "selected_fruit.TFrame"
    )
    
    orange_fruit.configure(style = "fruits_frame.TFrame")
    mango_fruit.configure(style = "fruits_frame.TFrame")
    apple_fruit.configure(style = "fruits_frame.TFrame")
    lemon_fruit.configure(style = "fruits_frame.TFrame")
    
    display_label.configure(
        image = strawberry_fruit_image,
        text = "Strawberry",
        font = ('Helvetica', 14, "bold"),
        compound = "bottom",
        padding = (5, 5, 5, 5),  
    )
    
def displaylemon():
    lemon_fruit.configure(
        relief = "sunken",
        style = "selected_fruit.TFrame"
    )
    
    orange_fruit.configure(style = "fruits_frame.TFrame")
    mango_fruit.configure(style = "fruits_frame.TFrame")
    strawberry_fruit.configure(style = "fruits_frame.TFrame")
    apple_fruit.configure(style = "fruits_frame.TFrame")
    
    display_label.configure(
        image = lemon_fruit_image,
        text = "Lemon",
        font = ('Helvetica', 14, "bold"),
        compound = "bottom",
        padding = (5, 5, 5, 5),  
    )
    


#----------STYLING AND IMAGES----------#
#Configuration of the Regions
s= ttk.Style()
s.configure('main_frame.TFrame', background = "#2B2B28")
s.configure('fruits_frame.TFrame', background = "#4A4A48")
s.configure('display_frame.TFrame', background = "0F1110")
s.configure('order_frame.TFrame', background = "#0000FF")
s.configure('fruits_frame.TFrame', background = "#00FA9A", relief = "raised")
s.configure('selected_fruit.TFrame', background  = "#8470FF")
s.configure('fruits_frame.TLabel',
            background = '#8B1C62',
            font = ("Arial", 12, "bold"),
            foreground = "white",
            padding = (5, 5, 5, 5),
            width = 21
            )
s.configure('order_transaction.TLabel',
            background = "#4A4A48",
            font = ('Arial', 15),
            foreground = "black",
            #wraplength = 170,
            anchor = "NW",
            padding = (3, 3, 3, 3)
            )

#Region Images: Top Banner Images
logo_image_object = Image.open("logo.png").resize((120, 130))
logo_image = ImageTk.PhotoImage(logo_image_object)

top_banner_object = Image.open("banner.png").resize((910, 130))
top_banner_image = ImageTk.PhotoImage(top_banner_object)

#Region at the Middle: Fruits Images
display_default_image_object = Image.open("display_default_image.png") .resize((500, 450))
display_default_image = ImageTk.PhotoImage (display_default_image_object)

apple_fruit_image_object = Image.open("apple.jpg"). resize((490, 450))
apple_fruit_image = ImageTk.PhotoImage (apple_fruit_image_object)

orange_fruit_image_object = Image.open("orange.jpg"). resize((490, 450))
orange_fruit_image = ImageTk.PhotoImage (orange_fruit_image_object)

mango_fruit_image_object = Image.open("mango.jpg"). resize((490, 450))
mango_fruit_image = ImageTk.PhotoImage (mango_fruit_image_object)

strawberry_fruit_image_object = Image.open("strawberry.jpg"). resize((490, 450))
strawberry_fruit_image = ImageTk.PhotoImage (strawberry_fruit_image_object)

lemon_fruit_image_object = Image.open("lemon.png"). resize((490, 450))
lemon_fruit_image = ImageTk.PhotoImage (lemon_fruit_image_object)



#----------WIDGETS----------#
#Region Frames: Section Frames
main_frame = ttk.Frame(root, width = 800, height = 580, style = 'main_frame.TFrame')
main_frame.grid(row = 0, column = 0, sticky = "NSEW")

top_banner_frame = ttk.Frame(main_frame)
top_banner_frame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

fruits_frame = ttk.Frame(main_frame, style = 'fruits_frame.TFrame')
fruits_frame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

display_frame = ttk.Frame(main_frame, style = 'display_frame.TFrame')
display_frame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

order_frame = ttk.Frame(main_frame, style = 'display_frame.TFrame')
order_frame.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

#Region at the Left: Various Fruits Frames
apple_fruit = ttk.Frame(fruits_frame, style = "fruits_frame.TFrame")
apple_fruit.grid(row = 1, column = 0, sticky = "NSEW")

orange_fruit = ttk.Frame(fruits_frame, style = "fruits_frame.TFrame")
orange_fruit.grid(row = 2, column = 0, sticky = "NSEW")

mango_fruit = ttk.Frame(fruits_frame, style = "fruits_frame.TFrame")
mango_fruit.grid(row = 3, column = 0, sticky = "NSEW")

strawberry_fruit = ttk.Frame(fruits_frame, style = "fruits_frame.TFrame")
strawberry_fruit.grid(row = 4, column = 0, sticky = "NSEW")

lemon_fruit = ttk.Frame(fruits_frame, style = "fruits_frame.TFrame")
lemon_fruit.grid(row = 5, column = 0, sticky = "NSEW")

#Region Top:Banner Section
logo_label= ttk.Label(top_banner_frame, image = logo_image, background= "#0F1110")
logo_label.grid(row = 0, column = 0, sticky = "W")

market_banner_label = ttk.Label(top_banner_frame, image = top_banner_image, background= "#0F1110")
market_banner_label.grid(row = 0, column = 1, sticky= "NSEW") 

#Region at the Left: Fruits Section
main_fruit_section_label = ttk.Label(fruits_frame, text = "Various Kinds of Fruits", style = "fruits_frame.TLabel")
main_fruit_section_label.grid(row = 0, column = 0, sticky = "WE")
main_fruit_section_label.configure(
    anchor = 'center',
    font = ("Helvetica", 14, "bold")  
)

#Region at the Left: Fruits Section: Various Kinds of Fruits (Labels)
apple_fruit_label= ttk.Label(apple_fruit, text = "Apple\n P20", style = "fruits_frame.TLabel")
apple_fruit_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

orange_fruit_label= ttk.Label(orange_fruit, text = "Orange\n P25", style = "fruits_frame.TLabel")
orange_fruit_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

mango_fruit_label= ttk.Label(mango_fruit, text = "Mango\n P30", style = "fruits_frame.TLabel")
mango_fruit_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

strawberry_fruit_label= ttk.Label(strawberry_fruit, text = "Strawberry\n P60", style = "fruits_frame.TLabel")
strawberry_fruit_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

lemon_fruit_label= ttk.Label(lemon_fruit, text = "Lemon\n P20", style = "fruits_frame.TLabel")
lemon_fruit_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

#Region at the Left: Fruits Section: Display Button
apple_fruit_display_button = ttk.Button(apple_fruit, text = "Display", command = displayapple)
apple_fruit_display_button.grid(row = 0, column = 1, padx = 10)

orange_fruit_display_button = ttk.Button(orange_fruit, text = "Display", command = displayorange)
orange_fruit_display_button.grid(row = 0, column = 1, padx = 10)

mango_fruit_display_button = ttk.Button(mango_fruit, text = "Display", command = displaymango)
mango_fruit_display_button.grid(row = 0, column = 1, padx = 10)

strawberry_fruit_display_button = ttk.Button(strawberry_fruit, text = "Display", command = displaystrawberry)
strawberry_fruit_display_button.grid(row = 0, column = 1, padx = 10)

lemon_fruit_display_button = ttk.Button(lemon_fruit, text = "Display", command = displaylemon)
lemon_fruit_display_button.grid(row = 0, column = 1, padx = 10)

#Region at the Middle: Display Section of Order and Remove Button
display_label = ttk.Label(display_frame, image = display_default_image)
display_label.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 2)

add_order_button = ttk.Button(display_frame, text = "Add to Order", command = add)
add_order_button.grid(row = 1, column = 0, sticky = "NSEW")

remove_order_button = ttk.Button(display_frame, text = "Remove", command = remove)
remove_order_button.grid(row = 1, column = 1, sticky = "NSEW")

#Region at the Middle: Order and Remove Button Title Label
order_title_label = ttk.Label(order_frame, text = "ORDER")
order_title_label.configure(
    foreground = "white", background = "#6A5ACD",
    font = ("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5)  
)
order_title_label.grid(row = 0, column = 0, sticky = "EW")

order_ID_Label = ttk.Label(order_frame, text = "ORDER ID: " + ORDER_ID())
order_ID_Label.configure(
    background = "#D02090",
    foreground = "white",
    font = ("Helvetica", 11, "bold"),
    anchor = "center"
)
order_ID_Label.grid(row = 1, column = 0, sticky = "EW", pady = 1)

order_transaction = ttk.Label(order_frame, style = 'order_transcation.TLabel')
order_transaction.grid(row = 2, column = 0, sticky = "NWSE")

total_label = ttk.Label(order_frame, text = "Total: 0", style = "total_label.TLabel")
total_label.grid(row = 3, column = 0, sticky = "EW")

order_button = ttk.Button(order_frame, text = "Order", command = order)
order_button.grid (row = 4, column = 0, sticky = "EW")

                            



#----------GRID CONFIGURATIONS--------#
fruits_frame.columnconfigure(2, weight = 1)
fruits_frame.rowconfigure(1, weight = 1)
fruits_frame.columnconfigure(0, weight = 1)
fruits_frame.rowconfigure(1, weight = 1)
fruits_frame.rowconfigure(2, weight = 1)
fruits_frame.rowconfigure(3, weight = 1)
fruits_frame.rowconfigure(4, weight = 1)
fruits_frame.rowconfigure(5, weight = 1)

order_frame.columnconfigure(0, weight = 1)
order_frame.rowconfigure(2, weight = 1)

root.mainloop()