import random 
r = 'rock'
p = 'paper'
s = 'scissors'

user_score = 0
pc_score = 0

options = [r, p, s]
    
### print("Best out of 3 ")

def game(usrgame):
    pcgame = random.choice(options)
    if usrgame == 'p':
        usrgame = p
    elif usrgame == 'r':
        usrgame = r
    elif usrgame == 's':
        usrgame = s
    else:
        print("You didn't type a valid option. ")
        return
        
    if pcgame == usrgame:
        print(f"The computer chose {pcgame} and you chose {usrgame}, so IT'S A TIE!" )
        return
    usr_win(usrgame, pcgame)

def usr_win(usr, pc):
    if usr == r and pc == s or usr == p and pc == r or usr == s and pc == p:
        print(f'The computer chose {pc} and you chose {usr}, so YOU WON! ')
        user_score += 1
    else:
        print(f'The computer chose {pc} and you chose {usr}, so YOU LOST! ')
        pc_score += 1
while user_score <= 2 or pc_score <= 2:
    game(input("use 'r' for rock, 's' for scissors and 'p' for paper  "))

if user_score < pc_score:
    print(f" \n \n  YOU WON THE GAME, the final score was \n YOU: {user_score} \n PC: {pc_score}  ")
else:
    print(f" \n \n  Sorry, you lost the game, the final score was \n YOU: {user_score} \n PC: {pc_score}  ")