import prompt


NUMBER_OF_ROUNDS = 3


def cycle_of_game(game, description):
    is_won = True
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print(description)
    for _ in range(NUMBER_OF_ROUNDS):
        question, ansver_true = game()
        print(question)
        answer_user = prompt.string('Your answer:')
        if answer_user != ansver_true:
            is_won = False
            break            
        print('correct')
    else:
        print(f"'{answer_user}' is wrong answer ;(.\
         Correct answer was '{ansver_true}'.")
        print(f"Let's try again, {name}!")
    if is_won:
        print(f'Congratulations, {name}!')
