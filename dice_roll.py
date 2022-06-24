from tkinter import *
import random
from unittest import result

random.seed(6969696969)
root = Tk()
root.title("Game tai xiu")
root.geometry("400x320")
dice_faces = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

dice_labe = Label(root,font=("Helvetica",200))

result_label = Label(root,font=("Helvetica",40))


def roll():
    first_dice = random.randint(1,6)
    second_dice = random.randint(1,6)
    third_dice = random.randint(1,6)
    
    dice_labe.config(
        text=f'{dice_faces[first_dice-1]}{dice_faces[second_dice-1]}{dice_faces[third_dice-1]}'
    )
    dice_labe.pack()
    
    sum = first_dice + second_dice + third_dice
    result_label.config(text="tai" if sum>10 else "xiu", foreground="red" if sum>10 else "green")
    result_label.pack(after=dice_labe)
    

b1 = Button(root, text="quay tai xiu", foreground="blue", command=roll)
b1.pack()
root.mainloop()