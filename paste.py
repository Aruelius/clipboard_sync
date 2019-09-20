import pyperclip
import time

paste_list = []

while True:
    text = pyperclip.paste()
    if text not in paste_list:
        print(text)
        paste_list.append(text)
    time.sleep(1)