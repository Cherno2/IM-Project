#!/usr/bin/env python3
#inport Libary tkinter
import tkinter as tk
#import package random for random number function
import random
# Used to derice special functions from general functions
from functools import partial

#creat random number between 1 and 100
guessnumber = random.randint(1,100)
tries = 0

#Function decides answer to the input and gives it to the def main()
def input_evaluate(inputfield, output_label, tries_label):
    
    global tries 

    try:
        entery = int(inputfield.get()) #make variable to int
    except ValueError: #Int is expected if the input is wrong this is the answer 
        reply = "We search a number!" 
    #Input is right, so we made 6 different cases with different answers 
    else:
        if entery == 0:
            reply = "Ohno, don´t we search a number from 1-100?"
        elif entery < 0:
            reply = "We search a positive number!"
        elif entery > 100:
            reply = "Way too big maximum 100"
        elif entery == guessnumber:
            reply = "Congratulations you have guessed the right number!"
        elif entery < guessnumber:
            reply = "Sorry, too small"
        elif entery > guessnumber:
            reply = "Sorry, too big"
        else:
            assert False
    #Counts +1 for each try
    tries +=1
    tries_label["text"] = tries
    #here we write in output_lable the reply 
    output_label["text"] = reply
    

def main():
    
    title = "Guess Number Game"
    #Define the window
    window = tk.Tk()
    #text which is shown in the top left corner
    window.title(title)
    #Background colour
    window["background"] = "#E0EEE0"
    #"Headline"
    tk.Label(
        window,
        text=title,
        fg="blue",
        font=("Helvetica Neue", 30),
    ).grid(row = 0, column = 1)     
    #grid is one of three layout (pack,grid place)
    #important to use the same layout for all labels!
    #grid works with colum and row (matrix)
    number_label = tk.Label(
        window,
        text="Input number between 1-100:",
        font=("Arial", 15),
    )
    number_label.grid(row=1, column=0)

    output_label = tk.Label(
        window,
        text="Let´s start :)",
        font=("Arial", 12), #With font you can edit font and size
    )
    output_label.grid(row = 2, column = 1)
   
    text = "Number between 1 - 100"
    #tk.Entry: where the input is made
    inputfield = tk.Entry(window, width=len(text), text=text)
    inputfield.grid(row = 1, column = 1)

    triestext_label = tk.Label(
        window,
        text="How many tries:",
    )
    triestext_label.grid(row = 3, column = 0 )

    tries_label = tk.Label(
        window,
        text= "0",
    )
    tries_label.grid(row=4,column=0)
    
    #button function from tk library
    tk.Button(
        window,
        text="Submit trail!",
        font=("Arial", 12),
        bg="orange", #bg defines background of butten
        command=partial(input_evaluate, inputfield, output_label, tries_label),
    ).grid(row = 1, column = 2)

    exit_button= tk.Button(window, text="Close Game", command=window.quit)
    #in command you say what button should do
    exit_button.grid(row=4, column=2)
    #tells Python to tun the TKinter event loop
    #used for events like button clicks etc.
    window.mainloop()


if __name__ == "__main__":
    main()