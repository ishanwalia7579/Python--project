import time
import os

def marquee_text(text, width=30, speed=0.1):
    # Add padding spaces to the text
    text = ' ' * width + text + ' ' * width
    while True:
        for i in range(len(text) - width + 1):
            # Clear the terminal (optional)
            os.system('cls' if os.name == 'nt' else 'clear')
            # Print the text slice
            print(text[i:i+width])
            time.sleep(speed)

# Run the marquee
marquee_text("Welcome to Python Marquee Demo!", width=50, speed=0.1)
