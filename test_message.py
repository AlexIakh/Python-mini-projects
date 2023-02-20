import time
import random, string
import pyautogui as gui

number= input("Enter the number: ")
message=input("Escribe lo que quieras enviar: ")
time.sleep(5)

for i in range(int(number)):
    #stri= string.ascii_lowercase
    #message ="".join(random.sample(stri, 10))
    #message=input("Escribe lo que quieras enviar: ")
    gui.typewrite(message)
    gui.press('Enter')