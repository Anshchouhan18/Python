'''import pywhatkit as pwk
for i in range(100):
    pwk.sendwhatmsg_instantly("+91", "Hello from Python")'''     # basic web framework structure 

'''import pyautogui
import time

contact = "+91"  # Replace with your contact
message = "Hello from Python!"

time.sleep(3)  # Gives you 3 seconds to open WhatsApp Desktop

for i in range(100):
    # Click on the search bar (adjust coordinates as per your screen)
    pyautogui.click(200, 100)  # Adjust coordinates
    time.sleep(0.5)

    # Type the contact number or name and press Enter
    pyautogui.write(contact)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)

    # Type the message and send
    pyautogui.write(message)
    pyautogui.press("enter")

    # Wait before sending the next message (reduce delay for faster speed)
    time.sleep(0.5)
'''   # made by chatgpt but you have to find your screen cordinates to direct the arrow to whatsapp which is getting little fishy



import os
import pyautogui
import time

# Replace with the contact's name or number (must match saved name in WhatsApp)
contact ="mummy"
message = "maan ki baat"

# Step 1: Open WhatsApp Desktop
os.system("start whatsapp:")  
time.sleep(5)  

# Step 2: Open the search bar using Ctrl + F (No mouse usage)
pyautogui.hotkey("ctrl", "f")
time.sleep(2)  

# Step 3: Type the contact name and press Enter
pyautogui.write(contact)
time.sleep(7)  
pyautogui.press("enter")
time.sleep(3)  

# Step 4: Send multiple messages to the contact
for i in range(50):
    pyautogui.write(message) 
    time.sleep(2)  
    pyautogui.press("enter")  # Send it
    time.sleep(0.5) 
