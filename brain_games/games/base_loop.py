import prompt


def loop(round, game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print(game.__doc__)
    for _ in range(round):
        question, ansver_true = game()
        print(question)
        answer_user = prompt.string('Your answer:')
        if answer_user == ansver_true:
        	print('correct')
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{ansver_true}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')