import prompt


NUMBER_OF_ROUNDS = 3


def cycle_of_game(game, description):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print(description)
    for _ in range(NUMBER_OF_ROUNDS):
        question, ansver_true = game()
        print("Question: {}".format(question))
        answer_user = prompt.string('Your answer:')
        if answer_user != ansver_true:
            print("'{}' is wrong answer ;(.Correct answer was "
                  "'{}'.".format(answer_user, ansver_true))
            print(f"Let's try again, {name}!")
            break
        print('correct')
    else:
        print(f'Congratulations, {name}!')
