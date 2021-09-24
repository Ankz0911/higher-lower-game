from art import logo
game_end = False 
score = 0
random_variable = 0
while game_end == False :  
    print(logo)
    from game_data import data
    from art import vs
    import random
    from replit import clear
    
    variable_a = random.randint(0,49)
    variable_b = random.randint(0,49)
    
    if variable_b == variable_a : 
        variable_b = random.randint(0,49)
    if random_variable == 0 : 
        option_a = data[variable_a]
    else : 
        option_a = winning_person
    option_b = data[variable_b]
    print(f"A option is {option_a['name']}, a {option_a['description']} from {option_a['country']}")
    print(vs)
    print(f"B option is {option_b['name']}, a {option_b['description']} from {option_b['country']}")
    

    user_guess = input('Guess who has more followers ? A or B?\n').upper()

    if user_guess == "A":
        if option_a['follower_count'] > option_b['follower_count'] :
            score += 1
            clear()
            print(f'You are right , your score is {score}')
            winning_person = option_a
            random_variable = 1

        else :
            clear()
            game_end = True
            print(f"You are wrong , your final score is {score}")
            
    else:
        if option_b['follower_count'] > option_a['follower_count'] :
            score += 1
            clear()
            print(f'You are right , your score is {score}')
            winning_person = option_b
            random_variable = 1
        else :
            clear()
            game_end = True
            print(f"You are wrong, your final score is {score}")
        

