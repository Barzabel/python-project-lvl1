import prompt


NUMBER_OF_ROUNDS = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print(game.DESCRIPTION)
    for _ in range(NUMBER_OF_ROUNDS):
        question, right_answer = game.generate_data_for_round()
        print("Question: {}".format(question))
        answer_user = prompt.string('Your answer:')
        if answer_user != right_answer:
            print("'{}' is wrong answer ;(.Correct answer was "
                  "'{}'.".format(answer_user, right_answer))
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
