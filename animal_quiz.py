def check_guess(guess, answer):
    global score
    if guess.lower() == answer.lower():
        print('Correct answer. ')
        score = score + 1
    else: 
        print('The correct answer is ' + answer)
        
score = 0
print('Guess the Animal')

guess1 = input('Which bear lives at the North Pole?')
check_guess(guess1, 'polar bear')

guess2 = input('Which is the fastest land animal?')
check_guess(guess2, 'cheetah')

guess3 = input('Which is the largest mammal?')
check_guess(guess3, 'blue whale')

print('Your score is ' + str(score) + ' out of 3.')

if score == 3:
    print('Full marks! Way to go!')
elif score == 2:
    print('Keep trying, you\'re almost there...')
else: 
    print('Better luck next time :(')