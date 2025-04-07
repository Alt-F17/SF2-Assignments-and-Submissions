import time
import pyautogui
import pyperclip

text = pyperclip.paste()

# Wait 5 seconds before starting
print("Waiting 10 seconds before typing begins...")
time.sleep(10)

# Type the text very quickly (small interval makes it type fast)
pyautogui.write(text, interval=0.0001)

print("Typing completed!")