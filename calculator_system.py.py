import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pygame

#----------FOR MUSIC----------#
def play_background_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)  # -1 means play indefinitely

# Replace the 'music_file.mp3' with the path to music file
music_file_path = 'for_calculator_system.mp3'

play_background_music(music_file_path)

# Adding a delay to keep the script running while the music plays
pygame.time.delay(10)  

#----------CALCULATOR SYSTEM----------#
def calculate_max_apples():
    try:
        money = float(money_entry.get())
        apple_price = float(price_entry.get())

        # Calculate the maximum number of apples
        max_apples = int(money // apple_price)

        # Calculate the remaining money after buying apples
        remaining_money = money % apple_price

        # Display the result
        result_label.config(text=f"Having an amount of {money}, you can buy {max_apples} apples.\nAfter buying apples, you will have {remaining_money:.2f} remaining. \n \n \n What are you waiting for? Order now at \n BICOLANO'S FRESHLY PICK FRUITS order system.")
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")

# Create the main Tkinter window
app = tk.Tk()
app.title("BICOLANO'S FRESHLY PICK FRUITS' AUTOMATIC CALCULATOR")

# Load the background image
background_image = PhotoImage(file="banner.png")

# Create a canvas with the background image
canvas = tk.Canvas(app, width=background_image.width(), height=background_image.height())
canvas.pack()

# Display the background image
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Create and place widgets
money_label = tk.Label(app, text="Enter the amount of money:")
money_label.pack(pady=10)

money_entry = tk.Entry(app)
money_entry.pack(pady=10)

price_label = tk.Label(app, text="Enter the price of an apple:")
price_label.pack(pady=10)

price_entry = tk.Entry(app)
price_entry.pack(pady=10)

calculate_button = tk.Button(app, text="Calculate", command=calculate_max_apples)
calculate_button.pack(pady=10)

result_label = tk.Label(app, text="The maximum number of apples I can buy \n and the remaining money that I will receive will be display here. ")
result_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()