import random
import prompt


def check_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        rand = random.randint(0, 100)
        print(f'Question: {rand}')
        answer = prompt.string('Your answer:')

        if rand % 2 == 0 and answer == 'yes':
            print('correct!')
        elif rand % 2 == 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            return

        if rand % 2 == 1 and answer == 'no':
            print('correct!')

        elif rand % 2 == 1 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
