###############code with perfect alignment#########
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("700x500+300+300")
top.resizable(False, False)

main_frame = Frame(top, bg="tan1", bd=2)
main_frame.pack(fill="both", expand=True)

header_frame = Frame(main_frame, bg="tan1")
header_frame.pack(fill="x", pady=10)

label_header = Label(header_frame, text="Welcome to Text Adventure Game", bg="tan1", fg="black", font=("arial bold", 24))
label_header.pack(pady=10)

story_frame = Frame(main_frame, bg="tan1")
story_frame.pack(fill="x", pady=10)

label_story = Label(story_frame, text="", bg="tan1", fg="black", font=("arial", 18))
label_story.pack(pady=10)

choice_frame = Frame(main_frame, bg="tan1")
choice_frame.pack(fill="x", pady=10)

label_choice = Label(choice_frame, text="", bg="tan1", fg="black", font=("arial", 18))
label_choice.pack(pady=10)

current_room = 1

def intro():
    global label_story
    label_story.config(text="You find yourself in a dark dungeon. \n Your goal is to reach the treasure room.")

def choose_path():
    global label_choice
    label_choice.config(text="Choose path: \n Left or Right")

game_over = False

def handle_key(event):
    global current_room, label_story, label_choice, game_over
    if game_over:
        return
    if event.keysym == 'Left':
        if current_room == 1:
            label_story.config(text="You go left and find a key.")
            current_room = 2
        elif current_room == 2:
            label_story.config(text="You encounter a friendly merchant. \n He gives you a map.")
            current_room = 3
        elif current_room == 3:
            label_story.config(text="You go left and find a trapdoor.")
            current_room = 1
    elif event.keysym == 'Right':
        if current_room == 1:
            label_story.config(text="You go right, but there's a locked door. \n You need a key to proceed.")
        elif current_room == 2:
            label_story.config(text="You go right and encounter a monster!")
            label_choice.config(text="Do you want to fight or sneak around? \n Press Left to fight, Right to sneak around")
            top.bind('<Left>', fight_monster)
            top.bind('<Right>', sneak_around)
            return
        elif current_room == 3:
            label_story.config(text="You go right and find the treasure room.")
            messagebox.showinfo("You won.",'You found the treasure')
            top.quit()

def fight_monster(event):
    global label_story, current_room, label_choice
    label_story.config(text="You bravely fight the monster and defeat it.")
    current_room = 3
    top.bind('<Left>', handle_key)
    top.bind('<Right>', handle_key)
    label_choice.config(text="")

def sneak_around(event):
    global label_story, game_over
    label_story.config(text="You try to sneak around, \n but the monster spots you. \n It attacks, and you lose the game.")
    messagebox.showinfo("You lost.",'you were killed by monster')
    label_choice.config(text="")
    game_over = True  # set game_over flag to True
    top.unbind('<Left>')  # unbind left and right keys to prevent further gameplay
    top.unbind('<Right>')

top.bind('<Left>', handle_key)
top.bind('<Right>', handle_key)


intro()
choose_path()

top.mainloop()
