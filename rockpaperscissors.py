import random
from tkinter import *

x = Tk()
x.title('Rock Paper Scissors Game')
x.geometry('500x300')

schema = {
    'rock' : {'paper':0, 'rock':1, 'scissors':2},
    'paper': {'paper':1, 'rock':2, 'scissors':0},
    'scissors' : {'paper':2, 'rock':0, 'scissors':1}
}

computer_score = 0 
player_score= 0 

def result_handler(user_choice):
    global computer_score 
    global player_score
    outcomes = ['rock', 'paper', 'scissors']
    random_num = random.randint(0, 2)
    computer_choice = outcomes[random_num]
    result = schema[user_choice][computer_choice]
    
    player_choice_label.config(fg='darkred', text='player choice : '+str(user_choice))
    computer_choice_label.config(fg='slateblue', text='computer choice : '+str(computer_choice))
    
    if result ==2:
        player_score= player_score + 2 
        player_score_label.config(text='Player : '+str(player_score))
        result_label.config(fg='blue', text='result: player won!')
    elif result ==1:
        player_score= player_score + 1
        computer_score = computer_score + 1
        player_score_label.config(text='Player : '+str(player_score))
        computer_score_label.config(text='computer : '+str(computer_score))
        result_label.config(fg='blue', text='result: draw!')
    elif result==0:
        computer_score = computer_score + 2
        computer_score_label.config(text='computer : '+str(computer_score))
        result_label.config(fg='blue', text='result: computer won!')

        

Label(x, text="rock paper scissors", font=("Calibri", 14)).grid(row=0, sticky=N, pady=10, padx=150)
Label(x, text="select an option", font=("Calibri", 13)).grid(row=1, sticky=N)

player_score_label = Label(x, text="Player : ", font=("Calibri", 13))
player_score_label.grid(row=2, sticky=W)

computer_score_label = Label(x, text="Computer : ", font=("Calibri", 13))
computer_score_label.grid(row=2, sticky=E)

player_choice_label = Label(x, font=("Calibri", 13))
player_choice_label.grid(row=3, sticky=W)
computer_choice_label = Label(x, font=("Calibri", 13))
computer_choice_label.grid(row=3, sticky=E)

result_label = Label(x, font=("Calibri", 13))
result_label.grid(row=3, sticky=N)

Button(x, text='Rock', width=15, command=lambda: result_handler('rock')).grid(row=4, sticky=W, pady=5, padx=5)
Button(x, text='Paper', width=15, command=lambda: result_handler('paper')).grid(row=4, sticky=N, padx=5)
Button(x, text='Scissors', width=15, command=lambda: result_handler('scissors')).grid(row=4, sticky=E, pady=5, padx=5)

x.mainloop()